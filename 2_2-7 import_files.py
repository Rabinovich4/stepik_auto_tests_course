from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os # имортируем модуль для работы с файлами с любой оси

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('naaaaaameeee')

    browser.find_element(By.NAME, 'lastname').send_keys('llllllaaaaaastname')

    browser.find_element(By.NAME, 'email').send_keys('dfgfdg@mailforspam.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'tetext.txt')
    # добавляем к этому пути имя файла
    # больше инфы https://docs.python.org/3/library/os.path.html

    browser.find_element(By.CSS_SELECTOR, 'input#file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)

    browser.quit()

