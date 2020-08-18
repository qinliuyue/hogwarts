#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium import webdriver
class Base():
    def setup(self):
        self.driver = webdriver.Chrome()  # 定义一个driver
        self.driver.implicitly_wait(5)  # (隐形等待5秒)
        self.driver.maximize_window()  # 窗口最大化

    def teardown(self):
        self.driver.quit()