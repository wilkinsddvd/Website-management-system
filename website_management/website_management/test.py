import time
import os
import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestReport

# class Router_test(unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def test_Router_1(self):
#         self.browser.get(self.live_server_url + '/')





# class SeleniumTestCase(LiveServerTestCase):
class User_All_test(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Edge()

    '''测注册时候，两个密码不一致的情况'''

    def test_User_register_1(self):
        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('123')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()
        # time.sleep(2)
        ''' 测试当确认密码不一致的时候 '''
        self.assertIn('Passwords do not match', self.browser.page_source)

    '''测试当已经注册的时候，这时候用户名相同的用户不能再注册'''


    # def tearDown_1(self):
    #     self.browser.quit()

    def test_User_register_2(self):
        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        self.assertIn('Username already taken', self.browser.page_source)

    '''测注册时候，用户名过长'''

    # def tearDown_2(self):
    #     self.browser.quit()


    def test_User_register_3(self):
        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901')
        ''' 用户名过长 101个字符'''
        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        self.assertIn('Username or password too long', self.browser.page_source)

    # def tearDown_3(self):
    #     self.browser.quit()


    '''测注册时候，密码和确认密码过长 '''

    def test_User_register_4(self):
        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()

        time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        ''' 用户名过长 101个字符'''
        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901')
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901')
        time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        self.assertIn('Username or password too long', self.browser.page_source)

    '''测试正确注册并登录'''
    #
    # def tearDown_4(self):
    #     self.browser.quit()

    def test_User_register_5_success(self):

        self.browser.get(self.live_server_url + '/')
        # time.sleep(2)

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin123')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        ''' 这里不进行对登录界面的跳转，验证注册后自动跳转登录功能 '''

        # self.browser.get(self.live_server_url + '/user/login/')

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin123')
        # time.sleep(2)

        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)

        login_button.click()

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin123', self.browser.page_source)


    # def tearDown_5(self):
    #     self.browser.quit()


    '''测试未注册用户登录，看报错信息是否正常'''

    def test_User_login_1(self):
        self.browser.get(self.live_server_url + '/')
        Login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
        )
        Login_button.click()

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin')
        # time.sleep(2)
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)

        login_button.click()
        self.assertIn('Invalid username or password, please try again', self.browser.page_source)


    ''' 测试注册之后登录，但用户名为空 '''
    # def tearDown_login_1(self):
    #     self.browser.quit()

    def test_User_login_2(self):

        self.browser.get(self.live_server_url + '/')


        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()
        # time.sleep(2)

        ''' 这里测试注册后自动跳转登录功能 '''

        self.browser.get(self.live_server_url + '/user/login/')
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        # username_input.send_keys('')
        # time.sleep(2)

        ''' 测试用户名为空 '''

        password_input = self.browser.find_element(By.NAME, 'password')
        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        password_input.send_keys('12345')
        login_button.click()
        # time.sleep(2)
        self.assertIn('请填写此字段', self.browser.page_source)

    ''' 测试注册之后登录，但密码为空 '''
    # def tearDown_login_2(self):
    #     self.browser.quit()

    def test_User_login_3(self):

        self.browser.get(self.live_server_url + '/')


        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()
        # time.sleep(2)

        ''' 这里测试注册后自动跳转登录功能 '''

        self.browser.get(self.live_server_url + '/user/login/')
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin')
        # time.sleep(2)

        ''' 测试密码为空 '''

        password_input = self.browser.find_element(By.NAME, 'password')
        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        password_input.send_keys('')
        login_button.click()
        # time.sleep(2)
        self.assertIn('请填写此字段', self.browser.page_source)

    ''' 测试注册之后登录，但账户和密码都为空 '''

    # def tearDown_login_3(self):
    #     self.browser.quit()


    def test_User_login_4(self):
        self.browser.get(self.live_server_url + '/')

        Register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        Register_button.click()
        # time.sleep(2)
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()
        # time.sleep(2)

        ''' 这里测试注册后自动跳转登录功能 '''

        self.browser.get(self.live_server_url + '/user/login/')
        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('')
        # time.sleep(2)

        ''' 测试账号和密码都为空 '''

        password_input = self.browser.find_element(By.NAME, 'password')
        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        password_input.send_keys('')
        login_button.click()
        # time.sleep(2)
        self.assertIn('请填写此字段', self.browser.page_source)

    '''测试从登录界面跳转注册界面的功能'''

    # def tearDown_login_4(self):
    #     self.browser.quit()



    def test_User_login_5_success(self):
        self.browser.get(self.live_server_url + '/')

        Login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
        )
        Login_button.click()

        register_link = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        register_link.click()

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        ''' 这里不进行对登录界面的跳转，验证注册后自动跳转登录功能 '''

        # self.browser.get(self.live_server_url + '/user/login/')

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        login_button.click()

        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)


    ''' 测试登录界面reset按钮的功能是否正常 '''

    # def tearDown_login_5(self):
    #     self.browser.quit()


    def test_User_login_6_success(self):

        self.browser.get(self.live_server_url + '/')

        Login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
        )
        Login_button.click()

        register_link = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/user/register/" and contains(@class, "button")]'))
        )
        register_link.click()

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('12345')
        # time.sleep(2)

        confirm_password_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('12345')
        # time.sleep(2)

        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        register_button.click()

        ''' 这里不进行对登录界面的跳转，验证注册后自动跳转登录功能 '''

        self.browser.get(self.live_server_url + '/user/login/')

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin')
        # time.sleep(2)

        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        ''' 测试reset按钮是否正常 '''
        reset_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="reset"]'))
        )
        reset_button.click()

        username_input.send_keys('admin')
        password_input.send_keys('12345')

        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        login_button.click()

        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_All_test("test_User_register_1"))
    suite.addTest(User_All_test("test_User_register_2"))
    suite.addTest(User_All_test("test_User_register_3"))
    suite.addTest(User_All_test("test_User_register_4"))
    suite.addTest(User_All_test("test_User_register_5_success"))
    suite.addTest(User_All_test("test_User_login_1"))
    suite.addTest(User_All_test("test_User_login_2"))
    suite.addTest(User_All_test("test_User_login_3"))
    suite.addTest(User_All_test("test_User_login_4"))
    suite.addTest(User_All_test("test_User_login_5_success"))
    suite.addTest(User_All_test("test_User_login_6_success"))

        # 指定报告生成在D盘的example_dir目录下
    import os
    filename = 'D:\\report\\result2.html'
    out = open(filename, 'wb')
    runner = HTMLTestReport.HTMLTestRunner(
        stream=out,
        title='用户测试报告',
        description='用户登录和注册功能测试报告'
    )
    runner.run(suite)
    out.close()




    # ''' 测试登录失败后返回初始主页，并从初始主页跳转到注册界面，注册后成功登录'''
    #
    # def User_login_test_6(self):
    #     self.browser.get(self.live_server_url + '/')
    #     Login_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
    #     )
    #     Login_button.click()
    #
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     # time.sleep(2)
    #     username_input.send_keys('admin')
    #     # time.sleep(2)
    #     password_input = self.browser.find_element(By.NAME, 'password')
    #     login_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #     # time.sleep(2)
    #     password_input.send_keys('12345')
    #     login_button.click()
    #     self.assertIn('Invalid username or password, please try again', self.browser.page_source)
    #
    #     return_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//a[text()="Back to Home"]'))
    #     )
    #     return_button.click()
    #
    #     # time.sleep(2)
    #     ''' 测试跳转到初始主页，再跳转到注册页面，进行注册，然后登录 '''
    #
    #     Register_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
    #     )
    #     Register_button.click()
    #     # time.sleep(2)
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     username_input.send_keys('admin')
    #     # time.sleep(2)
    #
    #     password_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'password'))
    #     )
    #     password_input.send_keys('12345')
    #     # time.sleep(2)
    #
    #     confirm_password_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'confirm_password'))
    #     )
    #     confirm_password_input.send_keys('12345')
    #     # time.sleep(2)
    #
    #     register_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #     register_button.click()
    #
    #     ''' 这里不进行对登录界面的跳转，验证注册后自动跳转登录功能 '''
    #
    #     # self.browser.get(self.live_server_url + '/user/login/')
    #
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     # time.sleep(2)
    #     username_input.send_keys('admin')
    #     # time.sleep(2)
    #
    #     password_input = self.browser.find_element(By.NAME, 'password')
    #     password_input.send_keys('')
    #
    #     ''' 测试不输密码的情况 '''
    #
    #     login_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #     # time.sleep(2)
    #     login_button.click()
    #
    #     self.assertIn('Invalid username or password, please try again', self.browser.page_source)


# class Website_test(LiveServerTestCase):


# if __name__ == '__main__':
#     my_suite = unittest.TestSuite()
#     my_suite.addTest(User_All_test('User_login_test'))
#     my_suite.addTest(User_All_test('User_register_test'))
#     filename = HTMLTestReport.HTMLTestRunner(
#
#     )

# if __name__ == '__main__':
#     # 创建测试套件
#     my_suite = unittest.TestSuite()
#     my_suite.addTest(User_All_test('User_login_test'))
#     my_suite.addTest(User_All_test('User_register_test'))
#
#     # 指定报告保存路径
#     report_dir = 'D:/report'
#     report_filename = 'result.html'
#     report_path = os.path.join(report_dir, report_filename)
#
#     # 确保报告目录存在，如果不存在则创建
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     # 使用HTMLTestRunner生成测试报告
#     with open(report_path, 'wb') as report_file:
#         runner = HTMLTestReport.HTMLTestRunner(stream=report_file,
#                                 title='用户测试报告',
#                                 description='用户登录和注册功能测试报告')
#         runner.run(my_suite)

# 复现失败
# if __name__ == '__main__':
#     # 创建测试套件
#     my_suite = unittest.TestSuite()
#     my_suite.addTest(User_test('test_login'))
#     my_suite.addTest(User_test('test_return'))
#
#     report_filename = 'D:\\report\\result.html'
#     fp = open(report_filename,'wb')
#     runner = HTMLTestReport.HTMLTestRunner(
#         stream = fp,
#         title = '测试报告',
#         description = '用例执行情况'
#     )
#     runner.run(my_suite)
#     fp.close()

#
# if __name__ == '__main__':
#     my_suite = unittest.TestSuite()
#     my_suite.addTest(User_test('test_login'))
#     my_suite.addTest(User_test('test_return'))
#
#     fp = open("./result.html",'wb')
#
#     runner = HTMLTestReport.HTMLTestRunner(
#         stream = fp,
#         title = '测试报告',
#         description = '用例执行情况'
#     )
#     runner.run(my_suite)
#     fp.close()

    # output.close()

# 执行用例cshsy01中的用例脚本，并生成HTML格式的测试报告report

# 生成测试套件
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestAdd1))

# 实例化HTMLTestReport对象



# 执行测试套件

# 判断当前脚本是否作为主程序运行

# if __name__ == '__main__':
#     # 加载测试用例类SeleniumTestCase中的所有测试方法，形成一个测试套件
#     suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumTestCase)
#
#     # 使用BeautifulReport库来运行测试套件，并生成测试报告
#     result = BeautifulReport(suite)
#
#     # 指定D 盘的路径，这里以D盘根目录下的report文件夹为例
#     # 请确保这个路径存在，否则BeautifulReport在尝试保存报告时会报错
#     log_path = 'D:/report'
#
#     # 生成测试报告，指定报告的文件名、描述和日志存放路径
#     # filename: 报告文件的名称
#     # description: 报告的描述信息
#     # log_path: 报告生成后存放的路径，这里设置为D盘的report目录
#     result.report(filename='SeleniumTestReport', description='Selenium Test Report', log_path=log_path)

# if __name__ == '__main__':
#     # 加载测试用例类SeleniumTestCase中的所有测试方法，形成一个测试套件
#     suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumTestCase)
#
#     # 使用BeautifulReport库来运行测试套件，并生成测试报告
#     result = BeautifulReport(suite)
#
#     # 获取当前文件的绝对路径，并获取其所在的目录
#     root_dir = os.path.dirname(os.path.abspath(__file__))
#
#     # 生成测试报告，指定报告的文件名、描述和日志存放路径
#     # filename: 报告文件的名称
#     # description: 报告的描述信息
#     # log_path: 报告生成后存放的路径，这里设置为当前脚本所在的目录
#     result.report(filename='SeleniumTestReport', description='Selenium Test Report', log_path=root_dir)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     ''' 验证登录功能,因为测试的数据库是没有用户的，所以需要注册一个用户，注册后登录，查看是否能正常显示用户信息'''
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/')
#         time.sleep(2)
#
#         Register_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
#             # EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         Register_button.click()
#         #
#         # self.browser.get(self.live_server_url + '/user/register/')
#         time.sleep(2)
#         username_input = WebDriverWait(self.browser, 20).until (
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         username_input.send_keys('1234')
#         time.sleep(2)
#
#         password_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'password'))
#         )
#         password_input.send_keys('1234')
#         time.sleep(2)
#
#         confirm_password_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'confirm_password'))
#         )
#         confirm_password_input.send_keys('1234')
#         time.sleep(2)
#
#         register_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         register_button.click()
#         time.sleep(2)
#
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         time.sleep(2)
#         username_input.send_keys('1234')
#         time.sleep(2)
#
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         time.sleep(2)
#         password_input.send_keys('1234')
#         # time.sleep(2)
#         login_button.click()
#
#         time.sleep(2)
#
#         self.assertIn('用户信息展示', self.browser.page_source)
#         self.assertIn('当前登录用户账号', self.browser.page_source)
#         self.assertIn('1234', self.browser.page_source)
#
#     '''验证返回按钮，是否能返回首页重新登录，以及尝试未注册用户登录，看是否能正常返回错误信息'''
#     def test_return(self):
#         self.browser.get(self.live_server_url + '/')
#         Login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
#             # EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         Login_button.click()
#
#         # 未注册用户登录
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         time.sleep(2)
#         username_input.send_keys('1234')
#         time.sleep(2)
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         time.sleep(2)
#         password_input.send_keys('1234')
#         # time.sleep(2)
#         login_button.click()
#         self.assertIn('用户名或密码错误,请重新登录', self.browser.page_source)
#
#         return_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//a[text()="Back to Home"]'))            # EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         return_button.click()
#
#         Register_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
#             # EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         Register_button.click()
#         #
#         # self.browser.get(self.live_server_url + '/user/register/')
#         time.sleep(2)
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         username_input.send_keys('1234')
#         time.sleep(2)
#
#         password_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'password'))
#         )
#         password_input.send_keys('1234')
#         time.sleep(2)
#
#         confirm_password_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'confirm_password'))
#         )
#         confirm_password_input.send_keys('1234')
#         time.sleep(2)
#
#         register_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         register_button.click()
#         time.sleep(2)
#
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         time.sleep(2)
#         username_input.send_keys('1234')
#         time.sleep(2)
#
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
#         )
#         time.sleep(2)
#         password_input.send_keys('1234')
#         # time.sleep(2)
#         login_button.click()
#
#         time.sleep(2)

    # def test






    # def test_register(self):
    #     self.browser.get(self.live_server_url + '/user/register/')
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     username_input.send_keys('1234')
    #
    #     password1_input = self.browser.find_element(By.LINK_TEXT, 'password')
    #     password1_input.send_keys('1234')
    #
    #     password2_input = self.browser.find_element(By.LINK_TEXT, 'confirm_password')
    #     password2_input.send_keys('1234')
    #
    #     register_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #
    #
    #
    #
    #     register_button.click()
    #
    #     time.sleep(2)  # Wait for the page to load
    #
    #     self.browser.get(self.live_server_url + '/user/login/')
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     username_input.send_keys('1234')
    #     time.sleep(2)
    #
    #     password_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'password'))
    #     )
    #     username_input.send_keys('1234')
    #     time.sleep(2)
    #
    #     login_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #     login_button.click()
    #     time.sleep(2)
    #      # Wait for the page to load
    #     self.assertIn('用户信息展示', self.browser.page_source)
    #     self.assertIn('当前登录用户账号', self.browser.page_source)
    #
    # def test_add_website(self):
    #     self.browser.get(self.live_server_url + '/user/login/')
    #     username_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'username'))
    #     )
    #     time.sleep(2)
    #     username_input.send_keys('123')
    #     time.sleep(2)
    #
    #     password_input = self.browser.find_element(By.NAME, 'password')
    #     login_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
    #     )
    #     time.sleep(2)
    #     password_input.send_keys('123')
    #     time.sleep(2)
    #     login_button.click()
    #
    #     time.sleep(2)
    #
    #     self.browser.get(self.live_server_url + '/website/add/')
    #     url_input = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'url'))
    #     )
    #     description_input = self.browser.find_element(By.NAME, 'description')
    #     add_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
    #     )
    #
    #     url_input.send_keys('http://newsite.com')
    #     description_input.send_keys('New site')
    #     add_button.click()
    #
    #     time.sleep(2)  # Wait for the page to load
    #     self.assertIn('http://newsite.com', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, 'button[@type="submit"]'))
#         # EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#         )
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('Welcome', self.browser.page_source)
#
#     def test_register(self):
#         self.browser.get(self.live_server_url + '/user/register/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password1_input = self.browser.find_element(By.NAME, 'password1')
#         password2_input = self.browser.find_element(By.NAME, 'password2')
#         register_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, 'button[@type="submit"]'))
#         # EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#         )
#
#         username_input.send_keys('newuser')
#         password1_input.send_keys('newpassword')
#         password2_input.send_keys('newpassword')
#         register_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('Welcome', self.browser.page_source)
#
#     def test_add_website(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, 'button[@type="submit"]'))
#         # EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#
#         )
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.browser.get(self.live_server_url + '/website/add/')
#         url_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'url'))
#         )
#         description_input = self.browser.find_element(By.NAME, 'description')
#         add_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, 'button[@type="submit"]'))
#         # EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#
#         )
#
#         url_input.send_keys('http://newsite.com')
#         description_input.send_keys('New site')
#         add_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('http://newsite.com', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, '123'))
#         )
#         password_input = self.browser.find_element(By.NAME, '123')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#         )
#
#         username_input.send_keys('123')
#         password_input.send_keys('123')
#         login_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('Welcome', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#         )
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('Welcome', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
#         )
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # Wait for the page to load
#         self.assertIn('Welcome', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.assertIn('Welcome', self.browser.page_source)
#
#     def test_add_website(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.browser.get(self.live_server_url + '/website/add/')
#         url_input = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.NAME, 'url'))
#         )
#         description_input = self.browser.find_element(By.NAME, 'description')
#         add_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         url_input.send_keys('http://newsite.com')
#         description_input.send_keys('New site')
#         add_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.assertIn('http://newsite.com', self.browser.page_source)

# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Edge()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = self.browser.find_element(By.NAME, 'username')
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.assertIn('Welcome', self.browser.page_source)
#
#     def test_add_website(self):
#         self.browser.get(self.live_server_url + '/user/login/')
#         username_input = self.browser.find_element(By.NAME, 'username')
#         password_input = self.browser.find_element(By.NAME, 'password')
#         login_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         username_input.send_keys('testuser')
#         password_input.send_keys('testpassword')
#         login_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.browser.get(self.live_server_url + '/website/add/')
#         url_input = self.browser.find_element(By.NAME, 'url')
#         description_input = self.browser.find_element(By.NAME, 'description')
#         add_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
#
#         url_input.send_keys('http://newsite.com')
#         description_input.send_keys('New site')
#         add_button.click()
#
#         time.sleep(2)  # 等待页面加载
#         self.assertIn('http://newsite.com', self.browser.page_source)

# import unittest
# import time
# import ddddocr
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# class TestSuccess(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Edge()
#
#     def tearDown(self):
#         # 关闭浏览器
#         self.driver.quit()
#
#     def test_login_success(self):
#         login_driver = self.driver
#         login_driver.get(self.url)
#         # 点击登录按钮
#         login_driver.find_element(By.XPATH, "//h3/a[@class='button']").click()