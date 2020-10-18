# @Time : 2020/10/17 21:58 
# @Author : yangyan
# @File : test_feature_allure.py 
# @Software: PyCharm
import allure


@allure.feature("搜索模块")
class TestSearch():

    def test_search01(self):
        print("根据用户名搜索！")

    def test_search02(self):
        print("根据性别搜索！")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("搜索模块登录失败")
        pass


@allure.feature("登录模块")
class TestLogin():

    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        with allure.step("点击用户名"):
            print("第一步：点击用户名")
        with allure.step("点击密码"):
            print("第二步：点击密码")
        with allure.step("提交登录"):
            print("第二步：登录失败")
        pass

    @allure.story("登录失败")
    def test_login_fail1(self):
        assert 1 == 2

    TEST_CASE_LINK = "https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637"

    @allure.step("第一步")
    @allure.testcase(TEST_CASE_LINK, "测试用例")
    def test_login_01(self):
        assert 1 == 1

    @allure.step("第二步")
    def test_login_02(self):
        assert 1 == 1
