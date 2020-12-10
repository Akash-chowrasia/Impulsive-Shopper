from .listParser import *

def click_buy_sunscreens_button(browser):
    browser.find_element_by_xpath("//button[text() = 'Buy sunscreens']").click()

def parse_spf50(browser):
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-50') or contains(text(),'spf-50')]/following-sibling::p")
    return list_finder(list_elements)

def parse_spf30(browser):
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p")
    return list_finder(list_elements)

def add_spf50(browser):
    price_list = parse_spf50(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-50') or contains(text(),'spf-50')]/following-sibling::p[contains(text(),minimum_price)]/following-sibling::button[text() = 'Add']").click()

def add_spf30(browser):
    price_list = parse_spf30(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p[contains(text(),minimum_price)]/following-sibling::button[text() = 'Add']").click()
