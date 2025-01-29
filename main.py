from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import pickle
import os
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def type_with_delay(element, text, min_delay=0.1, max_delay=0.5):
    for char in text:
        element.send_keys(char) #type once character at a time
        time.sleep(random.uniform(min_delay,max_delay)) # randomly delay time between each character




driver = webdriver.Chrome()

#check if cookies file exits
if os.path.exists("cookies.pkl"):
    driver.get("https://www.linkedin.com/login") #go to login page
    with open("cookies.pkl","rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        driver.get("https://www.linkedin.com/")
        for cookie in cookies:
            driver.add_cookie(cookie) #add each cookie to browser session
        driver.refresh()
    driver.get("https://www.linkedin.com/feed")
else:
    #perform normal login
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    email_element = driver.find_element(By.ID, "username")
    password_element = driver.find_element(By.ID, "password")

    type_with_delay(email_element, "ethan.adg@proton.me")
    type_with_delay(password_element, "E>ADEGBEYENI")

    sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    time.sleep(random.uniform(1,3)) #random delay between 1 and 3 befor clicking button
    sign_in_button.click()





try:

    # Save cookies after login
    with open("cookies.pkl", "wb") as cookiesfile:
        pickle.dump(driver.get_cookies(), cookiesfile)
        print("Cookies saved successfully.")

    #attempt to view profile picture
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "profile-card-member-details"))
    )
    #profile_pix = driver.find_element(By.CLASS_NAME, "profile-card-profile-picture-container")
    print("Succesful login ")

except:
    # If profile picture is not found, print an error message
    print("unsuccesful login attempt")

while True:
    #connection autmation here
    #add random delays between actions
    time.sleep(random.uniform(19,31))
    try:
        driver.find_element(By.ID, "username")  # username is only visible on login screen
        print("Logged out, Ending session...")
        driver.quit()  # close browser
        exit()  # exit the program
        break
    except:
        print("Session is still active")

    driver.refresh()
    time.sleep(random.uniform(44,66)) #random delay befor refreshing page