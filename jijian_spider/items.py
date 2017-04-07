# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class JijianSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    pic_url = Field()
    projectname = Field()
    projectaddress = Field()
    properties = Field()
    pattern = Field()
    standards = Field()
    owner_name = Field()
    inuest_coont = Field()
    project_intro = Field()
    proj_state_name = Field()
    link_uname = Field()
    link_tel = Field()
    rest = Field()
    turnover_time = Field()
    intime = Field()
    trend = Field()
    collect = Field()
    isfollow = Field()



