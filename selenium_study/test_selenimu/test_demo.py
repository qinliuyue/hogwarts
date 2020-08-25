#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from optparse import Option

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class TestDemo0():
    def setup_method(self,method):
        option = Options()
        option.debugger_address ='127.0.0.1:9222'
        self.driver = webdriver.Firefox(options = option)
        #隐式等待, 最好在实例化完driver马上去设置
        self.driver.implicitly_wait(5)

    #def teardown_method(self,method):
        #self.driver.quit()
    def test_demo0(self):
        #self.driver.get("https://ceshiren.com/")#打开这个网址
        self.driver.set_window_size(1536,960)#设置屏幕
        self.driver.find_element(By.LINK_TEXT,"所有分类").click()#找到所有分类, 进行点击
        categoryele = self.driver.find_element(By.LINK_TEXT,"所有分类").click()#找到所有分类, 进行点击
        #assert 'active' == categoryele.get_attribute ("class")