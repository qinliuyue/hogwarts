#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from test_project.pages.add_member_page import AddMemberPage
from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage
from selenium import webdriver

class MainPage(BasePage):
    def go_to_contact(self):
        return ContactPage(self.driver)

    def go_to_add_member(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element(By.CSS_SELECTOR,"[node-type=addmember]").click()

        return AddMemberPage(self.driver)
