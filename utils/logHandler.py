# -*- coding: utf-8 -*-
import sys
import logging
from conf import settings


class LogHandler(object):
    """
    log_file_path
    log_level
    log_file_level
    log_stream_level
    """
    def __init__(self, log_name, log_file_path, log_level=logging.INFO,
                 log_file_level=logging.WARNING, log_stream_level=logging.DEBUG):
        self.log_name = log_name
        self.log_file_path = log_file_path
        self.log_level = log_level
        self.log_file_level = log_file_level
        self.log_stream_level = log_stream_level
        # 实例化 log 对象
        self.log = logging.getLogger(self.log_name)
        self.log.setLevel(self.log_level)
        if not self.log.handlers:
            # 创建屏幕/文件输出流对象
            s_obj = logging.StreamHandler(sys.stdout)
            f_obj = logging.FileHandler(self.log_file_path)

            # 配置输出内容的格式
            fmt = logging.Formatter(settings.LOG_FORMATTER)

            # 将输出格式 set 到 两个输出流对象中
            s_obj.setFormatter(fmt)
            f_obj.setFormatter(fmt)

            # 将屏幕/文件输出流对象 set 到日志对象中
            self.log.addHandler(s_obj)
            self.log.addHandler(f_obj)

    @property
    def get_log(self):
        return self.log


def log():
    return LogHandler(
        log_name=settings.LOG_NAME,
        log_file_path=settings.LOG_FILE_PATH,
        log_level=settings.LOG_LEVEL,
        log_file_level=settings.LOG_FILE_LEVEL,
        log_stream_level=settings.LOG_STREAM_LEVEL
    ).get_log


if __name__ == '__main__':
    log().debug('debug')
    log().debug('info')
    log().warning('warning')
    log().error('error')
