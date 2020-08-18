#/usr/bin/env phthon
# -*- coding:utf-8 _*_
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