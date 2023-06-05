from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания


class CartPage:

    cart_button_header = (By.XPATH, '//a[@href="/cart"]')  # кнопка "Корзина" в заголовке сайта
    product_title = (By.XPATH, '//div[@class="product-title__head"]')  # заголовок книги
    #product_title = (By.XPATH, '(//div[@class="product-title__head"])[1]')  # заголовок книги
    buy_button = (By.XPATH, '//div[@class="button action-button blue"]')  # кнопка "Купить"
    buy_button_in_cart = (By.XPATH, '//span[@class="action-button__text"]')  # кнопка "Оформить заказ"
    cart_badge = (By.XPATH, '//span[@class="badge-notice header-cart__badge"]')  # значок на корзине с количеством товара
    price_product = (By.XPATH, '//div[contains(@class, "product-price__value")]')  # цена товара
    catalog_novelty = (By.XPATH, '//a[@href="/catalog/collections/novelty"]') #надпись новинки литературы
    #total_value = (By.XPATH, '//div[@class="total-value"]')  # Итого в Корзине
    total_value = (By.XPATH, '//div[@class="info-item cart-sidebar__item-summary"]//div[@class="info-item__value"]')  # Итого в Корзине
    delete_many = (By.XPATH, '//div[@class="delete-many"]')  # Очистить корзину
    recover_cart = (By.XPATH, '//div[@class="button cart-multiple-delete__button blue"]') # Восстановить корзину
    cart_multiple_delete_title = (By.XPATH, '//p[@class="cart-multiple-delete__title"]')  # Надпись "Корзина очищена"
    product_quantity_increase_button = (By.XPATH, '//button[@class="product-quantity__button product-quantity__button'
                                                  '--right"]') # кнопка увеличить количество книг в корзине "+"
    product_quantity_decrease_button = (By.XPATH, '//button[@class="product-quantity__button product-quantity__button'
                                                  '--left"]')# кнопка уменьшить количество книг в корзине "-"


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(50)
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()


    def scrollCatalogNovelty(self):
        target = self.driver.find_element(*self.catalog_novelty)
        self.wait.until(EC.visibility_of_element_located(self.catalog_novelty))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', target)

    def clickProductTitle(self):
        self.wait.until(EC.visibility_of_element_located(self.product_title))
        self.driver.find_element(*self.product_title).click()

    def clickCartButtonHeader(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_button_header))
        self.driver.find_element(*self.cart_button_header).click()

    def clickDeleteMany(self):
        self.driver.find_element(*self.delete_many).click()

    def clickRecoverCart(self):
        self.wait.until(EC.visibility_of_element_located(self.recover_cart))
        self.driver.find_element(*self.recover_cart).click()

    def textProductTitle(self):
        self.wait.until(EC.visibility_of_element_located(self.product_title))
        text = self.driver.find_element(*self.product_title).text
        return text

    def textCartMultipleDelete(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_multiple_delete_title))
        text = self.driver.find_element(*self.cart_multiple_delete_title).text
        return text

    def clickBuy_button(self):
        self.wait.until(EC.visibility_of_element_located(self.buy_button))
        self.driver.find_element(*self.buy_button).click()

    def Buy_button(self):
        self.driver.find_element(*self.buy_button)

    def textBuyButtonInCart(self):
        self.wait.until(EC.visibility_of_element_located(self.buy_button_in_cart))
        text = self.driver.find_element(*self.buy_button_in_cart).text
        return text

    def textCartBadge(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_badge))
        text = self.driver.find_element(*self.cart_badge).text
        return text

    def textPriceProduct(self):
        self.wait.until(EC.presence_of_element_located(self.price_product))
        text = self.driver.find_element(*self.price_product).text
        return text

    def textTotalValue(self):
        text = self.driver.find_element(*self.total_value).text
        return text

    def TotalValue(self):
        self.driver.find_element(*self.total_value)

    def AddBooks(self, n):
        self.wait.until(EC.visibility_of_element_located(self.buy_button))
        for i in range(n):
            self.driver.find_element(*self.buy_button).click()

    def IncreaseBooksInCart(self, n):
        self.wait.until(EC.visibility_of_element_located(self.product_quantity_increase_button))
        for i in range(n):
            self.driver.find_element(*self.product_quantity_increase_button).click()

    def FromStringToNum(self, total):
        books = ''
        for i in total:
            if i.isdigit():
                books += i
        return int(books)

    def textProductTitles(self):
        self.wait.until(EC.presence_of_element_located(self.product_title))
        text_title = self.driver.find_elements(*self.product_title)
        new_arr_titles = []
        for i in range(len(text_title)):
            new_arr_titles.append(text_title[i].text)
        return new_arr_titles

    def PriceSum(self):
        text_price = self.driver.find_elements(*self.price_product)
        new_arr_price = []
        for i in range(len(text_price)):
            price = ''
            for j in text_price[i].text:
                if j.isdigit():
                    price += j
            new_arr_price.append(price)
        sum_price = 0
        for f in range(len(new_arr_price)):
            sum_price += int(new_arr_price[f])
        return sum_price

    def textProductPrice(self):
        self.wait.until(EC.presence_of_element_located(self.price_product))
        text_price = self.driver.find_elements(*self.price_product)
        new_arr_price = []
        for i in range(len(text_price)):
            price = ''
            for j in text_price[i].text:
                if j.isdigit():
                    price += j
            new_arr_price.append(price)
        return new_arr_price
