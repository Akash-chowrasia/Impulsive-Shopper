from selenium import webdriver
from time import sleep
import sys
sys.path.append('/libs/')
from libs.temperatureFinder import temperatureFinder
from libs.summerParser import *
from libs.winterParser import *
from libs.paymentModule import *

def summer_shopping(browser):
    click_buy_sunscreens_button(browser)
    print("Successfully moved to the sunscreen page")
    add_spf50(browser)
    print("Least Priced SPF-50 product added to the cart..")
    add_spf30(browser)
    print("Least Priced SPF-30 product added to the cart..")

def winter_shopping(browser):
    click_buy_moisturizers_button(browser)
    print("successfully moved to Moisturizers page")
    add_aloe(browser)
    print("Least priced ALOE product added to the cart..")
    add_almond(browser)
    print("Least Priced ALMOND product is added to the cart..")
    
def checkout(browser):
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

def weather_predictor(temperature):
    if temperature < 19:
        return "winter"
    elif temperature > 34:
        return "summer"

if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get("https://weathershopper.pythonanywhere.com/")
    if browser.title == "Current Temperature":
        print("Owsome: Landed over right page")
    else:
        print("Error: Landed over wrong page")
    temperature = temperatureFinder(browser)
    print("Temperature found: ", temperature)
    weather = weather_predictor(temperature)
    if weather == "summer":
        summer_shopping(browser)
        checkout(browser)
    elif weather == "winter":
        winter_shopping(browser)
        checkout(browser)
    else:
        print("Hurrah!! It's All Good, No need for shopping")
    sleep(10)
    browser.close()
