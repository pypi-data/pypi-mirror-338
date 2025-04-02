import asyncio
import logging
from lw2.lightware import LightwareLW2

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def main():
    lw2 = LightwareLW2("192.168.21.51")
    await lw2.connect()
    await lw2.update()

    print(lw2.mapping)
    print(lw2.firmware)
    print(lw2.serial)
    print(lw2.product_type)
    print(lw2.mac)
    print(lw2.web_version)
    print(lw2.server_version)
    await lw2.close()


# Run the async function
asyncio.run(main())
