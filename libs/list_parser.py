'''
    This Module deals with traming and extracting
    operations related to price list
    Pylint Testing Rate for this file = 10/10.
'''
def number_parser(data):
    '''
        This functions extracts number by treaming
        it fron given string.
    '''
    num = data.split("Price:")[-1]
    number = num.split("Rs.")[-1]
    return int(number)

def list_finder(list_element):
    '''
        This funtion extracts the list of prices from
        given list of webdriver elements.
    '''
    price_list = []
    for price in list_element:
        data = price.text
        price_list.append(number_parser(data))
    return price_list
