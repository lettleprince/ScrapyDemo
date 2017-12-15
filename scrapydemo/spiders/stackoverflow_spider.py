# -*- coding: utf-8 -*-

# Spider for Stackoverflow
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowSpider(scrapy.Spider):
    # Spider for Stackoverflow.

    name = "stackoverflow"
    start_urls = ['https://stackoverflow.com/questions?page=1&sort=newest']

    def parse(self, response):
        for question in response.css("div.summary"):
            yield {
                'question_content': question.css("h3 a::text").extract_first(),
                # 为了让内容简短一点，这里换成了问题的提问者
                'user':
                question.css("div.user-details a::text").extract_first()
            }
        for href in response.css('div.pager a:last-of-type'):
            yield response.follow(href, callback=self.parse)


class UserSpider(scrapy.Spider):
    # Spider for Stackoverflow users.

    name = "user"
    start_urls = ['https://stackoverflow.com/questions?page=1&sort=newest']

    def parse(self, response):
        for href in response.css("div.user-details a::attr(href)"):
            yield response.follow(href, self.parse_user)
        for href in response.css('div.pager a:last-of-type'):
            yield response.follow(href, callback=self.parse)

    def parse_user(self, response):
        name = response.css("h2.user-card-name ::text").extract_first().strip()
        bio = response.css("div.bio p::text").extract_first().strip()
        yield {
            'name': name,
            'bio': bio,
        }


class TagSpider(scrapy.Spider):
    # Spider for Stackoverflow Tag.

    name = "tag"

    def start_requests(self):
        url = 'https://stackoverflow.com/questions/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tagged/' + tag + '?sort=frequent'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for question in response.css("div.summary"):
            yield {
                'question_content': question.css("h3 a::text").extract_first(),
                # 为了让内容简短一点，这里换成了问题的提问者
                'user':
                question.css("div.user-details a::text").extract_first()
            }
        for href in response.css('div.pager a:last-of-type'):
            yield response.follow(href, callback=self.parse)
