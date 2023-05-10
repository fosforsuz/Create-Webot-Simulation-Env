from abc import ABC, abstractmethod


class Instance(ABC):
    
    @staticmethod
    @abstractmethod
    def get_instance(object_count: int) -> str:
        pass
