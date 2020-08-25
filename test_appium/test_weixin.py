#/usr/bin/env phthon
# -*- coding:utf-8 _*_
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class TestWeixin:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".enterprise.attendance.controller.AttendanceActivity2"
        caps["noReset"] = "true"
        # 最重要的,和server建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()


    def test_send_message(self):
        sendtext = "test005"
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/hvn")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gfs")
        el2.send_keys("努力加油呀")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/ei_")
        el4.click()
        el4.send_keys("test006")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/ei6")
        el5.click()
        elements = self.driver.find_element_by_id("com.tencent.wework:id/ehv")
        assert sendtext == elements[-1].text

