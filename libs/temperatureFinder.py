def temperatureFinder(browser):
    temperature = browser.find_element_by_id("temperature")
    return int(temperature.text[:-2])
