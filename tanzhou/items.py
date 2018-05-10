# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TanzhouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    定义爬取的目标，本案例中只爬取标题和价格两个内容
    所以定义两个字段
    """
    # 课程金额
    money = scrapy.Field()
    # 课程名称
    title = scrapy.Field()