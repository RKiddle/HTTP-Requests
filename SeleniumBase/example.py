from seleniumbase import SB

# Initialize SeleniumBase with UC (Undetected Chromedriver) Mode enabled
# 'test=True' suppresses some extra console output
with SB(uc=True, test=True, locale="en") as sb:
    
    # 1. Navigate to the protected page
    url = "https://example.com/protected-page"
    print(f"Navigating to {url}...")
    sb.open(url)
    
    # 2. Handle potential CAPTCHAs or Cloudflare challenge pages
    # UC mode automatically strips standard webdriver flags, passing most passive checks.
    # If presented with an active challenge (like a checkbox), SeleniumBase can attempt to solve it.
    # sb.uc_gui_click_captcha()  # Often used for Cloudflare Turnstile
    # sb.solve_captcha()         # A more generic solver method
    
    # Give the page a moment to resolve any redirects or background bot-checks
    sb.sleep(3) 
    
    # 3. Extract the data (Scraping)
    print("Extracting data...")
    
    # Example A: Get the page title
    title = sb.get_page_title()
    print(f"Page Title: {title}")
    
    # Example B: Scrape text from a specific CSS selector
    # We use a standard try-except block in case the element doesn't exist
    try:
        # Wait up to 5 seconds for the element to be visible, then get its text
        main_heading = sb.get_text("h1", timeout=5)
        print(f"Main Heading: {main_heading}")
        
        # Example C: Scrape multiple items (e.g., a list of articles or products)
        items = sb.find_elements("div.item-card > a.title")
        for item in items:
            print(f"Item found: {item.text} - Link: {item.get_attribute('href')}")
            
    except Exception as e:
        print("Could not find the requested elements. The page structure might be different.")
        
    # Optional: Save a screenshot to verify what the bot actually saw
    sb.save_screenshot_to_logs()
    print("Scraping complete. Browser closing.")
