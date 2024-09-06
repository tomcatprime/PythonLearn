from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser open after program finishes

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.amazon.pl/Garmin-Forerunner-Smartwatch-Biegania-Blue/dp/B0B553HT2B/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.cd8f9827-1024-4efe-a534-f5778a204d2b&dib=eyJ2IjoiMSJ9.FqjZ6hP01bWMHMeLkc9HrdIve5MbvQ8TfQ4nF_eQPo_GVQaV4x1HuIHRO7T0H8I969ZmpJTfj01ZWxDspiyESXiss4iYsAuto5FCZuGBJp-Hnh5vL9ODfBZ6wCNncAe8lw0zLq5WcGvITUSsgKEtDa9E4Kvh8KlN2lGkSaeY3UGUY2vDRaNoxLSs-OTllPAm8Vb_9BWwUl7xx-x_wvuY7A.8OWlSq4oYRpiMRUU0Ufq_2ib4nocPb9MMjo5eaxoTgA&dib_tag=se&keywords=Garmin&pd_rd_r=baeda0f3-f7b9-4549-b097-08f12ffff1a9&pd_rd_w=LE22R&pd_rd_wg=Ui4qm&pf_rd_p=cd8f9827-1024-4efe-a534-f5778a204d2b&pf_rd_r=G6GBBE2A5MGKPT37J05Y&qid=1725607483&refinements=p_89%3AGarmin&rnid=21074364031&s=electronics&sr=1-2")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
price_symbol = driver.find_element(By.CLASS_NAME, value="a-price-symbol")

print(f"The price is {price.text},{price_fraction.text} {price_symbol.text}")


search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="nav-search-submit-button")
print(button.size)


#Xpath
link = driver.find_element(By.XPATH, value='//*[@id="productDocuments_feature_div"]/div/div/div/div[1]/a')
print(link.text)
#print value of href
print(link.get_attribute("href"))

# driver.close() #Close particular tab
driver.quit() #Quit the browser