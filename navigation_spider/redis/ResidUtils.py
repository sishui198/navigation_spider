# -*- coding: utf-8 -*-

import redis


class RedisClient():

    def __init__(self, host, port, pwd):
        self.db = redis.StrictRedis(host=host, port=port, password=pwd, decode_responses=True)



    def add(self, key, value):
        """
        将value添加到对应的key队列
        :param key:
        :param value:
        :return:
        """
        self.db.lpush(key, value)


    def get(self, key):
        """
        从key队列获取左侧第一个元素并从列表中移除
        :param key:
        :return:
        """
        return self.db.lpop(key)