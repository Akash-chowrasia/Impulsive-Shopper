from .listParser import *

def click_buy_moisturizers_button(browser):
    browser.find_element_by_xpath("//button[text() = 'Buy moisturizers']").click()

def parse_aloe(browser):
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Aloe')]/following-sibling::p")
    return list_finder(list_elements)

def parse_almond(browser):
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Almond')]/following-sibling::p")
    return list_finder(list_elements)

def add_aloe(browser):
    price_list = parse_aloe(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Aloe')]/following-sibling::p[contains(text(),minimum_price)]/following-sibling::button[text() = 'Add']").click()

def add_almond(browser):
    price_list = parse_almond(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Almond')]/following-sibling::p[contains(text(),minimum_price)]/following-sibling::button[text() = 'Add']").click()
