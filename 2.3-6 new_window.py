from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()

    # констуркция взятия заголовка второй вкладки и переключения на неё
    new_window = browser.window_handles[1] # нумерация вкладок с 0 т.е. текущая это 0
    browser.switch_to.window(new_window)

    # current_window = browser.current_window_handle так можно взять заголовок текущей вкладки

    chislo = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    x = calc(chislo)

    browser.find_element(By.CSS_SELECTOR, '.form-control#answer').send_keys(x)

    browser.find_element(By.TAG_NAME, 'button').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipboard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipboard)

finally:
    time.sleep(5)

    browser.quit()

