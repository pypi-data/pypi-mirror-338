# Twist Innovation API

## Overview
This is the **Twist Innovation API** – a Python library for interacting with Twist Innovation devices via MQTT.

## Installation

You can install this package using pip:

```bash
pip install twist-innovation-api
```

Alternatively, if you have cloned the repository, install it locally:

```bash
pip install .
```

## Contributing the Project (without installing in pip)
This repo can be tested with the include main.py. With this main.py, you don't need to install the package. If you just want to install and use, go to Usage
### Configuration
Before running the project, you need to create a configuration file named `config.yaml` in the project root directory. This file should contain your MQTT broker details:

```yaml
mqtt_broker: "your-mqtt-broker.com"
mqtt_user: "your-username"
mqtt_pass: "your-password"
mqtt_port: 1883  # Default MQTT port
```
### Testing
You can test the package using the included `main.py` file. Ensure you have a valid `config.yaml` file set up, then run:

```bash
python main.py
```

### Building
To build the package, run the following command:

```bash
python -m build
```

### Pushing to PyPi
To push the package to PyPi, run the following command:

```bash
twine upload dist/*
```



## Usage

Import the package in your Python scripts:

```python
import asyncio
import yaml
from typing import Callable, Awaitable
import aiomqtt

from twist import TwistAPI, TwistModel

# Load configuration
with open("config.yaml", 'r') as file:
    config = yaml.safe_load(file)

mqtt_broker = config["mqtt_broker"]
mqtt_user = config["mqtt_user"]
mqtt_pass = config["mqtt_pass"]
mqtt_port = config["mqtt_port"]

async def _noop(topic: str, payload: str):
    pass

callback_f :Callable[[str, str], Awaitable[None]]  = _noop


async def on_model_update(model: TwistModel):
    model.print_context()


async def main():
    global callback_f

    async with aiomqtt.Client(
        hostname=mqtt_broker,
        port=mqtt_port,
        username=mqtt_user,
        password=mqtt_pass
    ) as mqtt_client:

        # Async publish method
        async def mqtt_publish(topic: str, payload: str):
            await mqtt_client.publish(topic, payload)

        # Async subscribe method
        async def mqtt_subscribe(topic: str, callback: Callable[[str, str], None]):
            global callback_f
            callback_f = callback

            async def listen():
                await mqtt_client.subscribe(topic)
                async for message in mqtt_client.messages:
                    assert callback_f is not None
                    await callback_f(message.topic.value, message.payload.decode())

            asyncio.create_task(listen())

        # Initialize Twist API with async methods
        twist_api = TwistAPI(8)
        await twist_api.add_mqtt(mqtt_publish, mqtt_subscribe)

        twist_model_list: list[TwistModel] = await twist_api.search_models()

        for model in twist_model_list:
            model.register_update_cb(on_model_update)
            print(f"{type(model)} has Model id: {model.model_id}, Device id: {model.parent_device.twist_id}")
            
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())

```

## License
This project is licensed under the **GPL-3.0 License**. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## Contact
For any issues or questions, reach out via the [GitHub Issues](https://github.com/twist-innovation/twist-innovation-api/issues).

