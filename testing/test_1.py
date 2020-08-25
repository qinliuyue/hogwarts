#/usr/bin/env phthon
# -*- coding:utf-8 _*_
import pytest
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        # 传参, android设备必填
        desired_caps["platformName"] = 'android'
        desired_caps["deviceName"] = '6.0'
        desired_caps["appPackage"] = 'com.xueqiu.android'
        desired_caps["appActivity"] = 'com.xueqiu.android.common.MainActivity'
        desired_caps["NoReset"] = 'true'
        #desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        #输入中文要输定义这个, 因为是默认英文的
        desired_caps['unicodekeyBoard'] = 'true'
        desired_caps['resetkeyBoard'] = 'true'

        # 创建连接, 对像传进去, 返回一个driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        #执行完回到首页
        self.driver.back()
        self.driver.back()
        self.driver.quit()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android: id / action_close').click()
    def test_get_current(self):
        """
        1.打开 雪球 app
        2.点击搜索框
        3.向搜索框输入"阿里巴巴"
        4.在搜索结果里面选择"阿里巴巴",然后进行点击
        5.获取这只上 阿里巴巴的股价,并判断这只股票的价格>200

        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #双重定位,先通过ID定位,再通过它的名字,两者一起
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName'and @text='阿里巴巴']").click()
        time.sleep(30)
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        time.sleep(60)
        print(f"当前09988 对应的股票价格是:{current_price}")
        assert float(current_price)>200

    def test_myinfo(self):
        """"
        1,点击我的, 进入到个人信息页面
        2,点击登录, 进入到登录页面
        3,输入用户名, 输入密码
        4.点击登录
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button")').click()


    def test_get_attr(self):
        #找到搜索框这个元素
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        #获取content-desc属性,就是name属性
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        #是否可用,
        print(search_ele.get_attribute("enabled"))
        #是否可点击
        print(search_ele.get_attribute("clickable"))
        #坐标属性
        print(search_ele.get_attribute("bounds"))

    def test_hamcrest(self):
        #注意10的前后要有空格,
        #assert_that( 10 , equal_to(10))
        #close_to的意思是10上看浮动2, 判断8是否符合
        #assert_that( 12 , close_to( 10 , 2))
        assert_that( "contains some string",contains_string("string"))

    @pytest.mark.parametrize('selfsearchkey, type, expect_price'), [
        ('alibaba','BABA',180),
        ('xiaomi','01810',10),
    ])
    def test_search(self,searchkey,type,expect_price):
        '''
        1.打开雪球应用
        2.点击搜索框
        3.输入 搜索词'alibaba' or 'xiaomi'.....
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        '''
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        price_element= self.driver.find_element(MobileBy.XPATH,f"//*[@text={type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        current_price = float(price_element.text)
        #expect_price = 280
        print(f"当前的价格{current_price}")
        assert_that(current_price,close_to(expect_price, expect_price*0.1))



if __name__ == '__main__':
    pytest.main()