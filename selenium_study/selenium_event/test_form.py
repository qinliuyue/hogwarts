#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium import webdriver
from time import  sleep

class TestForm():#创类一个测试类
    def setup(self):
        self.driver = webdriver.Chrome()#定义一个driver
        self.driver.implicitly_wait(5)#隐形等待5秒
        self.driver.maximize_window()#窗口最大化
    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")#进入网站
        self.driver.find_element_by_id("user_login").send_keys("123")#编写测试用例
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(5)
