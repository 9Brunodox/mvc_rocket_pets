from typing import Dict
from abc import ABC, abstractmethod

class PetsListControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass


