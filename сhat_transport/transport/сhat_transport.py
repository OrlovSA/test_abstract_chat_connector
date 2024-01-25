from abc import ABC, abstractmethod


__all__ = ("ChatTransport",)


class ChatTransport(ABC):
    @abstractmethod
    def add_handler(self, event: str, text: str):
        raise NotImplementedError

    @abstractmethod
    async def send_message(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    async def run(self):
        raise NotImplementedError
