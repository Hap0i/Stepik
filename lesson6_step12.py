from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@example.com")

    # Формируем путь к файлу test.txt
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")

    # Если файла нет — создаём пустой
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass

    # Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()