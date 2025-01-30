from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from tabulate import tabulate
import time
import random
import pickle
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

def type_with_delay(element, text, min_delay=0.1, max_delay=0.5):
    """Types text into an element with a random delay between characters."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

def setup_driver():
    """Initializes the Chrome WebDriver."""
    return webdriver.Chrome()

def load_cookies(driver):
    """Loads LinkedIn cookies if available to skip login."""
    if os.path.exists("cookies.pkl"):
        driver.get("https://www.linkedin.com/login")
        with open("cookies.pkl", "rb") as cookiesfile:
            cookies = pickle.load(cookiesfile)
            driver.get("https://www.linkedin.com/")
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
        driver.get("https://www.linkedin.com/feed")
        return True
    return False

def login(driver):
    """Performs LinkedIn login if cookies are not available."""
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    email_element = driver.find_element(By.ID, "username")
    password_element = driver.find_element(By.ID, "password")
    type_with_delay(email_element, EMAIL)
    type_with_delay(password_element, PASSWORD)
    sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    time.sleep(random.uniform(1, 3))
    sign_in_button.click()

def save_cookies(driver):
    """Saves LinkedIn session cookies for future logins."""
    try:
        with open("cookies.pkl", "wb") as cookiesfile:
            pickle.dump(driver.get_cookies(), cookiesfile)
        print("Cookies saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving cookies: {e}")


def perform_search(driver, term):
    """Searches for a term on LinkedIn and applies the 'People' filter."""

    # Get the search bar value without clicking on it
    search_value = driver.execute_script("return document.querySelector('.search-global-typeahead__input').value;")

    if not search_value.strip():  # If search bar is empty, click the search icon and type the term
        search_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-global-typeahead__collapsed-search-button"))
        )
        search_icon.click()

        search_bar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-global-typeahead__input"))
        )
        print("Search located")
        driver.execute_script("arguments[0].scrollIntoView(true);", search_bar)

        print("Search bar is empty, retyping search query.")
        type_with_delay(search_bar, term)
        time.sleep(random.uniform(1, 2))
        search_bar.send_keys(Keys.RETURN)
        print("Typed search term and submitted.")
        time.sleep(random.uniform(3, 6))

        people_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "li.search-reusables__primary-filter:nth-child(4) > button:nth-child(1)"))
        )
        people_filter.click()
        time.sleep(random.uniform(3, 6))
        print("Clicked on people filter")
    else:
        print("Search bar already contains search term, skipping retyping.")



def get_profile_links(driver):
    """Extracts profile links from the search results page."""
    driver.execute_script("window.scrollTo(0, 0);")
    print("Scrolled to top")

    profile_links = []
    profiles = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')]")
    print("Searching profiles")

    for profile in profiles:
        profile_url = profile.get_attribute("href")
        if profile_url and profile_url not in profile_links:
            profile_links.append(profile_url)

    return profile_links

def process_profiles(driver, profile_links):
    """Opens each profile in a new tab, processes it, then closes it."""
    for link in profile_links:
        time.sleep(random.uniform(2, 3))
        driver.execute_script(f"window.open('{link}');")
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(random.uniform(3, 6))

        # --- Extract profile data here (To be implemented) ---

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    print(f"Found & Processed {len(profile_links)} profiles")
    table = [[i + 1, link] for i, link in enumerate(profile_links)]
    print(tabulate(table, headers=["No.", "Profile URL"], tablefmt="pretty"))
    print("Links found")

def check_if_logged_out(driver, count):
    """Checks if the user has been logged out of LinkedIn."""
    try:
        driver.find_element(By.ID, "username")
        print("Logged out, ending session...")
        driver.quit()
        exit()
    except:
        print("Session is still active")
        count += 1

    return count

def main():
    """Main execution loop for the bot."""
    count = 0
    driver = setup_driver()

    if not load_cookies(driver):
        login(driver)
        save_cookies(driver)

    while True:
        perform_search(driver, "cyber security")
        profile_links = get_profile_links(driver)
        # process_profiles(driver, profile_links)
        time.sleep(random.uniform(5, 10))
        driver.refresh()

        # Call check_if_logged_out and assign the updated count back to count
        count = check_if_logged_out(driver, count)
        print(f"Run Count: {count}")

        # Check if the count reached 3 to stop
        if count == 2:
            print("Run 3 times, ending process")
            print(f"Found & Processed {len(profile_links)} profiles")
            driver.quit()
            break  # To exit the loop after 3 runs





if __name__ == "__main__":
    main()
