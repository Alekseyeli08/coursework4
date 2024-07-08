from abc import ABC, abstractmethod
import requests


class AbstractApi(ABC):
    """
    Абстрактный класс для работы с API
    """
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(AbstractApi):
    """
    Класс для получания вакансий по ключевому слову
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.url, headers=self._headers, params=self.__params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1

            return vacancies