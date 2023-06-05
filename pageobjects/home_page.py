
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания
from time import sleep

class HomePage:
    main_menu_buttons = (By.XPATH, '//a[@class="header-bottom__link"]')  # кнопки главного меню
    menu_button_collections = (By.XPATH, '//a[@href="/collections"]')  # кнопка "Коллекции"
    text_collections = (By.CLASS_NAME, 'app-title')  # текcт "Подборки"
    favicon_button = (By.CLASS_NAME, 'header-logo__icon')  # кнопка фавикона
    menu_button_catalog = (By.CLASS_NAME,'catalog__button')  # кнопка "Каталог"
    menu_button_souvenirs = (By.XPATH, '//a[@href="/catalog/souvenirs"]')  # кнопка "Сувениры" в меню "Каталог"
    souvenirs_text = (By.XPATH, '//h1[@class="app-title app-title--mounted catalog-template__sidebar-title app-title--header-1 app-title--caps"]')
    text_title = (By.XPATH, '//h1[@itemprop = ""]')


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(50)
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()

    def open(self):
        self.driver.get('https://www.chitai-gorod.ru/')

    def clickCollectionsButton(self):
        self.wait.until(EC.visibility_of_element_located(self.menu_button_collections))
        self.driver.find_element(*self.menu_button_collections).click()

    def clickFavicon(self):
        self.driver.find_element(*self.favicon_button).click()

    def clickCatalog(self):
        self.driver.find_element(*self.menu_button_catalog).click()

    def clickSouvenirs(self):
        self.wait.until(EC.visibility_of_element_located(self.menu_button_souvenirs))
        self.driver.find_element(*self.menu_button_souvenirs).click()

    def textSouvenirs(self):
        self.wait.until(EC.visibility_of_element_located(self.souvenirs_text))
        text = self.driver.find_element(*self.souvenirs_text).text
        return text

    def mainMenuButtonsUrl(self):
        main_menu = self.driver.find_elements(*self.main_menu_buttons)
        new_arr_titles = []
        for i in range(len(main_menu)):
            main_menu[i].click()
            sleep(2)
            new_arr_titles.append(self.driver.current_url)
        return new_arr_titles


