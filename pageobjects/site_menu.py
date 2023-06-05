from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания

class SiteMenu:

    catalog_button_fiction = (By.XPATH, '//a[@href="/catalog/books/hudozhestvennaya-literatura-9657"]')  # кнопка "Художественная литература"
    toggle_button = (By.XPATH, '//div[@class="toggle-button"]') # кнопка переключение - неактивна
    catalog_list_head = (By.XPATH, '//div[@class="catalog-list-head__total"]')  # количество книг в разделе
    search_field = (By.XPATH, '//input[@class="header-search__input"]')  # поле поиска
    search_button = (By.XPATH, '//button[@class="header-search__button"]')  # кнопка "Поиск"
    search_result_text = (By.XPATH, '//p[@class="search-page__found-message"]')  # текст "Поиск"
    catalog_empty_result_header = (By.XPATH, '//h4[@class="catalog-empty-result__header"]')  # текст "Похоже у нас такого нет"
    button_search_clear = (By.XPATH, '//button[@class="header-search__clear"]')  # кнопка очистить поле поиска (крестик)

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    def clickCatalogButtonFiction(self):
        self.driver.find_element(*self.catalog_button_fiction).click()

    def clickToggleButton(self):
        self.wait.until(EC.visibility_of_element_located(self.toggle_button))
        self.driver.find_element(*self.toggle_button).click()

    def clickButtonSearchClear(self):
        self.wait.until(EC.visibility_of_element_located(self.button_search_clear))
        self.driver.find_element(*self.button_search_clear).click()

    def textCatalogListHead(self):
        self.wait.until(EC.visibility_of_element_located(self.catalog_list_head))
        text = self.driver.find_element(*self.catalog_list_head).text
        return text

    def searchButton(self, book_name):
        self.driver.find_element(*self.search_field).send_keys(book_name)
        self.driver.find_element(*self.search_button).click()

    def textSearchResult(self):
        self.wait.until(EC.presence_of_element_located(self.search_result_text))
        text = self.driver.find_element(*self.search_result_text).text
        return text

    def textEemptyResult(self):
        self.wait.until(EC.presence_of_element_located(self.catalog_empty_result_header))
        text = self.driver.find_element(*self.catalog_empty_result_header).text
        return text

    def CatalogHead(self, total):
        books = ''
        for i in total:
            if i.isdigit():
                books += i
        return int(books)

