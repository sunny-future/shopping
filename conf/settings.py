import os
import datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# -------------- salt ---------------

SALT = 'RedSalt369*!#++'


# -------------- db ---------------

USER_INFO = os.path.join(BASE_DIR, 'db', 'user_info')
USER_INFO_TMP = os.path.join(BASE_DIR, 'db', 'user_info_tmp')