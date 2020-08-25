#/usr/bin/env phthon
# -*- coding:utf-8 _*_
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeixin:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".enterprise.attendance.controller.AttendanceActivity2"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1  #等待页面空闲的时间
       # 最重要的,和server建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        time.sleep(3)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hgs").click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()
        result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/oh").text
        assert "外出打卡成功" == result
