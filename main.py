from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)



email_element = driver.find_element(By.ID, "username")

password_element = driver.find_element(By.ID, "password")

email_element.send_keys("ethan.adg@proton.me")
password_element.send_keys("E>ADEGBEYENI")

sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_button.click()

try:
    #attempt to view profile picture
    profile_pix = driver.find_element(By.CLASS_NAME, "profile-card-profile-picture-container")
    print("Succesful login ")
except:
    # If profile picture is not found, print an error message
    print("unsuccesful login attempt")