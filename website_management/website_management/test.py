import time
import os
import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestReport

class test_Router(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Edge()

    def tearDown(self):
        self.browser.quit()


    ''' 能过，但是是红色的通过，这个的静态文件有问题'''
    # ''' 测试超级管理员页面的路由 '''
    #
    # def test_Router_0(self):
    #     self.browser.get(self.live_server_url + '/')
    #     super_admin_button = WebDriverWait(self.browser, 20).until(
    #         EC.presence_of_element_located((By.XPATH, '//a[@href="/admin" and contains(@class, "button")]'))
    #     )
    #     super_admin_button.click()
    #     # time.sleep(2)
    #     self.assertIn('Django 管理', self.browser.page_source)
    #     self.browser.quit()

    ''' 测试登录页面的路由,然后返回首页 '''

    def test_Router_1(self):
        self.browser.get(self.live_server_url + '/')
        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
        )
        login_button.click()
        # time.sleep(2)
        self.assertIn('Login', self.browser.page_source)
        self.assertIn('Reset', self.browser.page_source)
        return_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Back to Home') and @href='/']"))
        )

        # bug: 这里的xpath语句有问题，无法定位到返回首页的按钮
        # return_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//a[@href='/']"))
        # )
        # return_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="/" '))
        # )
        return_button.click()
        self.assertIn('网站管理系统首页', self.browser.page_source)
        self.assertIn('欢迎来到网站管理系统，这里可以帮助你管理网站的地址', self.browser.page_source)

    ''' 测试先进入登录页面，然后点击注册按钮的路由 '''

    def test_Router_2(self):
        self.browser.get(self.live_server_url + '/')
        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/login/" and contains(@class, "button")]'))
        )
        login_button.click()
        # time.sleep(2)
        self.assertIn('Login', self.browser.page_source)
        self.assertIn('Reset', self.browser.page_source)
        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '/user/register/')]"))
        )
        #bug: 这里的xpath语句有问题，无法定位到注册按钮
        # register_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        # )
        register_button.click()
        self.assertIn('New User Registration', self.browser.page_source)
        self.assertIn('Already have an account?', self.browser.page_source)

    '''测试登录后返回首页，然后点击退出按钮的路由 '''

    def test_Router_3(self):
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

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

        logout_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/user/logout/' and contains(@class, 'button')]"))
        )
        # bug: 这里的xpath语句有问题，无法定位到退出按钮
        # logout_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="user/logout/" and contains(@class, "button")]'))
        # )
        logout_button.click()
        self.assertIn('网站管理系统首页', self.browser.page_source)
        self.assertIn('欢迎来到网站管理系统，这里可以帮助你管理网站的地址', self.browser.page_source)
        self.browser.quit()

    '''测试登录后返回首页，然后点击退出按钮的路由 '''

    def test_Router_4(self):
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

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

        return_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/" and contains(@class, "button")]'))
        )
        return_button.click()
        self.assertIn('网站管理系统首页', self.browser.page_source)
        self.assertIn('欢迎来到网站管理系统，这里可以帮助你管理网站的地址', self.browser.page_source)
        self.browser.quit()


    ''' 测试登录后，进入网址管理页面的路由 '''

    def test_Router_5(self):
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

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

        website_management_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/website/" and contains(@class, "button")]'))
        )
        # bug: 这里的xpath语句有问题，无法定位到网址管理按钮
        # website_management_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="/website_management/" and contains(@class, "button")]'))
        # )

        website_management_button.click()
        self.assertIn('Website List', self.browser.page_source)

        return_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/user/index" and @id="return_button"]'))
        )
        return_button.click()
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)
        self.browser.quit()

    '''测试网址增加模块的路由'''

    def test_Router_6(self):
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

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

        website_management_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/website/" and contains(@class, "button")]'))
        )
        # bug: 这里的xpath语句有问题，无法定位到网址管理按钮
        # website_management_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="/website_management/" and contains(@class, "button")]'))
        # )

        website_management_button.click()
        self.assertIn('Website List', self.browser.page_source)

        add_website_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '/website/add/') and @id='add_button']"))
        )
        add_website_button.click()
        self.assertIn('Add Website', self.browser.page_source)

        return_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/website/') and contains(@class, 'btn')]"))
        )
        return_button.click()
        self.assertIn('Website List', self.browser.page_source)
        self.browser.quit()

    '''测试网站修改的路由'''

    def test_Router_7(self):
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

        # time.sleep(2)
        self.assertIn('用户信息展示', self.browser.page_source)
        self.assertIn('当前登录用户账号', self.browser.page_source)
        self.assertIn('admin', self.browser.page_source)

        website_management_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/website/" and contains(@class, "button")]'))
        )
        # bug: 这里的xpath语句有问题，无法定位到网址管理按钮
        # website_management_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[@href="/website_management/" and contains(@class, "button")]'))
        # )

        website_management_button.click()
        self.assertIn('Website List', self.browser.page_source)

        add_website_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, '/website/add/') and @id='add_button']"))
        )
        add_website_button.click()
        self.assertIn('Add Website', self.browser.page_source)

        # 等待 URL 输入框出现，并输入 URL
        url_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'url'))
        )
        url_input.send_keys('https://stu.z-xin.net/')  # 移除了 HTML 实体编码

        # 等待名称输入框出现，并输入名称
        description_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'description'))
        )
        description_input.send_keys('知新学生端')

        # 等待提交按钮出现，并点击
        submit_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
        )
        submit_button.click()

        # 检查页面源代码中是否包含 'Website List'
        self.assertIn('https://stu.z-xin.net/', self.browser.page_source)
        self.assertIn('知新学生端', self.browser.page_source)

        edit_website_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='submit' and contains(@class, 'edit-button') and @title='编辑网站']"))
        )
        edit_website_button.click()

        url_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'url'))
        )
        url_input.clear()
        url_input.send_keys('https://www.luogu.com.cn/')

        description_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'description'))
        )
        description_input.clear()
        description_input.send_keys('洛谷主页')

        submit_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
        )
        submit_button.click()

        self.assertIn('https://www.luogu.com.cn/', self.browser.page_source)
        self.assertIn('洛谷主页', self.browser.page_source)

        self.browser.quit()

        #

        #   bug: 这里的xpath语句有问题，无法定位到修改按钮
        # url_input = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.NAME, 'url'))
        # )
        # url_input.send_keys('https://www.baidu.com')
        # # time.sleep(2)
        #
        # name_input = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.NAME, 'name'))
        # name_input.send_keys('百度')
        # # time.sleep(2)
        #
        # submit_button = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        # submit_button.click()
        # self.assertIn('Website List', self.browser.page_source)



# class SeleniumTestCase(LiveServerTestCase):
class test_user_register(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Edge()

    def tearDown(self):
        self.browser.quit()

    '''测注册时候，两个密码不一致的情况'''

    ''' 测试通过 '''
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
        self.browser.quit()

    '''测试当已经注册的时候，这时候用户名相同的用户不能再注册'''


    ''' 测试通过 '''

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
        self.browser.quit()

    '''测注册时候，用户名过长'''

    # def tearDown_2(self):
    #     self.browser.quit()
    ''' 测试通过 '''

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
        self.browser.quit()

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
        self.browser.quit()

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
        self.browser.quit()


    # def tearDown_5(self):
    #     self.browser.quit()




class test_user_login(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Edge()

    def tearDown(self):
        self.browser.quit()


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
        self.assertIn('Username or password is incorrect, please try again', self.browser.page_source)
        self.browser.quit()

    ''' 测试注册之后登录，但用户名为空 '''
    '''2_test'''
    '''无法登录'''

    def test_User_login_2(self):
        self.browser.get(self.live_server_url + '/')
        register_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="user/register/" and contains(@class, "button")]'))
        )
        register_button.click()

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)
        username_input.send_keys('admin')
        # time.sleep(2)
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        confirm_password_input = self.browser.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('12345')

        register_button = self.browser.find_element(By.XPATH, '//input[@type="submit"]')
        register_button.click()

        self.browser.get(self.live_server_url + '/user/login/')

        username_input = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # time.sleep(2)

        # time.sleep(2)
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('12345')

        login_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        )
        # time.sleep(2)
        login_button.click()

        self.assertIn('Login', self.browser.page_source)
        self.assertIn('Reset', self.browser.page_source)
        self.browser.quit()



if __name__ == "__main__":
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)

    # 获取脚本所在的目录
    script_dir = os.path.dirname(script_path)


    # 获取输出报告的目录路径
    output_dir = 'D:\\report'

    # 设置工作目录为输出路径
    os.chdir(output_dir)

    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(test_Router("test_Router_1"))
    suite.addTest(test_Router("test_Router_2"))
    suite.addTest(test_Router("test_Router_3"))
    suite.addTest(test_Router("test_Router_4"))
    suite.addTest(test_Router("test_Router_5"))
    suite.addTest(test_Router("test_Router_6"))
    suite.addTest(test_Router("test_Router_7"))


    suite.addTest(test_user_register("test_User_register_1"))
    suite.addTest(test_user_register("test_User_register_2"))
    suite.addTest(test_user_register("test_User_register_3"))
    suite.addTest(test_user_register("test_User_register_4"))
    suite.addTest(test_user_register("test_User_register_5_success"))


    suite.addTest(test_user_login("test_User_login_1"))
    suite.addTest(test_user_login("test_User_login_2"))



    # 指定测试报告的输出路径和文件名
    filename = 'D:\\report\\result.html'
    out = open(filename, 'wb')
    runner = HTMLTestReport.HTMLTestRunner(
        stream=out,
        title='用户测试报告',
        description='用户登录和注册功能测试报告'
    )
    runner.run(suite)
    out.close()


    # # 设置工作目录为脚本所在的目录
    # os.chdir(script_dir)
    #
    # # 创建测试套件
    # suite = unittest.TestSuite()
    # suite.addTest(test_user_register("test_User_register_1"))
    # suite.addTest(test_user_register("test_User_register_2"))
    # suite.addTest(test_user_register("test_User_register_3"))
    # suite.addTest(test_user_register("test_User_register_4"))
    # suite.addTest(test_user_register("test_User_register_5_success"))
    # suite.addTest(test_user_login("test_User_login_1"))
    #
    # # 指定测试报告的输出路径和文件名
    # filename = 'D:\\report\\result2.html'
    # out = open(filename, 'wb')
    # runner = HTMLTestReport.HTMLTestRunner(
    #     stream=out,
    #     title='用户测试报告',
    #     description='用户登录和注册功能测试报告'
    # )
    # runner.run(suite)
    # out.close()

    ''' 测试注册之后登录，但密码为空 '''
    '''3_test'''



    ''' 测试注册之后登录，但账户和密码都为空 '''
    ''' 4_test'''

    # def tearDown_login_3(self):
    #     self.browser.quit()


# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(test_user_register("test_User_register_1"))
#     suite.addTest(test_user_register("test_User_register_2"))
#     suite.addTest(test_user_register("test_User_register_3"))
#     suite.addTest(test_user_register("test_User_register_4"))
#     suite.addTest(test_user_register("test_User_register_5_success"))
#     suite.addTest(test_user_login("test_User_login_1"))
#
#     filename = 'D:\\report\\result2.html'
#     out = open(filename, 'wb')
#     runner = HTMLTestReport.HTMLTestRunner(
#         stream=out,
#         title='用户测试报告',
#         description='用户登录和注册功能测试报告'
#     )
#     runner.run(suite)
#     out.close()

