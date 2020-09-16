import os
import hashlib
from functools import wraps
from conf import settings


class User(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def register(self):
        with open(settings.USER_INFO, mode='w', encoding='utf-8') as f:
            f.write(f'{self.name}|{self.get_sha1()}|unauthorized\n')
        return True

    def login(self):
        with open(settings.USER_INFO, mode='r', encoding='utf-8') as f1,\
             open(settings.USER_INFO_TMP, mode='w', encoding='utf-8') as f2:
            flag = False
            for line in f1:
                user_name, password, status = line.strip().split('|')
                if self.name == user_name and self.get_sha1() == password:
                    f2.write(f'{self.name}|{self.get_sha1()}|authorized\n')
                    flag = True
                else:
                    f2.write(line)
        os.remove(settings.USER_INFO)
        os.rename(settings.USER_INFO_TMP, settings.USER_INFO)
        if flag:
            return True
        return False

    def login_required(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
                if self.is_authorized():
                    ret = func(*args, **kwargs)
                    return ret
                else:
                    print(f'{func.__name__} need login...')
        return inner

    def get_sha1(self):
        pwd_sha1 = hashlib.sha1(settings.SALT.encode('utf-8'))
        pwd_sha1.update(self.pwd.encode('utf-8'))
        ret = pwd_sha1.hexdigest()
        return ret

    def is_authorized(self):
        with open(settings.USER_INFO, mode='r', encoding='utf-8') as f:
            for line in f:
                user_name, password, status = line.strip().split('\n')
                if self.name == user_name and password == self.get_sha1():
                    if status == 'authorized':
                        return True
                return False


if __name__ == '__main__':
    u1 = User('alex', 'alex')
    print(u1.name)
    u1.register()
    u1.login()
