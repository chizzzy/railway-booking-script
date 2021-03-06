from selenium import webdriver
import time


def select_train(from_city_name, to_city_name):
    search_from = browser.find_element_by_name('from-title')
    search_to = browser.find_element_by_name('to-title')
    search_from.send_keys('{}'.format(from_city_name))
    time.sleep(4)
    city_from = browser.find_element_by_xpath('//li[text()="{}"]'.format(from_city_name))
    city_from.click()
    search_to.send_keys('{}'.format(to_city_name))
    time.sleep(4)
    city_to = browser.find_element_by_xpath('//li[text()="{}"]'.format(to_city_name))
    city_to.click()
    accept_button = browser.find_element_by_xpath('//span[contains(text(), "2019")]')
    accept_button.click()
    time.sleep(4)
    print(browser.current_url)
    return browser.current_url


def book_ticket(train_url, browser):
    train = browser.find_elements_by_xpath('//input[@value="Выбрать"]')
    train[0].click()
    time.sleep(4)
    free_rooms = browser.find_elements_by_css_selector('div.place.fr[role="button"]')
    if len(free_rooms) > 8:
        length = 8
    else:
        length = len(free_rooms)
    for i in range(length):
        free_rooms[i].click()
    time.sleep(4)
    book = browser.find_element_by_css_selector('input.g-button[value="Оформить билеты"')
    book.click()
    time.sleep(4)
    inputs = browser.find_elements_by_css_selector('input[type="text"][name="lastname"]')
    for input in inputs:
        input.send_keys('Рофлан')
    inputs = browser.find_elements_by_css_selector('input[type="text"][name="firstname"]')
    for input in inputs:
        input.send_keys('Контентович')
    finish = browser.find_element_by_css_selector('input.g-button[value="В корзину"')
    finish.click()
    time.sleep(3)
    # ok_button = browser.find_element_by_css_selector('a.ok')
    # ok_button.click()
    new_window = webdriver.Chrome()
    time.sleep(4)
    new_window.get(train_url)
    time.sleep(3)
    book_ticket(train_url, new_window)


browser = webdriver.Chrome()
browser.get('https://booking.uz.gov.ua/ru/')
train_url = select_train('Киев', 'Винница')
book_ticket(train_url, browser)
