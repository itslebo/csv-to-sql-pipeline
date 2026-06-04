import requests
from urllib.parse import urljoin
import urllib.robotparser

# Getting the first page:
# def response_code(response):
#     if response.status_code == 200:
#         print ("Page fetched successfully.")
#     else:
#         print ("Failed to fetch the page. Status code:", response.status_code)

# URL = "https://books.toscrape.com/"
# url_response = requests.get(URL)
# response_code(url_response)


# Checking the robots.txt file:
# def check_robots_txt(url):
#     robots_url = urljoin(url, "robots.txt")
#     response = requests.get(robots_url)
#     print(response.text)

# check_robots_txt('https://amazon.com/')

# Looking for delay:
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url('https://amazon.com/')
# rp.read()
# delay = rp.crawl_delay('*')
# print(f"Crawl delay for Amazon: {delay} seconds")

# Checking if scraping is allowed:
rp = urllib.robotparser.RobotFileParser() # Create a RobotFileParser object
rp.set_url('https://bash.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://bash.com/'))  # Check if scraping the homepage is allowed