'''
    This Module Ferforms all the operations related to
    summer shoping.
    Pylint Testing Rate for this file = 7.6/10.
'''
from .list_parser import list_finder # target line which descreased pylint rating.

def click_buy_sunscreens_button(browser):
    '''
        This function clicks over the "Buy snscreens" Button
        By scraping the page.
    '''
    browser.find_element_by_xpath("//button[text() = 'Buy sunscreens']").click()

def parse_spf50(browser):
    '''
        This function finds all the SPF50 items on the page
        and returns the cost of all items in a list.
    '''
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-50') or \
        contains(text(),'spf-50')]/following-sibling::p")
    return list_finder(list_elements)

def parse_spf30(browser):
    '''
        This function finds all the SPF30 items on the page
        and returns the cost of all items in a list.
    '''
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-30') or \
        contains(text(),'spf-30')]/following-sibling::p")
    return list_finder(list_elements)

def add_spf50(browser):
    '''
        This function will add the minimum cost SPF50 item
        into the cart.
    '''
    price_list = parse_spf50(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-50') or \
        contains(text(),'spf-50')]/following-sibling::p[contains(text(),%s)]/following-sibling::\
            button[text() = 'Add']"%minimum_price).click()

def add_spf30(browser):
    '''
        This function will add the minimum cost SPF30 item
        into the cart.
    '''
    price_list = parse_spf30(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/\
        following-sibling::p[contains(text(),%s)]/following-sibling::\
            button[text() = 'Add']"%minimum_price).click()
