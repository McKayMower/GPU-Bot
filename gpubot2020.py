# this file is a bot that buys a gpu
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'


# creates a web driver with my personal google chrome options and returns it
def make_driver():
    # open a new instance of chrome
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=C:\\Users\\mmowe\\AppData\\Local\\Google\\Chrome\\User Data')

    # might be able to use this: options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome('C:\\Users\\mmowe\\PycharmProjects\\chromedriver.exe', options=options)

    return driver


# finds the gpu from the link
def find_card(driver):
    # open url in chrome
    driver.get(url)

    while True:
        html = driver.page_source
        time.sleep(1)
        print(html)



if __name__ == '__main__':
    driver = make_driver()
    find_card(driver)
