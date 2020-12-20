'''
    This is the main file of the project, This is a simple
    demostration of the complete automated shopping system.
    Pylint Testing Rate for this file = 10/10.
'''
from time import sleep
from selenium import webdriver
from libs.temperature_finder import temperature_finder
from libs.summer_parser import click_buy_sunscreens_button, add_spf50, add_spf30
from libs.winter_parser import click_buy_moisturizers_button, add_aloe, add_almond
from libs.payment_module import goto_cart, click_pay_with_card, fill_cart, pay

def summer_shopping():
    '''
        This function takes browser reference as an Argument and
        adds the cheep priced SPF-50 and SPF-30 products to cart.
    '''

    click_buy_sunscreens_button(browser)
    print("Successfully moved to the sunscreen page")
    add_spf50(browser)
    print("Least Priced SPF-50 product added to the cart..")
    add_spf30(browser)
    print("Least Priced SPF-30 product added to the cart..")

def winter_shopping():
    '''
        This function takes browser reference as an Argument and
        adds the cheep priced Aloe and Almond products to cart.
    '''

    click_buy_moisturizers_button(browser)
    print("successfully moved to Moisturizers page")
    add_aloe(browser)
    print("Least priced ALOE product added to the cart..")
    add_almond(browser)
    print("Least Priced ALMOND product is added to the cart..")

def checkout():
    '''
        This function takes browser reference as an Argument and
        performs all the operations of payment with dummy account
        details and shows a successfull message when payment done.
    '''

    goto_cart(browser)
    print("Successfully Moved to the cart")
    sleep(3)
    click_pay_with_card(browser)
    print("Pay with card clicked")
    fill_cart(browser)
    print("Payment details filled...")
    sleep(2)
    message = pay(browser)
    print("payment", message)

#Driver code
if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get("https://weathershopper.pythonanywhere.com/")
    if browser.title == "Current Temperature":
        print("Owsome: Landed over right page")
    else:
        print("Error: Landed over wrong page")
    temperature = temperature_finder(browser)
    print("Temperature found: ", temperature)
    if temperature > 34:
        summer_shopping()
        checkout()
    elif temperature < 19:
        winter_shopping()
        checkout()
    else:
        print("Hurrah!! It's All Good, No need for shopping")
    sleep(10)
    browser.close()
