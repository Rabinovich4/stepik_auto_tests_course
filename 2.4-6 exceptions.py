from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/cats.html'


try:
    browser = webdriver.Chrome()
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    browser.implicitly_wait(5)

    browser.get(link)

    browser.find_element(By.ID, 'button')


finally:
    browser.quit()

