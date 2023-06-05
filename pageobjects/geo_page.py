from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC #для явного ожидания

class GeoPage:
    menu_geo_button = (By.XPATH, '//span[@class="header-city__title"]') #кнопка геолокации в главном меню
    city_button = (By.XPATH,'//div[@class="button change-city__button change-city__button--cancel light-blue"]')#кнопка "Нет, изменить город"
    city_input = (By.XPATH, '//input[@class="city-modal__city-input"]') #поле "Название города"
    city_list_item = (By.XPATH, '//li[@class="cities-list__item"][1]') #список с названием городов - 1 элемент (после поиска)
    header_city_title = (By.XPATH, '//span[@class="header-city__title"]') # заголовок с названием города
    delivery_button = (By.XPATH, '//a[@href="/delivery"]')  # кнопка "Доставка и оплата"
    city_delivery = (By.XPATH, '//div[@class="delivery-block__city-name"]')  # название города на странице "Доставка и оплата"
    city_list_item_2 = (By.XPATH, '//li[@class="city-modal__popular-item"][2]') # второй элемент из списка городов ("Санкт-Петербург")
    city_error_search = (By.XPATH, '//div[@class="city-modal__search-empty"]') #надпись при ошибке поиска "Извините, такого города не знаем"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

    def clickMenuGeoButton(self):
        self.wait.until(EC.visibility_of_element_located(self.menu_geo_button))
        self.driver.find_element(*self.menu_geo_button).click()


    def clickCityButton(self):
        self.wait.until(EC.visibility_of_element_located(self.city_button))
        self.driver.find_element(*self.city_button).click()

    def fillCityInput(self, city_name):
        self.wait.until(EC.visibility_of_element_located(self.city_input))
        self.driver.find_element(*self.city_input).send_keys(city_name)

    def clickCityListItem(self):
        self.driver.find_element(*self.city_list_item).click()

    def headerCityTitle(self):
        self.wait.until(EC.visibility_of_element_located(self.header_city_title))
        title_text = self.driver.find_element(*self.header_city_title).text
        return title_text

    def clickDeliveryButton(self):
        self.wait.until(EC.visibility_of_element_located(self.delivery_button))
        self.driver.find_element(*self.delivery_button).click()

    def clicCityDelivery(self):
        self.driver.find_element(*self.city_delivery).click()

    def textDelivery(self):
        self.wait.until(EC.visibility_of_element_located(self.city_delivery))
        city_text = self.driver.find_element(*self.city_delivery).text
        return city_text

    def clckCityListIitem2(self):
        self.wait.until(EC.visibility_of_element_located(self.city_list_item_2))
        self.driver.find_element(*self.city_list_item_2).click()

    def textCityEerrorSearch(self):
        self.wait.until(EC.visibility_of_element_located(self.city_error_search))
        error_text = self.driver.find_element(*self.city_error_search).text
        return error_text