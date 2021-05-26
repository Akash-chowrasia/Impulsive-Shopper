'''
    This module deals with all the operations related
    to payments for items added to the cart.
    Pylint Testing Rate for this file = 10/10.
'''
from time import sleep

def goto_cart(browser):
    '''
        This function searches the cart into the page and moves
        the curser over there to click and move to the cart.
    '''
    browser.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()

def click_pay_with_card(browser):
    '''
        This function finds the payment option into the cart
        and clicks it.
    '''
    browser.find_element_by_xpath("//button[@type = 'submit']").click()

def fill_cart(browser):
    '''
        This function fills the card details into the form.
        Make sure the e-mail ID is different for all time,
        No maters whether it is valid or invalid.
    '''
    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element_by_xpath("//input[@type = 'email']").send_keys("sample@gmail.com")
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']")\
        .send_keys('6011 1111 1111 1117')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('11 / 21')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'CVC']").send_keys('132')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'ZIP Code']").send_keys('201301')
    sleep(2)
    # browser.find_element_by_xpath("//a[@class = 'Checkbox']").click()
    # browser.find_element_by_xpath("//input[@autocomplete = 'mobile tel']").send_keys('9877870674')

def pay(browser):
    '''
        This function clicks over "submit" button to pay
        after filling the form and sends message whether payment
        goes successfull or not.
    '''
    browser.find_element_by_xpath("//button[@type='submit' and \
        @class='Button-animationWrapper-child--primary Button']").click()
    browser.switch_to_default_content()
    sleep(5)
    return "success" if browser.title == "Confirmation" else "failed"
