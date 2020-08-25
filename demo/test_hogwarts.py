#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from  selenium import webdriver#导入依赖模块
from  time import sleep

class TestHogwarts():#创建测试类
    def setup(self):
        self.driver = webdriver.Firefox()#driver初始化
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)#加个隐式等
    def teardowm(self):#资源回收
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("http://www.testerhome.com")#打开一个网址
        self.driver.find_element_by_link_text("社团").click()#找到一个元素.对他进行点击
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-23386 .title > a").click()