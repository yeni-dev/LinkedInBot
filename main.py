from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import time
import random
import pickle
import os
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

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

    type_with_delay(email_element, EMAIL)
    type_with_delay(password_element, PASSWORD)

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

except TimeoutException:
    print("Timed out while waiting for element.")
except Exception as e:
    print(f"An error occurred: {e}")

except:
    # If profile picture is not found, print an error message
    print("unsuccesful login attempt")


while True:
    #connection autmation here
    # Wait for the search icon to be clickable and click it to open the search panel
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "search-global-typeahead__collapsed-search-button"))
    )
    search_icon.click()  # Click the search icon to open the search panel


    search_bar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-global-typeahead__input"))
    )
    print("Search located")

    # Ensure the search bar is in view and focused
    driver.execute_script("arguments[0].scrollIntoView(true);", search_bar)  # Scroll to the search bar if needed
    search_bar.click()
    print("Scrolled to search bar")

    # Add a slight delay to ensure the element is ready for interaction
    time.sleep(random.uniform(1, 2))


    type_with_delay(search_bar, "cybersecurity")  # replace with user input later
    time.sleep(random.uniform(1, 2))  # random delay
    search_bar.send_keys(Keys.RETURN)  # press enter
    print("typed in and landed on search page")


    time.sleep(random.uniform(3, 6))  # time to allow page to load

    # find and click the 'people' filter button

    people_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div[2]/section/div/nav/div/ul/li[2]/button"))
    )

    people_filter.click()
    time.sleep(random.uniform(3, 6))  # wait for filter to apply
    print("Clicked on people filter")

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(4, 7))  # random delay to reduce bit time

    profile_links = []

    # find all profile links on page
    profiles = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')")

    for profile in profiles:
        profile_url = profile.get_attribute("href")
        if profile_url and profile_url not in profile_links:
            profile_links.append(profile_url)
    print(f"Found {len(profile_links)} profiles")
    print("links found")
    #add random delays between actions
    time.sleep(random.uniform(5,10))
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

