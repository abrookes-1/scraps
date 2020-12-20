import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

good_color = 'black'
URL = 'https://www.freitag.ch/en/f41'

# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

driver = webdriver.Chrome('/Users/aidanbrookes/Downloads/chromedriver', )
driver.get(URL)
driver.find_element_by_id('dismiss-cookies-cta').click()
time.sleep(0.5)
driver.find_element_by_id('products-load-all').click()
time.sleep(0.5)

browse = driver.find_element_by_id('products-selector')
items = browse.find_elements_by_tag_name('li')

for item in items:
    color = item.get_attribute('data-dimension17')
    if good_color in color:
        url = item.find_element_by_tag_name('a').get_attribute('href')
        driver.get(url)
        driver.find_element_by_id('product-addtocart').click()
        # driver.execute_script(f"window.open('{url}');")
        break

time.sleep(0.5)
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# print(drivera.find_element_by_tag_name('body'))
# print(len(items))

