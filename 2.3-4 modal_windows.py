from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()

    alert = browser.switch_to.alert # переключить внимание браузера на алерт
    alert.accept()  # принять алерт

    # alert_text = alert.text   забрать текст из алерта

    # confirm.dismiss()     не согласиться с алертом

    # prompt = browser.switch_to.alert конструкия для ввода текста в алерт с текстовым полем
    # prompt.send_keys("My answer")
    # prompt.accept()

    chislo = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    x = calc(chislo)
    browser.find_element(By.CSS_SELECTOR, '.form-control#answer').send_keys(x)

    browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()

    # конструкция с библиотекой pyperclip собирает текст из модального окна и загоняет в буфер обмена
    alert2 = browser.switch_to.alert
    text = alert.text
    addToClipBoard = text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(5)

    browser.quit()


