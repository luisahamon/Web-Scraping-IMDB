import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imbd.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulos': filmes.css('.titleColumn a'),
                'anos': filmes.css('.secondaryInfo::text'),
                'avaliaçao': response.css('strong::text')
                }