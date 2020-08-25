#/usr/bin/env phthon
# -*- coding:utf-8 _*_
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


class TestDemo0():
    def setup_method(self,method):
        option = Options()
       # option.debugger_address = '127.0.0.1:9222'
        #self.driver = webdriver.Chrome(options = option)
        self.driver = webdriver.Chrome()
        #隐式等待, 最好在实例化完driver马上去设置
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

    def test_cookie(self):
        #get_cookies()获取当前页面的cookies
        #cookies = self.driver.get_cookies()
        #print(cookies)
        #打开index 页面,这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 带有登录信息的cookie
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
     'value': 'ofFqWHL6oDHTI1Bd7aTVcIWDYZ5aQlyFnUKqJuHS1bCVpijTpvyHutLycjk1j9XRcoUtrjH6inMFLjkm_HCwBROtL8MaZMK2By2r8l8ZGi-AVaPIycP88kFvjGfBbFfbtN7yYA7RYzepK8eoumZHjy7MCdCxgZdYbgn76s-6VAY7gVvsLccXb9F_uoP1dBACD_y-RzZUQTUO6n2sK_A_zCpozHXzd_Keczr6eg9SKh5ov_JGKgN293AFpaU7slv16-sSUmff1OJ3z64xq1N7mA'}, {
        'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        'value': '1688850443732244'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid',
                                       'path': '/', 'secure': False, 'value': '1970324977151703'}, {
        'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                        'secure': False, 'value': 'swNQ3toZwoEOU63e8TJ-Vf71UPhlZC3UHFz3bFU-MGud3EP001WGbBz7oCltYeYn'}, {
        'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        'value': 'a9275695'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                               'secure': False, 'value': '13788138123311314'}, {'domain': '.work.weixin.qq.com',
                                                                                'httpOnly': True, 'name': 'wwrtx.ref',
                                                                                'path': '/', 'secure': False,
                                                                                'value': 'direct'}, {
        'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False,
        'value': '2069008384'}, {'domain': '.qq.com', 'expiry': 1598320571, 'httpOnly': False, 'name': '_gat',
                                 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com',
                                                                               'expiry': 1598349849, 'httpOnly': True,
                                                                               'name': 'ww_rtkey', 'path': '/',
                                                                               'secure': False, 'value': '67n7nng'}, {
        'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        'value': '1688850443732244'}, {'domain': '.work.weixin.qq.com', 'expiry': 1628949814, 'httpOnly': False,
                                       'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {
        'domain': '.qq.com', 'expiry': 1598406925, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        'value': 'GA1.2.183224924.1598286226'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600912528,
                                                 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/',
                                                 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com',
                                                                                      'expiry': 1661392525,
                                                                                      'httpOnly': False, 'name': '_ga',
                                                                                      'path': '/', 'secure': False,
                                                                                      'value': 'GA1.2.1460542916.1598286226'}, {
        'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False,
        'value': '2627156268'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie((cookie))
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_importcontact (self):
       # def test_cookie(self):
            # get_cookies()获取当前页面的cookies
            # cookies = self.driver.get_cookies()
            # print(cookies)
            # 打开index 页面,这时候需要登录
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 带有登录信息的cookie
            cookies = [
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                 'value': 'ofFqWHL6oDHTI1Bd7aTVcIWDYZ5aQlyFnUKqJuHS1bCVpijTpvyHutLycjk1j9XRcoUtrjH6inMFLjkm_HCwBROtL8MaZMK2By2r8l8ZGi-AVaPIycP88kFvjGfBbFfbtN7yYA7RYzepK8eoumZHjy7MCdCxgZdYbgn76s-6VAY7gVvsLccXb9F_uoP1dBACD_y-RzZUQTUO6n2sK_A_zCpozHXzd_Keczr6eg9SKh5ov_JGKgN293AFpaU7slv16-sSUmff1OJ3z64xq1N7mA'},
                {
                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                    'secure': False,
                    'value': '1688850443732244'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid',
                 'path': '/', 'secure': False, 'value': '1970324977151703'}, {
                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                    'secure': False,
                    'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                                    'secure': False,
                                    'value': 'swNQ3toZwoEOU63e8TJ-Vf71UPhlZC3UHFz3bFU-MGud3EP001WGbBz7oCltYeYn'}, {
                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                    'secure': False,
                    'value': 'a9275695'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                 'secure': False, 'value': '13788138123311314'}, {'domain': '.work.weixin.qq.com',
                                                                  'httpOnly': True, 'name': 'wwrtx.ref',
                                                                  'path': '/', 'secure': False,
                                                                  'value': 'direct'}, {
                    'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                    'secure': False,
                    'value': '2069008384'},
                {'domain': '.qq.com', 'expiry': 1598320571, 'httpOnly': False, 'name': '_gat',
                 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com',
                                                               'expiry': 1598349849, 'httpOnly': True,
                                                               'name': 'ww_rtkey', 'path': '/',
                                                               'secure': False, 'value': '67n7nng'}, {
                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                    'secure': False,
                    'value': '1688850443732244'},
                {'domain': '.work.weixin.qq.com', 'expiry': 1628949814, 'httpOnly': False,
                 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {
                    'domain': '.qq.com', 'expiry': 1598406925, 'httpOnly': False, 'name': '_gid', 'path': '/',
                    'secure': False,
                    'value': 'GA1.2.183224924.1598286226'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600912528,
                                                             'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/',
                                                             'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com',
                                                                                                  'expiry': 1661392525,
                                                                                                  'httpOnly': False,
                                                                                                  'name': '_ga',
                                                                                                  'path': '/',
                                                                                                  'secure': False,
                                                                                                  'value': 'GA1.2.1460542916.1598286226'},
                {
                    'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                    'secure': False,
                    'value': '2627156268'}]
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie((cookie))
                #重新打开已带有的cookie信息的index页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
            self.driver.find_element(By.ID,"js_upload_file_input").send_keys("E:\one\mydata.xls")
            assert "mydata.xls" == self.driver.find_element(By.ID,"upload_file_name").text