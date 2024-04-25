from abc import ABC, abstractmethod


class Gateway(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def receive(self):
        pass
