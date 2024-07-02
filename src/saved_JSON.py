import json
import os.path
from abc import ABC, abstractmethod


class Json(ABC):

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

    def __init__(self):
        self.file_name = ""
        self.abs_path = os.path.abspath("../data/vacancies.json")

    def read_file(self, data):
        with open(self.abs_path, 'r', encoding='UTF - 8') as file:
            return json.load(file)

    def load_file(self, data):
        with open(self.abs_path, 'a', encoding='UTF - 8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delite_file(self):
        pass
