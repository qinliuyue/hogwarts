#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep

class TestTouchAction():#1定义class
    def setup(self):#2定义一个setup#创建一个options
        option = webdriver.ChromeOptions()#option里面加入参数
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)#4创建driver对像,option添加到webdriver
        self.driver.implicitly_wait(5)#5加个隐形等待
        self.driver.maximize_window()#窗口最大化

    def teardown(self):#定义3teardown
        self.driver.quit()

    def test_touchaction_scrollbottom(self):#6定义test_touchaction
        self.driver.get("http://www.baidu.com")#7打开一个网址
        el = self.driver.find_element_by_id("kw")#8往这个元素里面输入
        el_search = self.driver.find_element_by_id("su")#10定义一个搜索元素
        el.send_keys("selenium测试")#10输入
        action = TouchActions(self.driver)#9定义TouchActions,导入包,
        action.tap(el_search)#11用tap方法连接搜索框(就是#10)
        action.perform()#12执行

        action.scroll_from_element(el,0,10000).perform()#给一个座标偏移量,水平位置不变,纵座标尽量大,设10000
        sleep(3)#延迟3秒


