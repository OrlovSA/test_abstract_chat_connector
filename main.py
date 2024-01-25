import asyncio

from сhat_transport.resources.config import settings, logger
from сhat_transport.transport import *


class BusinessLogicBot:
    def __init__(self, transport: ChatTransport):
        self.transport = transport
        self.transport.add_handler("ping", "pong")
    

    async def logic(self):
        await self.transport.send_message(msg="test")
    

async def main(transport_name: ChatTransportEnum = settings.CHAT_TRANSPORT) -> None:
    transport: ChatTransport = CHOICE_TRANSPORT[transport_name]()
    bot = BusinessLogicBot(transport)

    await bot.transport.run()
    await bot.logic()

if __name__ == '__main__':
    asyncio.run(main())