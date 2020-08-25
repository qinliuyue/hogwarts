#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class BasePage:

    def __init__(self,driver_base = None):
        #避免driver的重复实例化
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options = option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = driver_base