# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'  # 爬虫名，一个项目下可能有多个爬虫，并且每个爬虫有优先级、并发等设置。scrapy crawl[spider_name]
    allowed_domains = ['meijutt.com']     # 为了防止爬虫项目自动爬取到其他网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，
    start_urls = ['https://www.meijutt.com/new100.html']    # 第一个请求的url，整个程序逻辑的入口，得到response返回给self.parse(self,response=response)


    def parse(self, response):
        # print(respo
        movie_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movie_list:
            # movie.xpath('./h5/text()').extract_first()   # xpath()返回[Selector(),
            name = movie.xpath('./h5/a/text()').extract_first()    # .表示在字标签上继续解析

            item = MovieItem()
            item['name'] = name    # item['name'] = name
            yield item    # 相当于同步脚本方法中的return

