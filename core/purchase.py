from core import user_manager


class Bill(user_manager.User):

    def goods_list(self):
        res = f'{self.name}执行了查看商品...'

        return res

    def add_to_car(self):
        print('add to car...')

    def check_shopping_car(self):
        print(__name__)

    def settle_accounts(self):
        print()


if __name__ == '__main__':
    b = Bill('alex')
    ret = b.goods_list()
    print(ret)
