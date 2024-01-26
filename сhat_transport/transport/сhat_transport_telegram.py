from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
from aiogram.types import Message

from сhat_transport.resources.config import logger, settings
from сhat_transport.transport.сhat_transport import ChatTransport


__all__ = ("ChatTransportTelegram",)


class ChatTransportTelegram(ChatTransport):
    def __init__(self, token: str = settings.TELEGRAM_API_TOKEN) -> None:
        bot = Bot(token=token)
        self.dp = Dispatcher()
        self.router = Router()
        self.bot = bot

    def add_handler(self, event: str, text: str) -> None:
        async def generic_handler(message: Message):
            await message.answer(text)

        self.router.message(Command(event))(generic_handler)

    async def send_message(
        self, msg: str, chat_id: int = settings.TELEGRAM_CHAT_ID
    ) -> None:
        logger.info(f"{msg=}, {chat_id=}")
        await self.bot.send_message(chat_id, msg)

    async def run(self) -> None:
        logger.info("run telegram bot")

        self.dp.include_router(self.router)
        await self.dp.start_polling(self.bot)
