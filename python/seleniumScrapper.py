import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print('si paso')
driver.get('https://www.walmart.co.cr/')

#aqui estoy agregando la parte de que identifique como se llama la search bar, para escribir algo y darle enter. 

#Look for the class
search_box = driver.find_element(By.ID, 'downshift-0-input')
    
print('si paso')


#Write what we be searched
search_box.send_keys('leche')

#Submit the text
search_box.send_keys(Keys.RETURN)



driver.quit()



