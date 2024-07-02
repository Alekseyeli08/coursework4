
class Vacancy:
    def __init__(self, name: str, url: str, area, salary: int, description: str | None, schedule: str, currency):
        self.name: str = name
        self.url: str = url
        self.area: str = area
        self.salary: int = salary
        self.description: str = self._validate(description)
        self.schedule: str = schedule
        self.currency = currency

    @staticmethod
    def _validate(description: str | None) -> str:
        if description:
            return description
        else:
            return "нет описания вакансии"

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f"""
Название вакансии: {self.name}
Ссылка на вакансию: {self.url}
Город: {self.area}
Заработная плата: {self.salary if self.salary else "Не указана"} {self.currency}
Описание вакансии: {self.description.replace("<highlighttext>", "").replace(
            "</highlighttext>", "")}
Занятость: {self.schedule}"""

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        url = vacancy.get("alternate_url")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
                currency = vacancy.get("salary").get('currency')
            else:
                currency = ''
                salary = 0
        else:
            currency = ''
            salary = 0

        description = vacancy.get("snippet").get("responsibility")
        schedule = vacancy.get("schedule").get("name")
        return cls(name, url, area, salary, description, schedule, currency)