#/usr/bin/env phthon
# -*- coding:utf-8 _*_
# 1、补全计算器（加法 除法）的测试用例
# 2、使用参数化完成测试用例的自动生成
# 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
# 注意：
#     使用等价类，边界值，因果图等设计测试用例
#     测试用例中添加断言，验证结果
#     灵活使用 setup(), teardown() , setup_class(), teardown_class()
import pytest

from pythoncode.calc import Calculator


class TestCalc:   #定义一个计算器的测试类

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()
    def teardown_class(self):
        print("结束计算")
    @pytest.mark.parametrize('a,b,expect',[
        (1,2,3),
        (100,100,200),
        (0.1,0.1,0.2),
        (-1,-2,-3)
    ],ids=['int','bigint','float','minus'])
    def test_add(self,a,b,expect):         #定义一个计算器的相加测试方法
        #calc = Calculator()     #实列化计算器
        result=self.calc.add(a,b)    #调用相加方法
        if isinstance(result,float):
            result = round(result,2)
        assert expect == result      #断言


    def test_div(self):
        #calc = Calculator()
        result =self.calc.div(2,1)
        assert 2 == result
