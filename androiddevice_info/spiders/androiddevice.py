# -*- coding: utf-8 -*-
import json
import os
import random
from scrapy import Spider
from scrapy.http import Request

class AndroiddeviceSpider(Spider):
    name = 'androiddevice'
    allowed_domains = ['androiddevice.info']
    start_urls = ['']

    def __init__(self,sr_term):

        self.start_urls=['https://www.androiddevice.info/devices?search='+sr_term]


    def parse(self, response):
        print (response.url)
        print ('\n')

        listings = response.css('a:nth-of-type(2)::attr(href)').extract()

        for link in listings:
            ac_link = response.urljoin(link)

            sum_meta = link.split('/')[-1]

            yield Request(ac_link, meta={"sum_meta":sum_meta}, callback=self.parse_p)
            # yield scrapy.Request(ac_link, callback=self.parse_p)



        # checking_last = response.xpath('//*[contains(text(),"Last")]').xpath('.//@href').extract_first()

        # if checking_last:
        #     checking_last = checking_last.split('?page=')[-1].split('&')[0]

        #     ran_ = int(checking_last)+1


        # if int(checking_last) is not 1:
        #     for i in range(2, ran_):
        #         next_p = 'https://www.androiddevice.info/devices?page={}&search=samsung'.format(i)

        #         n_link = next_p
        #         yield Request(n_link, callback=self.parse)


    def parse_p(self, response):
        sum_meta = response.meta['sum_meta']

        r = response.url
        r = r.split('/')[-2]

        sum_meta = r

        listings = response.css('th a::attr(href)').extract()

        for link in listings:
            ac_link = response.urljoin(link)

            yield Request(ac_link, callback=self.parse_details)



        checking_last = response.xpath('//*[contains(text(),"Last")]').xpath('.//@href').extract_first()

        if checking_last:
            checking_last = checking_last.split('?page=')[-1].split('&')[0]

            ran_ = int(checking_last)+1


        if int(checking_last) is not 1:
            for i in range(2, ran_):
                # next_p = 'https://www.androiddevice.info/devices?page={}&search=samsung'.format(i)
                next_p = 'https://www.androiddevice.info/submissions/{}'+'?page={}'.format(sum_meta,i)

                n_link = next_p
                yield Request(n_link, callback=self.parse_p)



    def parse_details(self, response):


        url = response.url

        print (url)
        print ('\n')

        item = {}

        items = item

        timezone_olson_random = [
            "America/Indiana/Knox",
            "America/Denver",
            "America/Kentucky/Monticello",
            "America/Detroit",
            "America/Indiana/Petersburg",
            "America/New_York",
            "America/Chicago",
            "America/Kentucky/Louisville",
            "America/Los_Angeles",
            "America/Indianapolis",

        ]


        java_vm_version = response.xpath('//tr//th[contains(text(),"java_vm_version")]//following-sibling::th//pre//text()').extract_first()
        ro_product_provider = response.xpath('//tr//th[contains(text(),"ro.product.manufacturer")]//following-sibling::th//pre//text()').extract_first()
        ro_product_brand = response.xpath('//tr//th[contains(text(),"ro.product.manufacturer")]//following-sibling::th//pre//text()').extract_first()
        ro_product_name = response.xpath('//tr//th[contains(text(),"ro.product.name")]//following-sibling::th//pre//text()').extract_first()
        ro_product_model = response.xpath('//tr//th[contains(text(),"ro.product.model")]//following-sibling::th//pre//text()').extract_first()
        ro_product_board = response.xpath('//tr//th[contains(text(),"ro.product.board")]//following-sibling::th//pre//text()').extract_first()
        ro_build_id = response.xpath('//tr//th[contains(text(),"ro_build_id")]//following-sibling::th//pre//text()').extract_first()
        ro_build_version_incremental = response.xpath('//tr//th[contains(text(),"ro_build_version_incremental")]//following-sibling::th//pre//text()').extract_first()
        ro_build_version_release = response.xpath('//tr//th[contains(text(),"ro_build_version_release")]//following-sibling::th//pre//text()').extract_first()
        ro_build_version_sdk = response.xpath('//tr//th[contains(text(),"ro_build_version_sdk")]//following-sibling::th//pre//text()').extract_first()
        timezone_olson = random.choice(timezone_olson_random)



        item['java_vm_version'] = java_vm_version
        item['ro_product_provider'] = ro_product_provider
        item['ro_product_brand'] = ro_product_brand
        item['ro_product_name'] = ro_product_name
        item['ro_product_model'] = ro_product_model
        item['ro_product_board'] = ro_product_board
        item['ro_build_id'] = ro_build_id
        item['ro_build_version_incremental'] = ro_build_version_incremental
        item['ro_build_version_release'] = ro_build_version_release
        item['ro_build_version_sdk'] = ro_build_version_sdk
        item['timezone_olson'] = timezone_olson

        formatted_json = json.dumps(items, indent = 4,sort_keys=True)
        with open(os.path.join('out', ro_product_model+".json"), "w") as f:
            f.write(formatted_json)

        yield item