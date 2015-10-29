# -*- coding: utf-8 -*-

# from intelivix_crawl.mongodb.pipelines import CSVPipeline
from intelivix_crawl.mongodb.pipelines import MongoDBPipeline
from intelivix_crawl.pipelines import PipelineBase
from .items import LinkItem


__all__ = ['SamplePipleline', 'SampleDBPipeline']


class SamplePipleline(PipelineBase):

    items_allowed = [LinkItem]

    def item_pipeline(self, item, spider):
        return item


# class SampleCSVPipeline(CSVPipeline):

#     item_allowed = LinkItem
#     csv_name = ''
#     csv_directory = ''


class SampleDBPipeline(MongoDBPipeline):

    collections = {
        LinkItem: {
            'unique_key': 'link',
            'model': 'Link'
        }
    }
