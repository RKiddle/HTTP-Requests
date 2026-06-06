import urllib.robotparser

# 1. Set up the parser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.google.com/robots.txt")
rp.read()

# 2. Check if you (an unnamed bot, "*") are allowed to fetch a specific URL
url_to_check = "https://www.google.com/search"
user_agent = "*" 

can_fetch = rp.can_fetch(user_agent, url_to_check)

if can_fetch:
    print(f"Yes, you are allowed to scrape {url_to_check}")
else:
    print(f"No, scraping {url_to_check} is disallowed by robots.txt")
