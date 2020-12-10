from time import sleep

def goto_cart(browser):
    browser.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()

def click_pay_with_card(browser):
    browser.find_element_by_xpath("//button[@type = 'submit']").click()

def fill_cart(browser):
    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element_by_xpath("//input[@type = 'email']").send_keys("horasia.akashi@gmail.com")
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys('6011 1111 1111 1117')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('11 / 21')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'CVC']").send_keys('132')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'ZIP Code']").send_keys('201301')
    sleep(2)
    browser.find_element_by_xpath("//a[@class = 'Checkbox']").click()
    browser.find_element_by_xpath("//input[@autocomplete = 'mobile tel']").send_keys('9877870674')

def pay(browser):
    browser.find_element_by_xpath("//button[@type='submit' and @class='Button-animationWrapper-child--primary Button']").click()
    browser.switch_to_default_content()
    return "success" if browser.title == "Confirmation" else "failed"



