import allure
import pytest
from selenium.webdriver import Chrome
from pageobjects.home_page import HomePage
from pageobjects.site_menu import SiteMenu
from assertpy import assert_that
from time import sleep


@pytest.fixture()
@allure.title('Тестирование функциональности сайта "Читай-город"')
def driver():
    chrome = Chrome()
    yield chrome
    chrome.quit()

# @allure.title('Тестирование работы кнопки переключения:')
# @allure.severity(allure.severity_level.TRIVIAL)
# def test_ToggleButton(driver):
#      home_page = HomePage(driver)
#      site_menu = SiteMenu(driver)
#      with allure.step('- открываю главную страницу сайта "Читай-город"'):
#           home_page.open()
#      with allure.step('- нажимаю кнопку "Каталог"'):
#           home_page.clickCatalog()
#      with allure.step('-перехожу в пункт меню "Художественная литература"'):
#           site_menu.clickCatalogButtonFiction()
#           sleep(2)
#      with allure.step('-проверяю работу кнопки переключения"'):
#           books_in_list = site_menu.textCatalogListHead()
#           site_menu.clickToggleButton()
#           sleep(2)
#           books_in_stock = site_menu.textCatalogListHead()
#      with allure.step('Проверяю, что количество всех книг каталога больше, чем количество книг в наличии'):
#           assert_that(site_menu.CatalogHead(books_in_list)).is_greater_than_or_equal_to(site_menu.CatalogHead(books_in_stock))

# @allure.title('Тестирование функции поиска при вводе корректных значений:')
# @allure.severity(allure.severity_level.TRIVIAL)
# def test_SearchButtonCorrect(driver):
#     home_page = HomePage(driver)
#     site_menu = SiteMenu(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#           home_page.open()
#     with allure.step('- ввожу в поле Поиска значение "Анна Каренина" и нажимаю кнопку "Поиск"'):
#           site_menu.searchButton('анна каренина')
#           text1 = site_menu.textSearchResult()
#     with allure.step('- в результатах поиска проверяю наличие надписи "Показываем результаты по запросу"'):
#           assert_that(text1).contains('Показываем результаты по запросу')

@allure.title('Тестирование функции поиска при вводе некорректных значений:')
@allure.severity(allure.severity_level.TRIVIAL)
def test_SearchButtonIncorrect(driver):
    home_page = HomePage(driver)
    site_menu = SiteMenu(driver)
    with allure.step('- открываю главную страницу сайта "Читай-город"'):
         home_page.open()
    with allure.step('- ввожу в поле Поиска значение "000000000000000000000000" и нажимаю кнопку "Поиск"'):
         site_menu.searchButton('000000000000000000000000')
         text2 = site_menu.textEemptyResult()
    with allure.step('- в результатах поиска проверяю наличие надписи "Похоже, у нас такого нет"'):
         assert_that(text2).is_equal_to('Похоже, у нас такого нет')

