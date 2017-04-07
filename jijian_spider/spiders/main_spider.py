# __author__ = "Administrator"
# -*- coding: utf-8 -*-
import json

from scrapy import Spider, Request
from jijian_spider.items import JijianSpiderItem

class JijianSpider(Spider):
    name = 'Jijian'
    first_url = 'http://www.cninct.com/index.php?g=index&m=projectinfo&a=index&page={page}&pagesize=39'
    second_url = 'http://www.cninct.com/index.php?g=index&m=projectinfo&a=info&id={project_id}&page=1'

    def start_requests(self):
        urls = [self.first_url.format(page=page) for page in range(1, 545)]
        for url in urls:
            yield Request(url=url, callback=self.parse_projects)

    def parse_projects(self, response):
        result = json.loads(response.body_as_unicode())
        project_lst = result['ext']['list']  # 字典构成的列表
        for project in project_lst:
            yield Request(
                url=self.second_url.format(project_id=project['id']),
                callback=self.parse_detail)


    def parse_detail(self, reponse):
        results = json.loads(reponse.body_as_unicode())
        item = JijianSpiderItem()

        for field in item.fields:
            if field in results['ext'].keys():
                item[field] = results['ext'].get(field)
        yield item

        for project in results['ext']['other']['list']:
            yield Request(
                self.second_url.format(project_id=project['id']),
                callback=self.parse_detail)


