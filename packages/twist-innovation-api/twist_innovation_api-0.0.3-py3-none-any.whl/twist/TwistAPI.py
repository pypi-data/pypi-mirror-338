# Copyright (C) 2025 Twist Innovation
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU General Public License for more details:
# https://www.gnu.org/licenses/gpl-3.0.html


import asyncio
import json
import random

from .TwistDevice import TwistDevice, TwistModel
from .TwistTypes import DeviceVariant


class TwistAPI:
    def __init__(self, installation_id: int):
        self._ext_publish = None
        self._subscribe = None

        self.function_map = {
            "context": self._context_msg,
            "getboard": self._get_board
        }

        self.device_list: list[TwistDevice] = list()

        # TODO: this should come from the API
        self.installation_id = installation_id

    async def add_mqtt(self, publisher, subscriber):
        self._ext_publish = publisher
        self._subscribe = subscriber

        await self._subscribe(f"v2/{self.installation_id}/rx/#", self._on_message_received)

    async def search_models(self):
        await self.getboard(0xffffffff)
        await asyncio.sleep(3)

        model_list: list[TwistModel] = list()
        for device in self.device_list:
            for model in device.model_list:
                model_list.append(model)

        return model_list

    async def _publish(self, twist_id, opcode, payload: dict | None = None, model_id=None):
        if self._ext_publish is not None:
            topic = f"v2/{self.installation_id}/tx/{twist_id}/{opcode}"
            if payload is None:
                payload = dict()
            payload["key"] = random.randint(1, 65535)
            if model_id is not None:
                topic = f"{topic}/{model_id}"

            await self._ext_publish(topic, json.dumps(payload))

    async def getboard(self, twist_id):
        await self._publish(twist_id, "getboard")

    async def activate_event(self, model: TwistModel, data: json):
        await self._publish(model.parent_device.twist_id, "activate_event", data, model.model_id)

    def _parse_topic(self, topic):
        tpc_delim = topic.split('/')

        model_id = None
        if len(tpc_delim) == 6:
            model_id = int(tpc_delim[5])

        return {
            "twist_id": int(tpc_delim[3]),
            "opcode": tpc_delim[4],
            "model_id": model_id
        }

    async def _on_message_received(self, topic, payload, qos=None):
        data = self._parse_topic(topic)
        if any(dev.twist_id == data["twist_id"] for dev in self.device_list) or data["opcode"] == "getboard":
            if data["opcode"] in self.function_map:
                await self.function_map[data["opcode"]](data["twist_id"], payload, data["model_id"])

    async def _context_msg(self, twist_id, payload, model_id):
        device = next((d for d in self.device_list if d.twist_id == twist_id), None)
        await device.context_msg(model_id, payload)

    async def _get_board(self, twist_id, payload, model_id=None):
        data = json.loads(payload)
        if not any(dev.twist_id == twist_id for dev in self.device_list):
            self.device_list.append(TwistDevice(twist_id, data["h"], DeviceVariant(data["v"]), self))
            print(f"New device with id: {twist_id}")
