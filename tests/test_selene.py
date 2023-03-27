from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from time import sleep




def test_github1():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)




