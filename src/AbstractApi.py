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
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

            return vacancies