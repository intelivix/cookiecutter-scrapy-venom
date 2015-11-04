# -*- coding: utf-8 -*-

from scrapy_venom.steps import Step
from .items import LinkItem
from .items import OtherItem


__all__ = ['SampleStep']


class NextSampleStep(Step):

    item_class = OtherItem

    def crawl(self, selector, **kwargs):
        print('passando pelo {mensagem} step'.format(**kwargs))


class SampleStep(Step):

    next_step_cls = NextSampleStep
    item_class = LinkItem

    def clean_item(self, extraction):
        # LIMPANDO UM ITEM
        return {'link': extraction}

    def crawl(self, selector):

        # EXTRAINDO OS ITENS (LinkItem)
        print('passando pelo primeiro step')
        yield selector.xpath('//a/@href')

        # EXECUTANDO PROXIMO STEP
        kwargs = self.get_kwargs_for_next_step()
        for item in self.next_step(selector, **kwargs):
            yield item

    def get_kwargs_for_next_step(self):
        return {'mensagem': 'segundo'}
