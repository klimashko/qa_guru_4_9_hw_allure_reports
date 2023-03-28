from time import sleep

import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "klimashko")
@allure.feature("Тест только селен без шагов")
@allure.story("Нужен для сравнения с тестами степовой моделью")
@allure.link("https://github.com", name="Testing")
def test_github1():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('klimashko/qa_guru_4_9_hw_allure_reports')
    s('.header-search-input').submit()

    s(by.link_text('klimashko/qa_guru_4_9_hw_allure_reports')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)

