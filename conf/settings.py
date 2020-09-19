import os
import datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# -------------- salt ---------------

SALT = 'RedSalt369*!#++'


# -------------- db ---------------

USER_INFO = os.path.join(BASE_DIR, 'db', 'user_info')
USER_INFO_TMP = os.path.join(BASE_DIR, 'db', 'user_info_tmp')
GOODS_LIST = os.path.join(BASE_DIR, 'db', 'goods_list')
SHOPPING_CARS = os.path.join(BASE_DIR, 'db', 'shopping_car')
SHOPPING_CARS_TMP = os.path.join(BASE_DIR, 'db', 'shopping_car_tmp')

# -------------- actions ------------
INFO = {'用户登录': 'login', '用户注册': 'register',
        '查看商品': 'goods_list', '加入购物车': 'add_to_car',
        '查看购物车': 'show_shopping_car', '结算': 'bill',
        '退出': 'log_out'}


# -------------- log ------------
LOG_NAME = 'ShoppingMall'
# 按天切割日志
LOG_FILE_NAME = '{}{}'.format(datetime.datetime.today().strftime('%Y-%m-%d'), '.log')
LOG_FILE_PATH = os.path.join(BASE_DIR, 'log', LOG_FILE_NAME)
LOG_LEVEL = logging.DEBUG     # 只有屏幕输出流和文件输出流对象的level大于等于日志level时，才会输出结果
LOG_FILE_LEVEL = logging.WARNING
LOG_STREAM_LEVEL = logging.DEBUG
LOG_FORMATTER = "%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s"


if __name__ == '__main__':
    print(LOG_FILE_NAME)
