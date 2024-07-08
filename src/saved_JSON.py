import json
import os.path
from abc import ABC, abstractmethod


class Json(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def delite_file(self):
        pass


class Saved_JSON(Json):
    """
    Класс для чтения и сохранения файлов в формате Json
    """
    def __init__(self, file_name = "vacancies.json"):
        self.__file_name = os.path.abspath(f"../data/{file_name}")

    def read_file(self, data):
        with open(self.__file_name, 'r', encoding='UTF - 8') as file:
            return json.load(file)

    def load_file(self, data):
        with open(self.__file_name, 'a', encoding='UTF - 8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delite_file(self):
        pass
