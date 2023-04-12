from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
#new list
newVeggieList =[]
#store the table elements in a list
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieList =driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in veggieList:
    newVeggieList.append(veggie.text)

originalVeggieList = newVeggieList.copy()

#sort the list
newVeggieList.sort()
#compaire the both list

assert newVeggieList == originalVeggieList

driver.close()


