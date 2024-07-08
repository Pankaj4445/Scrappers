from multiprocessing import connection
import scrapy

from scraper_api import ScraperAPIClient
import re
import pymysql

#def get_scraperapi_url(url):
#        payload = {'api_key': "6ca64052722ccb89b27ec0686713f4a4", 'url': url}
#        proxy_url = "http://api.scraperapi.com?api_key=6ca64052722ccb89b27ec0686713f4a4&url="
 #       return proxy_url
        



class QuotesSpider(scrapy.Spider):
    name = "amazone"
    
 

    

    def start_requests(self):
        urls = ['http://api.scraperapi.com/?api_key=fe681822c94281d9593dbb30bf263c67&url=https://www.amazon.in/OnePlus-Wireless-Earbuds-Active-Cancellation/dp/B07XWB82D9?th=1'
                ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        connection=pymysql.connect(host="localhost",user="root",password="",database="scrap")
        pycursor=connection.cursor()
        

        title=response.xpath('//*[@id="productTitle"]/text()').extract()[0]
        
        print(title)
        
        image= response.css('div.imgTagWrapper img ').xpath('@src').getall()[0]
        
        print(image)
        
        price=response.css('span.a-price-whole::text').extract()[0]
        print(price)
        
        mrp=response.css('span.a-offscreen::text').extract()[0][1:]
        print(mrp)

        discount=response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/text()').extract()[0]
        print(discount)
        
        rating_el=response.css('span.a-icon-alt::text').extract()[0].split(' ')
        rating=rating_el[0]
        print(rating)

        review_el= response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()[0].split(' ')
        review=review_el[0]
        print(review)

        features=response.css('table.a-normal.a-spacing-micro td.a-span9 span::text').getall()

        color=features[1]
        print(color)

        brand=features[0]
        print(brand)

        model=features[3]
        print(model)

                   
        product_link= response.xpath('.//link/@href').getall()[-6]
        print(product_link)

        product_id_el=product_link.split('/')
        product_id=product_id_el[-1]
        print(product_id)
               
        stock=response.xpath('//*[@id="availability"]/span/text()').extract()[0][3]
        if 'I'==stock:
            status=0
        else:
            status=1

        print(status)
        InsertRow="insert into amazone(title,model,image,price,mrp,discount,color,brand,rating,review,id,product_link,oos) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        row=(title,model,image,price,mrp,discount,color,brand,rating,review,product_id,product_link,status)
        pycursor.execute(InsertRow,row)
        
        connection.commit()
        
        
        connection.close()
        
        

        # yield
        
        # {
             
        #      "title" : title,
        #      "model":model,
        #      "brand" : brand,
        #      "price" : price,
        #      "mrp"   : mrp,
        #      "discount" : discount,
        #      "color" : color,
        #      "image" : image,
        #      "id"    : product_id,
        #      "product_link" : product_link,
        #      "rating" : rating,
        #      "review" : review,
        #      "oos":status,
        # }