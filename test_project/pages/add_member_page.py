#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self):
        self.driver = webdriver.Chrome()
        self.driver.find_element(By.ID,"username").send_keys("皮城女警")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("3333")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13633322222")
        #return self是为了实现返回当前页面时依然可以实现链式调用
        #相当于别人调用是 add_member().save_member()就等同时self.save_member(self

        return self

    def save_member(self):
        self.driver.find_element(By.CSS_SELECTOR,"javascript").click()
        return ContactPage(self.driver)


    def cancel_memner(self):
        pass