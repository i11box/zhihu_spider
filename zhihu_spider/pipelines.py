# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import re

class ZhihuSpiderPipeline:
    
    def open_spider(self, spider):
        self.file = open('questionsId.json', 'w', encoding='utf-8')
        self.file.write('[')  # 开始一个 JSON 数组
    
    def close_spider(self, spider):
        self.file.write(']')  # 结束一个 JSON 数组
        self.file.close()
        
    
    def process_item(self, item, spider):
        try:
            item['title'] = re.sub(r'\\u003c.*?\\u003e|<.*?>', '', item['title'])
            line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(line)
        except BaseException as e:
            print("错误-----------",e)
        return item
