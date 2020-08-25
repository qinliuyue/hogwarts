#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from test_project.pages.basepage import BasePage
from test_project.pages.main_page import MainPage


class TestAddMember(BasePage):

    def test_add_member(self):
        self.main = MainPage()
        #1.从首页跳转到添加成员页面, 2.添加成员
        self.main.go_to_add_member().add_member()
    def test_contact_member(self):
        self.main = MainPage()
        #1从首页跳转到通讯录,2.再跳转到添加成员界面,3添加成员
        self.main.go_to_contact().go_to_add_member().add_member()