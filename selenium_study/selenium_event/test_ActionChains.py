# /usr/bin/env phthon
# -*- coding:utf-8 _*_
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()  # 创建一个driver,实例化了一个Chrome driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()#窗口最大化

    def teardow(self):
        self.driver.quit()  # 配置quit方法
    @pytest.mark.skip#加个装饰器不执行这个用例,只执行moveto
    def test_case_click(self):  # 定义一个test_case,模拟click操作
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elemenet_click = self.driver.find_element_by_xpath("//input[@value='click me']")  # 查找点击元素
        elemenet_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")  # 查找双击元素
        elemenet_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")  # 查找右击元素
        action = ActionChains(self.driver)  # 定义一个ActionChains,导入一个包,往里面传处一个driver
        action.click(elemenet_click)  # 添加第一个事件
        #action.pause(1)强制等待
        action.context_click(elemenet_rightclick)  # 添加第二个事件
        #action.pause(1)强制等待
        action.double_click(elemenet_doubleclick)  # 添加第三个事件
        sleep(3)  # 延迟3秒
        action.perform()  # 调用perporm,执行上面添加的方法
        sleep(3)  # 延迟3秒
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_elements_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele[0])
        action.perform()
        sleep(3)
