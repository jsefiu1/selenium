from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(articles.text) 
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Jon")
first_name.send_keys("Sefiu")
email.send_keys("sefiujon@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

# Find element by Link Text 
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click() 

# Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

