import allure
import pytest
from selenium.webdriver import Chrome
from pageobjects.home_page import HomePage
from pageobjects.cart_page import CartPage
from assertpy import assert_that
from time import sleep

@pytest.fixture()
@allure.title('Тестирование функциональности Корзины на сайте "Читай-город"')
def driver():
    chrome = Chrome()
    yield chrome
    chrome.quit()

# @allure.title('Тестирование бейджа на иконке Корзины:')
# def test_CatrBadge(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- прокручиваю страницу до раздела "Новинки литературы"'):
#          cart_page.scrollCatalogNovelty()
#     with allure.step('- нажимаю на наименование первой книги из данного раздела'):
#          cart_page.clickProductTitle()
#     with allure.step('- перехожу на страницу карточки товара и нажимаю на кнопку "Купить"'):
#          cart_page.clickBuy_button()
#          cart_page.textBuyButtonInCart()
#          cart_page.textCartBadge()
#          expected_buy_button_text = 'ОФОРМИТЬ ЗАКАЗ'
#          expected_cart_badge_text = '1'
#     with allure.step('- проверяю, что текст на кнопке "Купить" изменился на "Оформить заказ"'):
#          assert_that(cart_page.textBuyButtonInCart()).is_equal_to(expected_buy_button_text)
#     with allure.step('- проверяю, что на иконке Корзины появился бейдж с количеством выбранных товаров (1)'):
#          assert_that(cart_page.textCartBadge()).is_equal_to(expected_cart_badge_text)

# allure.title('Тестирование добавления товара в Корзину:')
# def test_CatrAddProduct(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- прокручиваю страницу до раздела "Новинки литературы"'):
#          cart_page.scrollCatalogNovelty()
#     with allure.step('- записываю в переменные название первой книги из данного раздела и ее цену'):
#          cart_page.AddBooks(1)
#     with allure.step('- нажимаю на кнопку "Купить" под книгой'):
#          title_1 = cart_page.textProductTitle()
#          price_1 = cart_page.textPriceProduct()
#     with allure.step('- нажимаю на иконку Корзины - перехожу в Корзину'):
#          cart_page.clickCartButtonHeader()
#          title_2 = cart_page.textProductTitle()
#          price_2 = cart_page.textPriceProduct()
#     with allure.step('- проверяю, что название и цена книги в Корзине соответствует, значению переменных'):
#          assert_that(title_1).is_equal_to(title_2)
#     with allure.step('- проверяю, что значение стороки Корзины "Итого" соответствует цене выбранной книги'):
#          assert_that(price_1).is_equal_to(price_2)
#          assert_that(price_1).is_equal_to(cart_page.textTotalValue())
# #
# @allure.title('Тестирование полной очистки Корзины:')
# def test_CartMultipleDelete(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- прокручиваю страницу до раздела "Новинки литературы"'):
#          cart_page.scrollCatalogNovelty()
#     with allure.step('- нажимаю на кнопку "Купить" у трех первых книг из данного раздела'):
#          cart_page.AddBooks(3)
#          sleep(1)
#     with allure.step('- нажимаю на иконку Корзины - перехожу в Корзину'):
#          cart_page.clickCartButtonHeader()
#          sleep(1)
#     with allure.step('- нажимаю кнопку "Очистить корзину" в верхней строке Корзины'):
#          cart_page.clickDeleteMany()
#          expected_text = 'Корзина очищена'
#     with allure.step('- проверяю, что появилась надпись "Корзина очищена"'):
#          assert_that(expected_text).is_equal_to(cart_page.textCartMultipleDelete())
#
# @allure.title('Тестирование изменения количества товаров в Корзине:')
# def test_IncreaseBooksInCart(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- прокручиваю страницу до раздела "Новинки литературы"'):
#          cart_page.scrollCatalogNovelty()
#     with allure.step('- записываю в переменную цену первой книги из данного раздела'):
#          price_1 = cart_page.FromStringToNum(cart_page.textPriceProduct())
#     with allure.step('- нажимаю на кнопку "Купить" под книгой'):
#          cart_page.AddBooks(1)
#     with allure.step('- нажимаю на иконку Корзины - перехожу в Корзину'):
#          cart_page.clickCartButtonHeader()
#          sleep(1)
#     with allure.step('- нажимаю один раз на кнопку "+" (увеличения количества товара), общее число единиц выбранного товара=2'):
#          cart_page.IncreaseBooksInCart(1)
#          sleep(1)
#          price_2 = cart_page.FromStringToNum(cart_page.textPriceProduct())
#     with allure.step('- проверяю, что осуществился пересчет суммы в корзине и итоговая сумма равна сумме книги умноженной на 2'):
#          assert_that((price_1*2)).is_equal_to(price_2)
#          assert_that(price_2).is_equal_to(cart_page.FromStringToNum(cart_page.textTotalValue()))

# @allure.title('Тестирование восстановления Корзины после удаления в ней товаров:')
# def test_CartRecovery(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#     with allure.step('- открываю главную страницу сайта "Читай-город"'):
#          home_page.open()
#     with allure.step('- прокручиваю страницу до раздела "Новинки литературы'):
#          cart_page.scrollCatalogNovelty()
#     with allure.step('- записываю в переменную наименование первых 4 книг'):
#          cart_page.AddBooks(4)
#     with allure.step('- нажимаю на кнопку "Купить" у четырех первых книг из данного раздела'):
#          cart_page.clickCartButtonHeader()
#     with allure.step('- нажимаю на иконку Корзины - перехожу в Корзину'):
#          title_1 = cart_page.textProductTitles()
#          sleep(1)
#     with allure.step('- нажимаю кнопку "Очистить корзину" в верхней строке Корзины'):
#          cart_page.clickDeleteMany()
#     with allure.step('- нажимаю кнопку "Восстановить корзину"'):
#          cart_page.clickRecoverCart()
#          title_2 = cart_page.textProductTitles()
#     with allure.step('- проверяю, что наименование восстановленных книг в Корзине, соответствует наименованию удаленных книг'):
#          assert_that(title_1).is_equal_to(title_2)
#
@allure.title('Тестирование расчёта итоговой суммы в Корзине:')
def test_CartPriceSum(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    with allure.step('- открываю главную страницу сайта "Читай-город"'):
         home_page.open()
    with allure.step('- прокручиваю страницу до раздела "Новинки литературы"'):
         cart_page.scrollCatalogNovelty()
    with allure.step('- нажимаю на кнопку "Купить" у шести первых книг из данного раздела'):
          cart_page.AddBooks(6)
    with allure.step('- нажимаю на иконку Корзины - перехожу в Корзину'):
         cart_page.clickCartButtonHeader()
    with allure.step('- нажимаю у первой книги два раза на кнопку "+" (увеличения количества товара)'):
         cart_page.IncreaseBooksInCart(2)
         sleep(1)
    with allure.step('- рассчитываю общую стоимость товаров, находящихся в Корзине, и сравниваю её со строкой Корзины "Итого"'):
         assert_that(cart_page.PriceSum()).is_equal_to(cart_page.FromStringToNum(cart_page.textTotalValue()))
#
