from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# service_obj = Service("path to chrome driver")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, 'foo')
driver.find_element(By.XPATH, 'foo')
driver.find_element(By.CLASS, 'foo')
driver.quit()