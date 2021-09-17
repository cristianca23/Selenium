
# En esta sección se practica un poco lo basico de selenium tomando el website de practica de selenium y probando un boton y una barra de texto
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.system('cls')
driver = webdriver.Chrome()
website = "https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"
driver.implicitly_wait(30) 
driver.get(website)
my_element = driver.find_element_by_id('downloadButton')
my_element.click()

progress_element = driver.find_element_by_class_name('progress-label')
print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),# Element Filtration
        'Complete!'# The expected Text
    )
)

