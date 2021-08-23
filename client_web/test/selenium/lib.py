from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import time
import random

class utils():

    def __init__(self, driver):
        self.driver = driver

    #################################################SEND KEYS & CLICK###############################################################

    def send_keys_by_id(self, id, value, error_msg, success_msg, fonction, ligne):
        try:
            field = self.driver.find_element_by_id(id)
            field.clear()
            field.send_keys(str(value))
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def send_keys_by_xpath(self, xpath, value, error_msg, success_msg, fonction, ligne):
        try:
            field = self.driver.find_element_by_xpath(xpath)
            field.clear()
            for i in str(value):
                field.send_keys(i)
                time.sleep(random.random())
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def send_keys_by_css(self, css, value, error_msg, success_msg, fonction, ligne):
        try:
            field = self.driver.find_element_by_css_selector(css)
            field.clear()
            field.send_keys(str(value))
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def send_keys_to_next(self, value, error_msg, success_msg, fonction, ligne):
        try:
            self.driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
            field = self.driver.switch_to_active_element()
            field.clear()
            for i in str(value):
                field.send_keys(str(i))
                time.sleep(random.random())
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def click_on_element_by_id(self, id, error_msg, success_msg, fonction, ligne):
        try:
            click_element = self.driver.find_element_by_id(id)
            click_element.click()
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def click_on_element_by_text(self, text, error_msg, success_msg, fonction, ligne):
        try:
            click_element = self.driver.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")
            click_element.click()
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def click_on_element_by_xpath(self, xpath, error_msg, success_msg, fonction, ligne):
        try:
            click_element = self.driver.find_element_by_xpath(xpath)
            click_element.click()
            print("\033[32m" + success_msg + "\033[0m")
            return 0
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 1

    def click_on_element_by_css(self, css, error_msg, success_msg, fonction, ligne):
        try:
            click_element = self.driver.find_element_by_css_selector(css)
            click_element.click()
            print("\033[32m" + success_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)

    def check_value_element_by_xpath(self, xpath, contains, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if str(contains) in element.text:
                print("\033[32m" + success_msg + "\033[0m")
                return 1
            else:
                print("\033[31m" + error_msg + "\033[0m")
                return 0
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 84

    def check_value_element_by_id(self, id, contains, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_id(id)
            if str(contains) in element.text:
                print("\033[32m" + success_msg + "\033[0m")
                return 1
            else:
                print("\033[31m" + error_msg + "\033[0m")
                print('element text = ' + element.text)
                return 0
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 84

    def waitUrl(self, url) :
        waitingTime = 0
        page_state = ''
        while page_state != 'complete' :
            page_state = self.driver.execute_script('return document.readyState;')
            time.sleep(1)
            waitingTime += 1
            if waitingTime > 3:
                print('\033[33mThis page is too long : '  + url + "\033[0m")
            if waitingTime > 7:
                print('\033[31mThis page not loading : '  + url + "\033[0m")

    def check_attribute_by_id(self, id, attribute, value, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_id(id)
            elem_att = element.get_attribute(attribute)
            if value == elem_att:
                print("\033[32m" + success_msg + "\033[0m")
            else:
                print("\033[31m" + error_msg + "\033[0m")
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 84
    def check_attribute_by_xpath(self, xpath, attribute, value, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            elem_att = element.get_attribute(attribute)
            if value == elem_att:
                print("\033[32m" + success_msg + "\033[0m")
                return 0
            else:
                print("\033[31m" + error_msg + "\033[0m")
                return 84
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 84

    def get_value_element_by_id(self, id, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_id(id)
            print("\033[32m" + success_msg + "\033[0m")
            return element.text
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 'Error'

    def get_value_element_by_xpath(self, xpath, error_msg, success_msg, fonction, ligne):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            print("\033[32m" + success_msg + "\033[0m")
            return element.text
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return 'Error'

    def tab_down(self, number_of_tab):
        try:
            self.driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
            field = self.driver.switch_to_active_element()
            for i in range(number_of_tab):
                field.send_keys(Keys.DOWN)
            print("\033[32mDown\033[0m")
        except Exception as e:
            print("\033[31mFailed to tab down\033[0m")
            print(e)

    def get_attribute_by_xpath(self, xpath, attribute, error_msg, success_msg):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            elem_att = element.get_attribute(attribute)
            return elem_att
        except Exception as e:
            print("\033[31m" + error_msg + "\033[0m")
            print(e)
            return ""
    #################################################################################################################################