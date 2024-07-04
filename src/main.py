from saved_JSON import Saved_JSON
from vacancy import Vacancy
from user_interactive import UserInteractive


# Функция для взаимодействия с пользователем
def user_interaction():
    user_class = UserInteractive()
    user_input = input("Введите название вакансии: ")
    top_n = int(input("Введите количество вакансий с наивысшей зп: "))
    keyword = input("Введите ключевое слово: ")
    for i in user_class.get_vacancies_list(user_input):
        new_vacancy = Vacancy.new_vacancy(i)
        user_class.vacancies_list.append(new_vacancy)

    user_class.filter_vacancies(keyword)
    user_class.top_n_salary(top_n)
    save_file = Saved_JSON()
    save_file.load_file(user_class.get_vacancies_list(user_input))
    for vacancy in user_class.vacancies_list:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()