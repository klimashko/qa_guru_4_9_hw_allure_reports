import allure
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from time import sleep




def test_github2():
    with allure.step('Открываем главую страницу GitHub'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Открываем репозиторий'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)






