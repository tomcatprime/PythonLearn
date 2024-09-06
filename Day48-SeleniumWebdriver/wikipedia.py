from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# using xpath
articles_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
print(articles_count)



article_count_div = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count_div.text)

# interactions

# article_count_div.click()

#find element by lniktext

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

#Find the search <input> by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()


