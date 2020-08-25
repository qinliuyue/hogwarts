#/usr/bin/env phthon
# -*- coding:utf-8 _*_
"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入,
同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""

#class Bicycle():
    #def run(self,km):
        #print(f"用脚一共骑行了{km}km,好累好累呀")


#class EBicycle(Bicycle):
   # def __init__(self,valume):
       # self.valume = valume

    #def fill_charge(self,vol):
       # print(f"电动车已充电{vol}度")
        #print(f"电动车充完电后还有{vol+self.valume}度")

    #def run(self,km):
        #e_km = self.valume *10
        #print("电动车的最大骑行公里数",e_km)
        #if km < e_km:
           # print(f"用电一共骑行了{km}km")
        #else:
            #print(f"用电一共骑行了{e_km}km")
            #super().run(km-e_km)
            #print(f"用脚骑行了{km-e_km}km")




#ebike = EBicycle(100)
#ebike.run(10000)
#导入
from appium import webdriver
import time
#创建对象, 字典型
desired_caps={}
#传参, android设备必填
desired_caps["platformName"]='android'
desired_caps["deviceName"]='6.0'
desired_caps["appPackage"]='com.xueqiu.android'
desired_caps["appActivity"]='com.xueqiu.android.common.MainActivity'
desired_caps["NoReset"]='true'
desired_caps['dontStopAppOnReset']='true'
desired_caps['skipDeviceInitialization'] = 'true'
#创建连接, 对像传进去, 返回一个driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
#执行完返回上一个页面
driver.back()
driver.quit()
























