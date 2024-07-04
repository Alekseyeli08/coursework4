import pytest
from src.user_interactive import UserInteractive
from src.vacancy import Vacancy


@pytest.fixture
def test():
    test = UserInteractive()
    test_list = []
    for i in range(10):
        test_vac = Vacancy(
            f"testname {i}",
            f"testurl {i}",
            f"testarea {i}",
            i * 1000,
            f"description {i}",
            f"testschedule {i}",
            f"testcurrency {i}")
        test_list.append(test_vac)
    test.vacancies_list = test_list
    return test


def test_top_n_salary(test):
    assert UserInteractive.top_n_salary(test, 0) == []


def test_top_n_salary_2(test):
    assert len(UserInteractive.top_n_salary(test, 5)) == 5


def test_top_n_salary_3(test):
    assert UserInteractive.top_n_salary(test, 1)[0].salary == 9000


def test_filter_vacancies(test):
    assert UserInteractive.filter_vacancies(test, "testurl1") == []

