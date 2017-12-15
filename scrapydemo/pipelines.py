# -*- coding: utf-8 -*-

# item pipelines
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


class ScrapydemoPipeline(object):
    # item pipelines

    def process_item(self, item, spider):
        return item
