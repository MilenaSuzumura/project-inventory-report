from abc import ABC, abstractmethod


class importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, path):
        ...
