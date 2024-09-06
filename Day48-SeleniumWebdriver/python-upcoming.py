from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.python.org/")


content = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in content:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_names:
    print(name.text)

event_dictionary = {}

for n in range(len(event_names)):
    event_dictionary[n] = {
        "time": content[n].text,
        "name": event_names[n].text
    }

print("########################")
print("Upcoming Python Events")
print(event_dictionary)

driver.quit()