from core import user_manager

WELCOME_INFO = """
*********************** 欢迎来到XUP商城 *************************
               1、 用户登录                 2、 用户注册
               3、 查看商品                 4、 加入购物车
               5、 查看购物车               6、 结算
               7、 退出
"""


def main():
    while True:
        print(WELCOME_INFO)
        inp = input('>>>请输入：').strip()


if __name__ == '__main__':
    main()
