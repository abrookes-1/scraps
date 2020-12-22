# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import json

with open('config.json', 'r') as f:
    config = json.load(f)

URL = 'https://www.freitag.ch/en/f41'
checkoutURL = 'https://www.freitag.ch/en/checkout/'


def main():
    found = False

    driver = webdriver.Chrome(config['driver-path'], )
    driver.get(URL)
    time.sleep(0.5)
    driver.find_element_by_id('dismiss-cookies-cta').click()
    time.sleep(0.5)

    while not found:
        try:
            found = check_stock(driver)
        except:
            pass

        driver.refresh()
        if 'FREITAG' not in driver.find_element_by_tag_name('title').get_attribute('innerHTML'):
            # assume 404
            driver.execute_script(f"window.open('{config['alarm-url']}');")

        time.sleep(config['wait-seconds'])

    # after found
    wait()


def check_stock(driver):
    driver.find_element_by_id('products-load-all').click()
    time.sleep(0.1)

    browse = driver.find_element_by_id('products-selector')
    items = browse.find_elements_by_tag_name('li')

    for item in items:
        color = item.get_attribute('data-dimension17')
        if config['color'] in color:
            url = item.find_element_by_tag_name('a').get_attribute('href')
            driver.get(url)
            time.sleep(1)
            driver.find_element_by_id('product-addtocart').click()
            time.sleep(1)
            driver.execute_script(f"window.open('{config['alarm-url']}');")
            checkout(driver)
            return True

    return False


def checkout(driver):
    driver.get(checkoutURL)


def wait():
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
