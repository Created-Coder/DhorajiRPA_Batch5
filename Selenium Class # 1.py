from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Example 1
# Open URL
# driver.get("https://www.olx.com.pk/")

# time.sleep(5)

# driver.close()

# driver.refresh()

# driver.get("https://chromedriver.chromium.org/downloads")
# time.sleep(5)

# driver.back()
# time.sleep(5)

# driver.forward()
# time.sleep(5)


# Example 2
driver.get("https://m.facebook.com/r.php?next=%2Fhome.php&soft=hjk")
time.sleep(3)

fname = driver.find_element(By.XPATH, "//*[@id='firstname_input']")
fname.send_keys("salman")
time.sleep(3)

lname = driver.find_element(By.XPATH, "//*[@id='lastname_input']")
lname.send_keys("Zakir")
time.sleep(3)

btn = driver.find_element(By.XPATH, "//*[@id='mobile-reg-form']/div[9]/div[2]/button[1]")
btn.click()

