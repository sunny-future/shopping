# -*- coding: utf-8 -*-
from core import core
from conf import settings


def action_choice():
    """
    打印功能列表
    :return:
    """
    for ind, item in enumerate(settings.INFO.keys(), 1):
        print(ind, item)


def main():
    """
    主程序入口，功能选择
    :return:
    """
    user = core.User()
    while 1:
        print(f" 欢迎来到德莱商城 ".center(80, '*'))
        action_choice()
        inp = input("请输入功能选项：").strip()
        if inp.isdecimal() and int(inp) in range(len(settings.INFO.keys()) + 1):
            menu = [index for index in settings.INFO.keys()]
            action = settings.INFO[menu[int(inp) - 1]]
            getattr(user, action)()
        else:
            print('输入有误哦!')


if __name__ == '__main__':
    main()

