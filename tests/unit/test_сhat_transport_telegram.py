import pytest
from unittest.mock import AsyncMock
from aiogram.filters import Command

from сhat_transport.transport import *
from tests.mock import *


@pytest.mark.asyncio
async def test_add_handler(telegram_bot: ChatTransportTelegram, router_mock):
    event = "test"
    text = "test message"
    telegram_bot.router = router_mock

    telegram_bot.add_handler(event=event, text=text)

    router_mock.message.assert_called_once()
    assert isinstance(router_mock.message.call_args[0][0], Command)


@pytest.mark.asyncio
async def test_send_message(telegram_bot: ChatTransportTelegram):
    bot_mock = AsyncMock()
    telegram_bot.bot = bot_mock

    msg = "Test"
    chat_id = 123

    await telegram_bot.send_message(msg, chat_id)

    bot_mock.send_message.assert_awaited_once_with(chat_id, msg)