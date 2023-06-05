import allure
import pytest
from selenium.webdriver import Chrome
from pageobjects.home_page import HomePage
from assertpy import assert_that
from time import sleep


@pytest.fixture()
@allure.title('Тестирование главной страницы сайта "Читай-город"')
def driver():
    chrome = Chrome()
    yield chrome
    chrome.quit()

# @allure.title('Тестирование Логотипа страницы "Читай-город":')
# @allure.severity(allure.severity_level.MINOR)
# def test_Logo(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.clickCollectionsButton()
#     with allure.step('- нажимаю кнопку "Подборки", перехожу на страницу "Подборки"'):
#          home_page.clickFavicon()
#     with allure.step('- нажимаю кнопку Логотипа'):
#          expected_home_url = 'https://www.chitai-gorod.ru/'
#     with allure.step('- проверяю, что программа перешла на главную страницу'):
#          actual_url_1 = driver.current_url
#          home_page.clickCatalog()
#     with allure.step('- нажимаю кнопку "Каталог", из выпадающего меню выбираю пункт "Сувениры", перехожу на страницу "Сувениры"'):
#          home_page.clickSouvenirs()
#     with allure.step('- нажимаю кнопку Логотипа'):
#          sleep(2)
#          home_page.clickFavicon()
#          actual_url_2 = driver.current_url
#     with allure.step('- проверяю, что программа перешла на главную страницу'):
#          assert_that(expected_home_url).is_equal_to(actual_url_1)
#          assert_that(expected_home_url).is_equal_to(actual_url_2)

@allure.title('Тестирование кнопок главного меню:')
def test_Menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    with allure.step('- открываю главную страницу сайта "Читай-город"'):
         expected_buttons_url = ['https://www.chitai-gorod.ru/promotions','https://www.chitai-gorod.ru/collections',
                                 'https://www.chitai-gorod.ru/articles','https://www.chitai-gorod.ru/books-series']
    with allure.step('- нажимаю поочередно все кнопки меню и проверяю URL загружаемых страниц'):
          assert_that(expected_buttons_url).is_equal_to(home_page.mainMenuButtonsUrl())



