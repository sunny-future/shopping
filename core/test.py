#!/bin/bash
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 20:45
# @Author  : 张开
# File      : 学员选课系统.py


# https://www.cnblogs.com/Eva-J/articles/9235899.html



"""
1. 作业交的太少了



关于课程类，目前只有属性没有方法



接下来的代码逻辑：
1. 学生类先放放，优先实现管理员的功能
2. 创建学生对象和课程对象，用pickle序列化到文件中
3. 优化：用上反射
"""
import hashlib


class Course(object):
    """ 课程类 """
    pass


class Manager(object):
    """ 管理员 """
    operate_list = [
        "创建课程",
        "创建学生学生账号",
        "查看所有课程",
        "查看所有学生",
        "查看所有学生的选课情况",
        "退出程序",
    ]

    def __init__(self, name):
        self.name = name

    # -------- 参照学生类 实现5个方法

    def q(self):
        exit('拜拜了您嘞')


class Student(object):
    """ 学生 """
    operate_list = [
        "查看可选课程",
        "选择课程",
        "查看所选课程",
        "退出程序",
    ]

    def __init__(self, name):
        self.name = name
        self.course = []

    def show_course(self):
        print('查看可选课程')

    def selected_course(self):
        print('选择课程')

    def show_selected_course(self):
        print('查看所选课程')

    def q(self):
        exit('拜拜了您嘞')


class Operator(object):
    """ 操作 """

    def get_file(self):
        with open(r'D:\tmp\user.txt', 'r', encoding='utf-8') as f:
            return f.readlines()

    def get_md5(self, s):
        return hashlib.md5(s.encode()).hexdigest()

    def login(self):
        """ 所有角色登录 """
        username = input('user: ').strip()
        password = input('password: ').strip()
        for line in self.get_file():
            self.user, pwd, self.identify = line.strip().split('|')
            if self.user == username and pwd == self.get_md5(password):
                # print(username, '登录 成功')
                break
        else:
            exit('user [{}] login error'.format(username))

    def handler(self):
        """ 根据不同的登录用户，执行不同的操作 """
        # 调用登录函数，获取登录成功的用户身份
        self.login()
        print(self.identify,self.user, '登录成功')
        if self.identify == 'Student':
            # 学生都要干什么，有什么属性，有什么方法
            s_obj = Student(self.user)
            # print(s_obj.operate_list)
            while 1:
                for index, item in enumerate(s_obj.operate_list, 1):
                    print(index, item)
                num = input('请选择你要做的操作: ').strip()
                if num == '1':
                    s_obj.show_course()
                elif num == '2':
                    s_obj.selected_course()
                elif num == '3':
                    s_obj.show_selected_course()
                elif num == '4':
                    s_obj.q()
                else:
                    print('别瞎输')
                    continue

        elif self.identify == 'Manager':
            pass


if __name__ == '__main__':
    # print(hashlib.md5('123'.encode()).hexdigest())
    obj = Operator()
    obj.handler()
    # user, pwd, identify = ['wangqingxia', '202cb962ac59075b964b07152d234b70', 'Student']
    # print(user, pwd, identify)






























