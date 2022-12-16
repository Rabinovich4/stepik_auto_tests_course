import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get('http://suninjuly.github.io/explicit_wait2.html')



    # говорим Selenium ждать 13 секунд пока не появится цена 100
    button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    browser.find_element(By.ID, 'book').click()

    text1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text

    x = calc(text1)

    browser.find_element(By.CSS_SELECTOR, '.form-control#answer').send_keys(x)

    browser.find_element(By.CSS_SELECTOR, 'button#solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipboard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipboard)


finally:
    time.sleep(5)

    browser.quit()


