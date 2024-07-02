from HH_Api import HH_Api


class UserInteractive:
    def __init__(self):
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH_Api()
        return hh.load_vacancies(keyword)

    def top_n_salary(self, top_n):
        self.vacancies_list = list(sorted(self.vacancies_list, reverse=True))[:top_n]

    def filter_vacancies(self, keywords):
        self.vacancies_list = [elem for elem in self.vacancies_list if elem.name.find(keywords) != -1]
