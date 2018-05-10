# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TanzhouPipeline(object):
    """
    编写爬取到的数据保存的逻辑
    """
    def __init__(self):
        """
        可选择实现，对参数做一些初始化的处理
        """
        pass

    def open_spider(self, spider):
        """
        重写open_spider函数，该函数在爬虫启动时就自动执行
        :param spider:
        :return:
        """
        self.file = open("tz.json", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        """
        将yield丢过来的数据进行一定的处理并保存
        :param item:
        :param spider:
        :return:
        """
        # 管道传过来的数据item是一个对象，将它转化为字典，然后存储
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        """
        重写该函数，爬虫执行完毕后执行该函数
        :param spider:
        :return:
        """
        self.file.close()