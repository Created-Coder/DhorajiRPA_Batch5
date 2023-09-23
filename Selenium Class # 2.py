from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.implicitly_wait(30)

driver.get("https://www.nike.com/w/jordan-accessories-equipment-37eefzawwpw")

# elements = driver.find_elements(By.XPATH, "//img[@class='product-card__hero-image css-1fxh5tw']")
# print(len(elements))

elements = WebDriverWait(driver, 1).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[@data-testid='product-card__link-overlay']"))
    )

prductsURLS = []

for element in elements:
    try:
        prductsURLS.append(element.get_attribute("href"))
    
    except:
        continue
    
for url in prductsURLS:
    driver.get(url)
    title = driver.find_element(By.XPATH,"//h1[@id = 'pdp_product_title']")
    price = driver.find_element(By.XPATH,'//*[@id="PDP"]/div[2]/div/div[4]/div[1]/div/div[2]/div/div/div/div/div')
    
    data = {
        "title" : title.get_attribute("innerHTML"),
        "price" : price.get_attribute("innerHTML")
    }

    print(data)


driver.close()