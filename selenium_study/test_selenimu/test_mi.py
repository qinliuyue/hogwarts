#/usr/bin/env phthon
# -*- coding:utf-8 _*_
import pytest
from appium import webdriver


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
        # 执行完回到首页
        self.driver.quit()