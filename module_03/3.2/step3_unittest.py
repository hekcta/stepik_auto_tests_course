from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestPage(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("example@gmail.com")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        phone.send_keys("+79999999999")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        address.send_keys("Russia, Smolensk")
        # button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        # button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

        # # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(20)
        # # закрываем браузер после всех манипуляций
        # browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("example@gmail.com")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        phone.send_keys("+79999999999")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        address.send_keys("Russia, Smolensk")
        # button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        # button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()