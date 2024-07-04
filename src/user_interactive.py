from src.AbstractApi import HH


class UserInteractive:
    def __init__(self):
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH()
        return hh.load_vacancies(keyword)

    def top_n_salary(self, top_n):
        """
        Метод для сортировки по зарплате
        """
        self.vacancies_list = list(sorted(self.vacancies_list, reverse=True))
        return self.vacancies_list[:top_n]

    def filter_vacancies(self, keywords):
        """
        Метод для поиска вакансий по ключевым словам
        """
        self.vacancies_list = [elem for elem in self.vacancies_list if elem.name.find(keywords) != -1]
        return self.vacancies_list

