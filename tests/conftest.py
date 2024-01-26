import pytest
from сhat_transport.transport.сhat_transport_telegram import ChatTransportTelegram


@pytest.fixture
def telegram_bot():
    return ChatTransportTelegram(token="6773878599:AAEiBWL2X4H7PLALSRkx_e8kdxjo9olreKE")
