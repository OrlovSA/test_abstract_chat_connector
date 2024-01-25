from сhat_transport.resources.enum import ChatTransportEnum
from сhat_transport.transport.сhat_transport import *
from сhat_transport.transport.сhat_transport_discord import *
from сhat_transport.transport.сhat_transport_telegram import *


CHOICE_TRANSPORT = {
    ChatTransportEnum.TELEGRAM: ChatTransportTelegram,  # noqa
    ChatTransportEnum.DISCORD: ChatTransportDiscord,  # noqa
}
