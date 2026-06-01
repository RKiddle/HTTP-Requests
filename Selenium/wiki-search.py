from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# STEP 1: Launch the Robot Browser
print("Starting the browser...")
driver = webdriver.Chrome() 

# STEP 2: Navigate to a website
print("Going to Wikipedia...")
driver.get("https://www.wikipedia.org/")

# STEP 3: Find the search bar and type into it
# We tell Selenium to look for an element on the page named "search"
search_bar = driver.find_element(By.NAME, "search")

print("Typing in the search bar...")
# This actually simulates pressing keys on a keyboard
search_bar.send_keys("Methane")

# Simulate pressing the "Enter" key
search_bar.send_keys(Keys.RETURN)

# Give the page a couple of seconds to load
time.sleep(2) 

# STEP 4: Scrape the data we want
# We tell Selenium to find the main heading of the new page
heading = driver.find_element(By.ID, "firstHeading")

# Find the first paragraph (usually standard text in a <p> tag)
# XPATH is a way to find elements by their HTML structure
first_paragraph = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')

print("\n--- SUCCESS! HERE IS THE DATA ---")
print(f"Page Title: {heading.text}")
print(f"Summary: {first_paragraph.text}")
print("---------------------------------\n")

# STEP 5: Clean up and close the browser
print("Closing the browser in 3 seconds...")
time.sleep(3)
driver.quit()
