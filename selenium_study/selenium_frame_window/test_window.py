#/usr/bin/env phthon
# -*- coding:utf-8 _*_

from selenium_study.selenium_frame_window.base import Base
from time import sleep


class TestWindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_link_text("登录").click()#先要去识别登录
        print(self.driver.current_window_handle)

        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13800000000")
        sleep(3)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)
