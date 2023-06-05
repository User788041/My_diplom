import allure
import pytest
from selenium.webdriver import Chrome
from pageobjects.home_page import HomePage
from pageobjects.geo_page import GeoPage
from assertpy import assert_that
from time import sleep

@pytest.fixture()
@allure.title('Тестирование функции геолокации сайта "Читай-город"')
def driver():
    chrome = Chrome()
    yield chrome
    chrome.quit()


# @allure.title('Тестирование смены города пользователя через верхнее меню:')
# def test_GeoLocation(driver):
#     home_page = HomePage(driver)
#     geo_page = GeoPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- нажимаю кнопку смены города в верхнем меню, выбираю пункт "Нет, изменить город" '):
#         geo_page.clickMenuGeoButton()
#     with allure.step('- в окне "Выберите город" в поле "Название города" ввожу значение "Рязань"'):
#         geo_page.clickCityButton()
#         geo_page.fillCityInput('Рязань')
#     with allure.step('- в появившемся списке выбираю "Рязань, Рязанская область"'):
#         sleep(2)
#         geo_page.clickCityListItem()
#         expected_city_name = 'Россия, Рязань'
#     with allure.step('- проверяю, что название города в верхнем меню изменилось на "Рязань"'):
#         assert_that(expected_city_name).is_equal_to(geo_page.headerCityTitle())

# @allure.title('Тестирование смены города на странице "Доставка и оплата" при изменении города через верхнее меню:')
# def test_Delivery(driver):
#     home_page = HomePage(driver)
#     geo_page = GeoPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- нажимаю кнопку смены города в верхнем меню, выбираю пункт "Нет, изменить город" '):
#          geo_page.clickMenuGeoButton()
#     with allure.step('- в окне "Выберите город" в поле "Название города" ввожу значение "Рязань"'):
#          geo_page.clickCityButton()
#          geo_page.fillCityInput('Рязань')
#     with allure.step('- в появившемся списке выбираю "Рязань, Рязанская область"'):
#          geo_page.clickCityListItem()
#     with allure.step('- нажимаю пункт меню "Доставка и оплата"'):
#          sleep(2)
#          geo_page.clickDeliveryButton()
#          expected_city_name_1 = 'Россия, Рязань'
#     with allure.step('- проверяю, что на странице "Доставка и оплата" появилась надпись "Куда везём Россия, Рязань"'):
#          assert_that(expected_city_name_1).is_equal_to(geo_page.textDelivery())

# @allure.severity(allure.severity_level.MINOR)
# @allure.title('Тестирование смены города пользователя через верхнее меню путем выбора названия из списка городов:"')
# def test_DeliveryCity(driver):
#     home_page = HomePage(driver)
#     geo_page = GeoPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- нажимаю кнопку смены города в верхнем меню, выбираю пункт "Нет, изменить город" '):
#          geo_page.clickMenuGeoButton()
#          geo_page.clickCityButton()
#     with allure.step('- в окне "Выберите город" из списка городов выбираю "Санкт-Петербург"'):
#          geo_page.clckCityListIitem2()
#          sleep(2)
#          expected_city_name_2 = 'Россия, Санкт-Петербург'
#     with allure.step('- проверяю, что название города в верхнем меню изменилось на "Санкт-Петербург"'):
#          assert_that(expected_city_name_2).is_equal_to(geo_page.headerCityTitle())

@allure.severity(allure.severity_level.MINOR)
@allure.title('Тестирование функции поиска города при вводе некорректных значений:')
def test_BadCitySearch(driver):
    home_page = HomePage(driver)
    geo_page = GeoPage(driver)
    with allure.step('- открываю главную страницу сайта "Читай-город"'):
         home_page.open()
    with allure.step('- нажимаю кнопку смены города в верхнем меню, выбираю пункт "Нет, изменить город" '):
         geo_page.clickMenuGeoButton()
         geo_page.clickCityButton()
    with allure.step('- в окне "Выберите город" в поле "Название города" ввожу значение "111222333"'):
         geo_page.fillCityInput('111222333')
    with allure.step('- в результатах поиска проверяю наличие надписи "Извините, такого города не знаем"'):
         expected_error_text = 'Извините, такого города не знаем'
         assert_that(expected_error_text).is_equal_to(geo_page.textCityEerrorSearch())

