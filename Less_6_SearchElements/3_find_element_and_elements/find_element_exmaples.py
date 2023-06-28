from Less_6_SearchElements.locators.MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/")
element = driver.find_elements(By.CSS_SELECTOR, MainPage.nav_links)
driver.quit()
