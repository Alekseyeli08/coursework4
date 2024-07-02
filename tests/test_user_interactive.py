import pytest
from src.HH_Api import HH_Api
from src.user_interactive import UserInteractive


@pytest.fixture
def test():
    test = UserInteractive()
    test.vacancies_list = []
    return test


def test_top_n_salary(test):
    assert UserInteractive.top_n_salary(test, 0) == []
