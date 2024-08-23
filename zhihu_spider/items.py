# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuestionItem(scrapy.Item):
    question_id = scrapy.Field()
    title = scrapy.Field()

class QuestionInfoItem(scrapy.Item):
    question_id = scrapy.Field()
    question_name = scrapy.Field()

class AnswerItem(scrapy.Item):
    question_id = scrapy.Field()
    content = scrapy.Field()

