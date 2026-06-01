from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Start browser and search
driver = webdriver.Chrome() 
driver.get("https://www.wikipedia.org/")

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Methane")
search_bar.send_keys(Keys.RETURN)

# 2. THE FIX: Create a "Wait" object (Wait up to 10 seconds max)
wait = WebDriverWait(driver, 10)

print("Waiting for the page to load...")

# 3. Tell the Wait object exactly what to look for before proceeding
# This will pause the script until the 'firstHeading' element is physically present on the page
heading = wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))

# Now that we know the page has loaded, it's safe to grab the paragraph.
# (Note: I also upgraded the selector to a CSS selector, which is often less fragile than XPath)
first_paragraph = driver.find_element(By.CSS_SELECTOR, '#mw-content-text .mw-parser-output > p:not(.mw-empty-elt)')

print("\n--- SUCCESS! HERE IS THE DATA ---")
print(f"Page Title: {heading.text}")
print(f"Summary: {first_paragraph.text}")
print("---------------------------------\n")

driver.quit()