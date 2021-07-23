import scrapy


class IetfProjectSpider(scrapy.Spider):
    name = 'ietf_project'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.xpath('//span[@class="title"]/text()').get()
        return {"title": title}
      
