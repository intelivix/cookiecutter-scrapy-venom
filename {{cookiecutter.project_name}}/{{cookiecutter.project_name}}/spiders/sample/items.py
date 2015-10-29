# -*- coding: utf-8 -*-

from scrapy import Item
from scrapy import Field


__all__ = ['LinkItem', ]


class LinkItem(Item):
    link = Field()


class OtherItem(Item):
    other = Field()
