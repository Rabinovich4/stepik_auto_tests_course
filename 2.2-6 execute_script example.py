from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser.get(link)
    znachenie = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    x = calc(znachenie)

    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(x)

    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()

    button.click()

    # скролл на 10 пикселей вниз
    # browser.execute_script("window.scrollBy(0, 100);")
    # https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView больше инфы

finally:
    time.sleep(5)

    browser.quit()
