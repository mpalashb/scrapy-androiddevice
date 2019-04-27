# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AndroiddeviceInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # title = scrapy.Field()
    # price = scrapy.Field()

    # image_urls = scrapy.Field()
    # images = scrapy.Field()

	java_vm_version = scrapy.Field()
	ro_product_provider = scrapy.Field()
	ro_product_brand = scrapy.Field()
	ro_product_name = scrapy.Field()
	ro_product_model = scrapy.Field()
	ro_product_board = scrapy.Field()
	ro_build_id = scrapy.Field()
	ro_build_version_incremental = scrapy.Field()
	ro_build_version_release = scrapy.Field()
	ro_build_version_sdk = scrapy.Field()
	timezone_olson = scrapy.Field()

	fields = scrapy.Field()