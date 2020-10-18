# @Time : 2020/10/17 23:50 
# @Author : yangyan
# @File : test_sevenrity.py 
# @Software: PyCharm
import allure


# 没加装饰器的不会当做任意一个级别
def test_sevenrity_11():
    assert 1 == 1


@allure.severity(allure.severity_level.NORMAL)
def test_sevenrity_out_normal():
    assert 1 == 1


@allure.severity(allure.severity_level.CRITICAL)
def test_sevenrity_critical():
    assert 1 == 1


@allure.severity(allure.severity_level.BLOCKER)
def test_sevenrity_out_blocker():
    assert 1 == 1


"""
类加装饰器，里面的method未加装饰器都默认为类加的装饰器
"""


@allure.title("霍格沃兹测试用例级别练习")
@allure.severity(allure.severity_level.NORMAL)
class TestClassWithBlocker():

    @allure.title("霍格沃兹测试用例级别normal练习")
    def test_sevenrity_inside_normal(self):
        assert 1 == 1

    @allure.title("霍格沃兹测试用例级别trivial练习")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_sevenrity_trivial(self):
        assert 1 == 1
