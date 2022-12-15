from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



link = 'https://suninjuly.github.io/selects1.html'


def summochka(a, b):
    return int(a) + int(b)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, 'num1')
    a = input1.text

    input2 = browser.find_element(By.ID, 'num2')
    b = input2.text

    input3 = summochka(a, b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(input3))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)

    browser.quit()
