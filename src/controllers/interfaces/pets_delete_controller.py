from abc import ABC, abstractmethod

class PetsDeleteControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass