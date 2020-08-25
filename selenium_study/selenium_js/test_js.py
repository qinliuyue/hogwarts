#/usr/bin/env phthon
# -*- coding:utf-8 _*_


from selenium_study.selenium_frame_window.base import Base
import time
import pytest
class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element=self.driver.execute_script("return document.getElementById('su')")
        time.sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_css_selector('#page a:nth-child(11)').click()
        element.click()
        time.sleep(3)
        #for code in[
         #   'return document.title','return JSON.stringify(performance.timing)'
        #]:
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))
    def test_datettime(self):
        self.driver.get("https://www.12306.cn/index/")#打开12306网站
        #找到这个元素定位到这个时间控件,返回值.并移除他的只读属性
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        time.sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")#获取到这个元素,给这个元素赋值
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))#执行打印value值
