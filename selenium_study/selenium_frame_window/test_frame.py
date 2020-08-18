#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium_study.selenium_frame_window.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")#frame切换
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)