from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

name.send_keys("tomcat", Keys.ENTER)
last_name.send_keys("szejk", Keys.ENTER)
email.send_keys("email@example.com", Keys.ENTER)

time.sleep(5)
driver.close()

print("Done")