# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

#class NobelWinnersPipeline:
#    def process_item(self, item, spider):
#        return item

#scraping images with the image pipeline
import scrapy

#from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.linkextractors import LinkExtractor

class NobelImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item,info):
        for image_url in item['image_urls']:
            yield scrapy.Requests(image_url)

    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok]
        if image_paths:
            item['bio_image'] = image_paths[0]
        return item

'''
from scrapy.exceptions import DropItem

class DropNonPersons(object):
    #Remove non-person winners
    def process_item(self,item,spider):
        if not item['gender']:
            raise DropItem("No gender for %s"%item['name'])
        return item
'''
