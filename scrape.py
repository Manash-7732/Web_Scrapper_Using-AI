import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser ...")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path) , options=options)

    try:
        driver.get(website)
        print("Page Loaded ...")
        html = driver.page_source
        time.sleep(10);

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser");
    body_content = soup.body
    if body_content:
        return str(body_content);
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for i in soup(["script" , "style"]):
        i.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content



def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content [i: i+ max_length] for i in range(0,len(dom_content) , max_length)
    ]

# from os import environ
# from selenium.webdriver import Remote, ChromeOptions as Options
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection

# AUTH = environ.get('AUTH', default='USER:PASS')
# TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


# def scrape(url=TARGET_URL):
#     if AUTH == 'USER:PASS':
#         raise Exception('Provide Scraping Browsers credentials in AUTH ' +
#                         'environment variable or update the script.')
#     print('Connecting to Browser...')
#     server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
#     connection = Connection(server_addr, 'goog', 'chrome')
#     driver = Remote(connection, options=Options())
#     try:
#         print(f'Connected! Navigating to {url}...')
#         driver.get(url)
#         print('Navigated! Scraping page content...')
#         data = driver.page_source
#         print(f'Scraped! Data: {data}')
#     finally:
#         driver.quit()


# if __name__ == '__main__':
#     scrape()