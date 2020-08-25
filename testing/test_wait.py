#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com/")
    def test_wait(self):
        self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw').send_keys("霍格沃兹测试学院")


