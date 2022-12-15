from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'
    time.sleep(11)
    # строка после None будет в сообщенни с ошибкой ТОЛЬКО если атрибута НЕТ

    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots radio: ', robots_checked)
    assert robots_checked is None

    disabled_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    disabled_button_checked = disabled_button.get_attribute('disabled')
    print('value of disabled_button_checked: ', disabled_button_checked)
    assert disabled_button_checked == 'true'

finally:
    browser.quit()

