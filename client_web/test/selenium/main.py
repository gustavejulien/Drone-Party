#!/usr/bin/env python3
# encoding: utf-8
from lib import utils

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

import os
import sys

class testDroneWebsite():
    def __init__(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("javascript.enabled", True)
        d = DesiredCapabilities().FIREFOX
        d["marionette"] = True
        d['loggingPrefs'] = { 'browser':'ALL' }

        options = Options()
        options.log.level = 'trace'
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Firefox(firefox_options=options, executable_path='./geckodriver', firefox_profile=fp, capabilities=d)
        self.driver.set_window_size(1920, 1080)
        self.utils = utils(self.driver)

    def tear_Down(self):
        self.driver.quit()


    def kill_processes(self):
        kill_ffox_cmd = 'pkill -f firefox'
        kill_gecko_cmd = 'pkill -f geckodriver'

        os.system(kill_ffox_cmd)
        os.system(kill_gecko_cmd)
    #################################################################################################################################

    def test(self):
        ################
        main_url = "http://localhost:3000/"
        ################

        self.driver.get(main_url)
        self.utils.waitUrl(main_url)

    def exec_x(self):
        try:
            self.test()
        except Exception as e:
            print(e)
        self.tear_Down()
        self.kill_processes()

a = testDroneWebsite()
a.exec_x()