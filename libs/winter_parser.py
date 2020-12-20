'''
    This Module Ferforms all the operations related to
    winter shoping.
    Pylint Testing Rate for this file = 7.6/10.
'''
from .list_parser import list_finder

def click_buy_moisturizers_button(browser):
    '''
        This function clicks over the "Buy moisturizers" Button
        By scraping the page.
    '''
    browser.find_element_by_xpath("//button[text() = 'Buy moisturizers']").click()

def parse_aloe(browser):
    '''
        This function finds all the aloe items on the page
        and returns the cost of all items in a list.
    '''
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Aloe')]\
        /following-sibling::p")
    return list_finder(list_elements)

def parse_almond(browser):
    '''
        This function finds all the almond items on the page
        and returns the cost of all items in a list.
    '''
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Almond')]\
        /following-sibling::p")
    return list_finder(list_elements)

def add_aloe(browser):
    '''
        This function will add the minimum cost aloe item
        into the cart.
    '''
    price_list = parse_aloe(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Aloe')]/\
        following-sibling::p[contains(text(),%s)]/\
            following-sibling::button[text() = 'Add']"%minimum_price).click()

def add_almond(browser):
    '''
        This function will add the minimum cost almond item
        into the cart.
    '''
    price_list = parse_almond(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Almond')]/\
        following-sibling::p[contains(text(),%s)]/\
            following-sibling::button[text() = 'Add']"%minimum_price).click()
