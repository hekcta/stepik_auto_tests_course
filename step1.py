import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(url)
WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, 'book'))).click()


x = driver.find_element(By.ID, 'input_value').text
y = calc(int(x))
driver.find_element(By.ID, 'answer').send_keys(y)
driver.find_element(By.ID, 'solve').click()
time.sleep(10)
