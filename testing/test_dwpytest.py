#/usr/bin/env phthon
# -*- coding:utf-8 _*_
import pytest
from appium import webdriver
import time

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
        desired_caps['avd']='A6'

        # 创建连接, 对像传进去, 返回一个driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        #执行完回到首页
        self.driver.back()
        self.driver.back()
        self.driver.quit()
    def test_search(self):
        """
        1.打开 雪球 app
        2.点击搜索框
        3.向搜索框输入"阿里巴巴"
        4.在搜索结果里面选择"阿里巴巴",然后进行点击
        5.获取这只上 阿里巴巴的股价,并判断这只股票的价格>200

        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(20)
        #不对
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId="com.xueqiu.android:id/name".index("0")').click()


        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200


       # def test_touchaction(self):
            #需要导入一个包, 要不然会标红,
            #action = TouchAction(self.driver)
            #action.press(x=428,y=2020).move_to(x=428,y=650).release().perform()

if __name__ == '__main__':
    pytest.main()

