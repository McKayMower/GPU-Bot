# McKay Mower, mmower777@gmail.com
# 12/18/2020
# This python script represents a bot that can buy the product given a certain url from newegg

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time
import bs4
import os

# kills all current instances of chrome before launching a new webdriver (in case someone forgets to close chrome before starting bot)
browserExe = "chrome.exe"
os.system("taskkill /f /im "+browserExe)

# 3070 combo url
# url = 'https://www.newegg.com/p/pl?d=3070%20combo&cm_mmc=snc-twitter-_-pm-restock-_-3070combos-_-na'

# 3070 plain url
# url = 'https://www.newegg.com/p/pl?d=3070&LeftPriceRange=450+600&N=100007709&isdeptsrh=1'

# newegg test url has multiple add to cart buttons and multiple sold out items
url = 'https://www.newegg.com/p/pl?d=3070'


# creates a web driver with my personal google chrome options and returns it
def make_driver():
    # open a new instance of chrome
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=C:\\Users\\mmowe\\AppData\\Local\\Google\\Chrome\\User Data')
    # might be able to use this: options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome('C:\\Users\\mmowe\\PycharmProjects\\chromedriver.exe', options=options)
    return driver

# generates a list of every item that can be added to cart
def generate_list(driver):
    driver.get(url)
    markup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    # find which items can/cannot be added to cart
    all_items = markup.find_all('a', {'class': 'item-branding'})
    add_to_cart = markup.find_all('button', {'class': 'btn btn-primary btn-mini'})
    sold_out = markup.find_all('p', {'class': 'item-promo'})
    for item in all_items:
        print(f'item: ', {item.text})
    for atc in add_to_cart:
        print(f'add to cart: ', {atc.text})
    for so in sold_out:
        print(f'sold out: ', {so.text})



if __name__ == '__main__':
    driver = make_driver()
    generate_list(driver)

