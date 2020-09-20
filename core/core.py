import os
import hashlib
from conf import settings
from utils.logHandler import log


class User(object):

    def register(self):
        """
        新用户注册入口
        :return:
        """
        self.user = input('请输入用户名：')
        self.password = input('请输入密码：')
        if self.is_not_exist():
            with open(settings.USER_INFO, mode='a', encoding='utf-8') as f:
                f.write(f'{self.user}|{self.get_sha1(self.password)}|unauthorized\n')
                # print(f'{self.user}注册成功!')
                log().debug(f'{self.user}注册成功!')
                return True
        else:
            # print(f'用户{self.user}已存在，请重新输入！')
            log().warn(f'用户{self.user}已存在，请重新输入！')

    @staticmethod
    def get_sha1(pas):
        """
        内部使用的 sha1 算法加密
        :param pas: 用户密码
        :return:
        """
        sha1 = hashlib.sha1(settings.SALT.encode())
        sha1.update(pas.encode())
        sha1_pas = sha1.hexdigest()
        return sha1_pas

    def is_not_exist(self):
        with open(settings.USER_INFO, mode='r+', encoding='utf-8') as f:
            for line in f:
                name, pwd, login_status = line.strip().split('|')
                if name == self.user:
                    return False
            else:
                return True

    def login(self):
        """
        用户登录入口
        :return:
        """
        print(f" 用户请登录 ".center(80, '*'))
        user = input('请输入用户名：')
        pwd = input('请输入密码：')
        login_flag = False
        with open(settings.USER_INFO, mode='r', encoding='utf-8') as f1, \
             open(settings.USER_INFO_TMP, mode='a', encoding='utf-8') as f2:
            for line in f1:
                self.user, self.password, self.login_status = line.strip().split('|')
                if user == self.user and self.password == self.get_sha1(pwd):
                    f2.write(f'{user}|{self.password}|authorized\n')
                    login_flag = True
                    break
                else:
                    f2.write(line)
        os.remove(settings.USER_INFO)
        os.rename(settings.USER_INFO_TMP, settings.USER_INFO)
        if login_flag:
            # print(f'{self.user}登录成功！')
            log().info(f'{self.user}登录成功！')
            return True
        else:
            # print(f'用户名或密码错误，{user}登录失败！')
            log().error(f'用户名或密码错误，{user}登录失败！')

    def is_login(self):
        """
        判断用户登录态
        :return:
        """
        if hasattr(self, 'user'):
            with open(settings.USER_INFO, mode='r', encoding='utf-8') as f:
                for line in f:
                    user, password, login_status = line.strip().split('|')
                    if self.user == user and login_status == 'authorized':
                        return True

    def is_login_required(self):
        def inner(self, *args, **kwargs):
            if self.is_login():
                res = getattr(self, self.__name__)
                return res
            else:
                self.is_login()
        return inner

    def goods_list(self):
        """
        打印商品列表
        :return:
        """
        if self.is_login():
            with open(settings.GOODS_LIST, mode='r', encoding='utf-8') as f:
                for line in f:
                    print(line.strip())
            log().info(f'{self.user}查看商品列表.')
        else:
            self.login()

    def add_to_car(self):
        """
        加入购物车
        :return:
        """
        if self.is_login():
            goods = input('请输入商品名>>>')
            nums = input('请输入个数>>>')
            with open(settings.GOODS_LIST, mode='r', encoding='utf-8') as f1, \
                 open(settings.SHOPPING_CARS, mode='a', encoding='utf-8') as f2:
                for line in f1:
                    commodity, price = line.strip().split('|')
                    if commodity == goods:
                        f2.write(f"{self.user}|{commodity}|{price}|{nums}\n")
                        # print(f'{commodity}已加入购物车！')
                        log().info(f'{self.user}将{nums}个{commodity}加入购物车！')
                        break
        else:
            self.login()

    def show_shopping_car(self):
        """
        打印该用户的购物车商品内容
        :return:
        """
        if self.is_login():
            with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f:
                for line in f:
                    user, commodity, price, nums = line.strip().split('|')
                    if user == self.user:
                        print(line.strip())
                log().info(f'{self.user}执行了查看购物车操作')

        else:
            self.login()

    def bill(self):
        """
        结账，清空该用户的购物车
        :return:
        """
        if self.is_login():
            total = []
            with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f1, \
                 open(settings.SHOPPING_CARS_TMP, mode='w', encoding='utf-8') as f2:
                for line in f1:
                    user, commodity, price, nums = line.strip().split('|')
                    if user == self.user:
                        total.append(float(price) * int(nums))
                    else:
                        f2.write(line)
            os.remove(settings.SHOPPING_CARS)
            os.rename(settings.SHOPPING_CARS_TMP, settings.SHOPPING_CARS)
            money = sum(total)
            # print(f'{self.user}共消费{money}元')
            log().debug(f'{self.user}共消费{money}元')
        else:
            self.login()

    def log_out(self):
        """
        退出系统
        :return:
        """
        if self.is_login():
            with open(settings.USER_INFO, mode='r', encoding='utf-8') as f1, \
                 open(settings.USER_INFO_TMP, mode='w', encoding='utf-8') as f2:
                for line in f1:
                    user, password, login_status = line.strip().split('|')
                    if user == self.user:
                        f2.write(f'{user}|{password}|unauthorized\n')
                    else:
                        f2.write(line)
            os.remove(settings.USER_INFO)
            os.rename(settings.USER_INFO_TMP, settings.USER_INFO)
            log().info(f'{self.user}已退出系统')
            quit(f'下次再来哦')
        else:
            self.login()


if __name__ == '__main__':
    u = User()
    # u.register()
    # u.login()
    u.goods_list()
