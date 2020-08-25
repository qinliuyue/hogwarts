#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        #解决循环导入问题
        from test_project.pages.add_member_page import AddMemberPage

        return AddMemberPage(self.driver)