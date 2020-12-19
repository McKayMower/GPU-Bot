# this file is a bot that buys a gpu
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import bs4

# actual gpu
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'

# add to cart test
# url = 'https://www.bestbuy.com/site/amd-ryzen-7-3700x-3rd-generation-8-core-16-thread-3-6-ghz-4-4-ghz-max-boost-socket-am4-unlocked-desktop-processor/6356277.p?skuId=6356277'
# sold out test
url = 'https://www.bestbuy.com/site/msi-aegis-rs-gaming-desktop-intel-core-i7-10700kf-16gb-memory-nvidia-geforce-rtx-3080-1tb-ssd-black-black/6439310.p?skuId=6439310'

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
        markup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        # print(markup)
        # driver.close()
        try:
            add_to_cart = markup.find('button', {'class': 'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button'})
            sold_out = markup.find('button', {'class': 'btn btn-disabled btn-lg btn-block add-to-cart-button'})
            if add_to_cart:
                print(f'found button:', add_to_cart.get_text())
            elif sold_out:
                print(f'found button:', sold_out.get_text())
                time.sleep(5)
                driver.refresh()

        # if no card was found, wait 5 seconds, refresh page, try again.
        finally:
            time.sleep(5)
            driver.refresh()



if __name__ == '__main__':
    driver = make_driver()
    find_card(driver)
