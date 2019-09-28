# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sql_parameter_type_change
   Description :
   Author :       'li'
   date：          2019/9/27
-------------------------------------------------
   Change Activity:
                   2019/9/27:
-------------------------------------------------
"""
import time

__author__ = 'li'


class TypeChange(object):
    @staticmethod
    def to_string(json_obj, key):
        """
        change type
        :param json_obj:
        :param key:
        :return:
        """
        if key in json_obj and json_obj[key] is not None:
            return str(json_obj[key])
        return ''

    @staticmethod
    def date_stamp_to_datetime(date_stamp):
        """

        :param date_stamp:
        :return:
        """
        date_stamp = int(date_stamp)
        time_local = time.localtime(date_stamp)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt

    @staticmethod
    def to_int(json_obj, key):
        """
        change type
        :param json_obj:
        :param key:
        :return:
        """
        if key in json_obj and json_obj[key] is not None:
            return int(json_obj[key])
        return 0