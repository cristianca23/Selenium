import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.system('cls')
driver = webdriver.Chrome() 


Webpage = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(Webpage) #accedo a la pagina
driver.implicitly_wait(5)
try:
    thanks_button = driver.find_element_by_class_name('at-cm-no-button') #quito la publicidad
    thanks_button.click()
except:
    print('No se encontro elemento con esta clase')
sum1 = driver.find_element_by_id('sum1') # obtengo los campos input para la suma
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5 ) #ingreso numeros a los campos input
sum2.send_keys(10)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]') # selecciono el boton con un selector css [attribute^=value]	a[href^="https"]	Concepto: Selects every <a> element whose href attribute value begins with "https"
btn.click() 