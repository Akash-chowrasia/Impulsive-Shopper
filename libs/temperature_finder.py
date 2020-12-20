'''
    This Module deals with all the Operations
    Related to the application
    Pylint Testing Rate for this file = 10/10.
'''
def temperature_finder(browser):
    '''
        This function finds the temperature by
        scraping the page
    '''
    temperature = browser.find_element_by_id("temperature")
    return int(temperature.text[:-2])
