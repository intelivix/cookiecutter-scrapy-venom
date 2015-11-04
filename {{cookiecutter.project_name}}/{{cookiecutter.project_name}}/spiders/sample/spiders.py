# -*- coding: utf-8 -*-

from scrapy_venom.spiders import SpiderStep
from .steps import SampleStep


__all__ = ['SampleSpider']


class SampleSpider(SpiderStep):

    name = 'sample-spider'
    initial_step_cls = SampleStep
    initial_url = 'https://www.google.com.br/?q=facebook'
    pipelines_allowed = ['sample.SamplePipeline']
