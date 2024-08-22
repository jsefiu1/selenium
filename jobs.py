from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "sefiujon99@gmail.com"
PASSWORD = "blerim123"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

# Wait for sign in button to be clickable
sign_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/a[1]'))
)
sign_in.click()

# Wait for email and password fields to be present
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)

email.send_keys(EMAIL)
password.send_keys(PASSWORD)

submit = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit.click()


all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in all_listings:
    print("Opening listing")
    listing.click()
    time.sleep(1)  # Added an argument for time.sleep()

    try:
        # Wait for the save button to be present
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3'))
        )        
        save_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
