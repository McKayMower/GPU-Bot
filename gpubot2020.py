# this file is a bot that buys a gpu
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time
import bs4

# actual gpu
url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442 '

# tests below
# url = 'https://www.bestbuy.com/site/sandisk-ultra-dual-drive-luxe-128gb-usb-3-1-usb-type-c-flash-drive/6422271.p?skuId=6422271'
# add to cart test
# url = 'https://www.bestbuy.com/site/amd-ryzen-7-3700x-3rd-generation-8-core-16-thread-3-6-ghz-4-4-ghz-max-boost-socket-am4-unlocked-desktop-processor/6356277.p?skuId=6356277'
# url = 'https://www.bestbuy.com/site/corsair-vengeance-rgb-pro-32gb-2pk-16gb-3-2ghz-pc4-25600-ddr4-dimm-unbuffered-non-ecc-desktop-memory-kit-with-rgb-lighting-black/6333800.p?skuId=6333800'
# sold out test
# url = 'https://www.bestbuy.com/site/msi-aegis-rs-gaming-desktop-intel-core-i7-10700kf-16gb-memory-nvidia-geforce-rtx-3080-1tb-ssd-black-black/6439310.p?skuId=6439310'


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
        # gather html from page
        markup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        try:
            # try to get either a sold out or atc button
            add_to_cart = markup.find('button', {'class': 'btn btn-primary btn-lg btn-block btn-leading-ficon '
                                                          'add-to-cart-button'})
            sold_out = markup.find('button', {'class': 'btn btn-disabled btn-lg btn-block add-to-cart-button'})

            # check which button it is
            if add_to_cart:
                print(f'found button:', add_to_cart.get_text())
                add_cart(driver)
            elif sold_out:
                print(f'found button:', sold_out.get_text())
                print('sold out, refreshing')
                time.sleep(4)
                driver.refresh()
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            time.sleep(4)
            driver.refresh()



def add_cart(driver):
    # get atc button name from css
    atc_button = '.add-to-cart-button'
    # try to click button
    while True:
        try:
            driver.find_element_by_css_selector(atc_button).click()
            print('clicked button, check cart')
            break
        finally:
            driver.implicitly_wait(1)

    # once add to cart button is clicked, navigate to cart
    driver.get('https://www.bestbuy.com/cart')
    initiate_checkout(driver)


def initiate_checkout(driver):
    time.sleep(1)
    # get checkout button name from css
    checkout_button = '.btn-primary'
    while True:
        try:
            driver.find_element_by_css_selector(checkout_button).click()
            print('clicked to initiate checkout')
            break
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            pass
    # once checkout is initiated, last thing we need to enter is the cvv code of the card
    enter_cvv(driver)


def enter_cvv(driver):
    time.sleep(1)
    # try to switch to shipping from in store pick up
    print('switching to shipping method instead of ispu')
    try:
        driver.find_element_by_class_name('ispu-card__switch').click()
    except (NoSuchElementException, TimeoutException):
        pass

    while True:
        try:
            cvv = driver.find_element_by_id('credit-card-cvv')
            print('found cvv input, going to send input')
            cvv.send_keys('600')
            time.sleep(1)
            print('typed cvv, placing order')
            break
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            print('transaction could not be made')

    # once cvv is in, just need to confirm order
    place_order(driver)


def place_order(driver):
    time.sleep(1)
    print('Trying to place order')
    while True:
        try:
            # click the place order button
            driver.find_element_by_css_selector('.btn-primary').click()
            break
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            pass

    print('order placed!')

if __name__ == '__main__':
    driver = make_driver()
    find_card(driver)
