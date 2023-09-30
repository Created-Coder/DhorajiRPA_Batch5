# driver.get()
# driver.back()
# driver.forward()
# driver.backward()
# driver.close()
# driver.refresh()
# driver.send_keys()
# driver.click()
# driver.get_attribute()
# driver.find_element
# driver.find_elements
# driver.execute_script
# time.sleep(seconds)
# driver.implicitly_wait()
# driver.explicitly_wait()
# driver.scroll to bottm of page
# image downloading


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.nike.com/w/mens-clothing-6ymx6znik1")

# elements = WebDriverWait(driver, 1).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card__body']"))
#     )

# Image Downloading

# for element in elements:
#     src = element.find_element(By.XPATH, ".//img").get_attribute("src")
#     print(src)

#     name = element.find_element(By.XPATH, ".//a[1]").text
#     urlretrieve(src, f"{name}.png")


# Scroll to Bottom

# SCROLL_PAUSE_TIME = 0.5
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     elements = WebDriverWait(driver, 1).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//a[@data-testid='product-card__link-overlay']"))
#     )
#     print("Products Length : ", len(elements))

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height


# Scroll to ELement

# element = driver.find_element(By.XPATH, "(//div[@class='product-card__body'])[24]")

# driver.execute_script("arguments[0].scrollIntoView();", element)

# time.sleep(5)
