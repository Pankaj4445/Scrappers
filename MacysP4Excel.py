import json
import scrapy
import re
from urllib.parse import urljoin,urlparse
import os
from datetime import datetime
from icecream import ic
from StealthCrawlingScrapy.items import MacysItem
import json
from datetime import datetime
from pytz import timezone, utc
import pandas
##Not Working
def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d

h = get_headers('''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9,hi;q=0.8
    cache-control: no-cache
    dnt: 1
    pragma: no-cache
    sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
    sec-ch-ua-mobile: ?0
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: none
    sec-fetch-user: ?1
    sec-gpc: 1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36            
    ''')

dictdata={} 
class amazonSpider(scrapy.Spider):
    #handle_httpstatus_all = True
    name= 'MacysP4Excel'
    def __init__(self, input=''):
        self.inputFile = input
        ic(input)
                
    def start_requests(self):
        ic(self.inputFile)
        var=pandas.read_csv(self.inputFile)
        for i in var.index:
            varurl=scrapy.Request(var['API URL'][i])
            dictdata[varurl.url]=[var['URL'][i],var['SKU'][i],var['Sublot'][i],var['Frequency'][i],var['Retailer'][i],var['ID'][i]]
            yield scrapy.Request(varurl.url,headers=h)       

    def parse(self, response):
        data=json.loads(response.body)
        date_format='%Y-%m-%d %I:%M:%S:%Z'
        date = datetime.now(tz=utc)
        date = date.astimezone(timezone('US/Central'))
        pstDateTime=date.strftime(date_format)        
        item=MacysItem()
        try:
            item['Producttitle']=data['product'][0]['detail']['name']
        except : 
            item['Producttitle']="N/A"

        try:
            item['RegularPrice']= data['meta']['analytics']['data']['product_original_price'][0]
            #item['RegularPrice']= data['product'][0]['pricing']['price']['finalPrice']['values'][0]['formattedValue']

        except:
            item['RegularPrice']='N/A'
        try:
            item['Brand']=data['product'][0]['detail']['brand']['name']
        except : 
            item['Brand']="N/A"
        try:
            urlog=''
            if response.request.meta.get('redirect_urls'):
                urlog = response.request.meta['redirect_urls'][0]
            else:
                urlog = response.request.url 
            item['URL']=dictdata[urlog][0]
            
        except:
            item['URL']='N/A' 


        try:

            imgData=data['product'][0]['imagery']['images']
            imgstr=''
            for i in imgData:
                if imgstr=='':
                    imgstr='https://slimages.macysassets.com/is/image/MCY/products/'+i['filePath']+'?op_sharpen=1&wid=1230&hei=1500&fit=fit,1&$filterxlrg$&fmt=webp'
                else:
                    imgstr=imgstr+'||'+'https://slimages.macysassets.com/is/image/MCY/products/'+i['filePath']+'?op_sharpen=1&wid=1230&hei=1500&fit=fit,1&$filterxlrg$&fmt=webp'    
           
            if imgstr=='':
                item['Image']='N/A'
            else:
                item['Image']=imgstr    
        except:
            item['Image']="N/A"


        try:        
            item['Reviews']=data['product'][0]['detail']['reviewStatistics']['aggregate']['count']
        except:
            item['Reviews']="N/A"
        try:    
            item['Rating']= data['product'][0]['detail']['reviewStatistics']['aggregate']['rating']
        except:
            item['Rating']= "N/A"  

        try:
            breadcrumdata=data['product'][0]['relationships']['taxonomy']['categories']
            #breadcrumdata=json.loads(bradcrum)
            breadcumstr=''
            for i in breadcrumdata:
                if breadcumstr=='':
                    breadcumstr=i['name']
                else:
                    breadcumstr=breadcumstr+'>'+i['name']    

            if breadcumstr=='':
                item['Breadcrum']="N/A"    
            else:
                item['Breadcrum']=breadcumstr
        except:
            item['Breadcrum']="N/A"  

        try:
            url='https://www.macys.com'+data['meta']['tags']['canonical']
            if url=='':
                item['Canonical_url']="N/A"
            else:
                item['Canonical_url']=url 
        except:
            item['Canonical_url']='N/A'

        try:
            item['Availability']=data['product'][0]['availability']['available']
        except:
            item['Availability']="N/A" 
        try:
            item['Price'] =data['meta']['analytics']['data']['product_price'][0]
            #item['Price'] =data['product'][0]['pricing']['price']['finalPrice']['values'][1]['formattedValue']
            
        except:
            item['Price']='N/A'  

        try:
            bg=data['product'][0]['pricing']['badgesMap']
            offer2str=''
            for i in bg:
                if offer2str=='':
                    offer2str=bg[i]['header']
                else:
                    offer2str=offer2str+'||'+bg[i]['header']

            if offer2str=='':
                item['Offer2']='N/A'
            else:
                item['Offer2']=offer2str    

        except:
            item['Offer2']='N/A'

        try:
            upcs=data['product'][0]['relationships']['upcs']
            UpcStr=''

            for i in upcs:
                if UpcStr=='':
                    UpcStr=upcs[i]['identifier']['upcNumber']
                else:
                    UpcStr=UpcStr+'||'+upcs[i]['identifier']['upcNumber']
            if UpcStr=='':
                item['ALLUPC']='N/A'
            else:
                item['ALLUPC']=UpcStr                

        except:
            item['ALLUPC']='N/A'  

        try:
            karlna=data['product'][0]['details']['klarna']['klarnaDataClientId']
            if karlna=='':
                item['offer1']='N/A'
            else:
                item['offer1']='karlna:True'
        except:
            item['offer1']='N/A'
        try:
            item['Crawl_Date']=pstDateTime
        except:
            item['Crawl_Date']="N/A" 

        try:
            
            item['SKU']=dictdata[urlog][1]
            
        except:
            item['SKU']="N/A" 

        try:
            item['Sublot']=dictdata[urlog][2]
        except:
            item['Sublot']="N/A"                                               
        try:
            item['Frequency']=dictdata[urlog][3]
        except:
            item['Frequency']="N/A"                                               
        try:
            item['Retailer']=dictdata[urlog][4]
        except:
            item['Retailer']="N/A"                                               

        try:
            tieredPrice=data['product'][0]['pricing']['price']['tieredPrice']
            for i in tieredPrice:
                if len(i['values'])>1:
                    if i['label']=='Reg. [PRICE]':
                        try:
                            item['tieredRegularPrice']=i['values'][1]['noCurrency']
                        except:
                            item['tieredRegularPrice']='N/A'
                    if i['label']=='Sale [PRICE]':
                        try:
                            item['tieredSalePrice']=i['values'][1]['noCurrency']
                        except:
                            item['tieredSalePrice']='N/A'
                else:
                    if i['label']=='Reg. [PRICE]':
                        try:
                            item['tieredRegularPrice']=i['values'][0]['noCurrency']
                        except:
                            item['tieredRegularPrice']='N/A'
                    if i['label']=='Sale [PRICE]':
                        try:
                            item['tieredSalePrice']=i['values'][0]['noCurrency']
                        except:
                            item['tieredSalePrice']='N/A'

            
        except:
            item['tieredRegularPrice']="N/A"
            item['tieredSalePrice']='N/A'                                               

        try:
            finalPrice=data['product'][0]['pricing']['price']['finalPrice']['values'][1]['noCurrency']
            item['FinalPrice']=finalPrice
        except:
            item['FinalPrice']="N/A"                                               
        try:
            item['ID']=dictdata[urlog][5]
        except:
            item['ID']="N/A"                                               


        yield item               

       



            
                      

                               




