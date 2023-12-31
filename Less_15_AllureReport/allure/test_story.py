# $ pytest tests.py --allure-features feature2 --allure-stories story2

import allure


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.feature('Авторизация')
@allure.story('Валидные данные')
def test_with_epic_1():
    pass


@allure.story('Забыли пароль')
def test_with_story_1():
    pass


@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('Авторизация')
@allure.story('Невалидные данные')
def test_with_story_2_and_feature_2():
    pass
