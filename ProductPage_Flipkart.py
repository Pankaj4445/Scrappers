import csv
import requests
from lxml import html
import time
import datetime
from datetime import date
from datetime import datetime
import pandas as pd
import random
import json
import re
from pytz import timezone, utc
import concurrent.futures

clean = re.compile('<.*?>')
clean2 = re.compile('&.*?;')

NUM_RETRIES = 3
NUM_THREADS = int(input('Thread count = '))

def useragentselector():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.97',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.61',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.61',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.61',
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.61',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 YaBrowser/23.9.0.2325 Yowser/2.5 Safari/537.36'

    ]
    return random.choice(user_agent)


def productcrawl(produrl, SKU_ID, input1):
    useragent = useragentselector()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Host': 'www.flipkart.com',
        # 'cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJYcXJMU1ExZVl3eDVKTEdzaTIiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNjM1MzEyOTUxLCJleHAiOjE2NDMwODg5NTEsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.QgeEo6iiOyksoG04E77Ceg6ay91UpvGDsRFmYrI4r74; visitorppl=XqrLSQ1eYwx5JLGsi2; device_id=XqrLSQ1eYwx5JLGsi2; beautyProfilePopup=1; _gcl_au=1.1.132286446.1635312999; _ga=GA1.2.1288715737.1635313000; _fbp=fb.1.1635313000254.1972253702; _gid=GA1.2.758409461.1635417863; is_robot=false; client_ip=115.96.77.107; listingVers=listingV1; generic_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJLSXdZY1Z2Yzgwdld2QmV1TUoxMjcwMDExNTgwMjA1ODY3IiwibW9kZV9kZXZpY2UiOiJkZXNrdG9wIiwibW9kZV9kZXZpY2VfdHlwZSI6IndlYiIsImlhdCI6MTU4NDA4NjYzOCwiZXhwIjoyNjkwNjQ3NTI0LCJhdWQiOiJ3ZWIiLCJpc3MiOiJ0b2tlbm1pY3Jvc2VydmljZSJ9.RdrqkTAPBDh0Qe-605a_dOYoXOOPcJe33f6tuMioKi8; generic_visitorppl=KIwYcVvc80vWvBeuMJ1270011580205867; session_initiated=Direct; referrer=; utm_source=Direct; utm_medium=; utm_campaign=; gclid=; pclid=; fbclid=; session_initiator=Direct; is_first_session=false; environment=prod; is_webview=false; mode_device=desktop; sessionCreatedTime=1635436869; g_state={}; session_id=94daebe1818be7d8ccf2207234fb96b5; isSessionDetails=true; _gat_UA-28132362-1=1; _gat_UA-28132362-2=1; sessionExpiryTime=1635438679',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'User-Agent': useragent,
    }

    produrl = str(produrl).replace("\n", "")
    for i in range(2):
        try:
            sleeptime = random.randint(2, 4)
            time.sleep(sleeptime)
            resp = requests.get(produrl, headers=headers, timeout=30)
            if resp.status_code == 200:
                break
        except Exception as e:
            print(str(e))
            if i > 0:
                return produrl + ' ^^ ' + str(e), 'Error'
    try:

        prodtree = html.fromstring(resp.text)
        try:
            partjson1 = prodtree.xpath('//script[@type="application/ld+json"]/text()')[0].strip()
            if partjson1 == '{}' or partjson1 == '[]':
                partjson1 = prodtree.xpath('//script[@type="application/ld+json"]/text()')[2].strip()
            else:
                pass
            jsondata1 = json.loads(partjson1)
        except:
            jsondata1 = 'n/a'

        try:
            partjson = prodtree.xpath('//script[@id="is_script"]/text()')[0].strip().replace("window.__INITIAL_STATE__ = ","").replace("{}}};","{}}}").replace("}};", "}}")
            jsondata = json.loads(partjson)
        except:
            jsondata = 'n/a'

        pagestatus = ''
        try:
            pagedata = prodtree.xpath('//div[@class="_3uTeW4"]/text()')[0].strip()
        except:
            try:
                pagedata = prodtree.xpath('//div[@class="_2RZvAZ"]/text()')[0].strip()
            except:
                pagedata = 'n/a'
        if pagedata != 'n/a':
            pagestatus = "Page Not Found"
        else:
            pagestatus = 'n/a'

        try:
            Canonical_URL = prodtree.xpath('//link[@rel="canonical"]/@href')[0].strip()
        except:
            Canonical_URL = 'n/a'

        try:
            Product_URL = str(produrl)
        except:
            Product_URL = 'n/a'

        try:
            Schemaorg = jsondata['pageDataV4']['page']['pageData']['seoData']['schema'][0]['@context']
        except:
            Schemaorg = 'n/a'
        if Schemaorg == 'n/a':
            Schemaorg = jsondata1['@context']
        else:
            pass
        if Schemaorg == "http://schema.org":
            Schemaorg = "Yes"
        else:
            Schemaorg = "n/a"


        try:
            Product_ID = jsondata['pageDataV4']['page']['pageData']['pageContext']['productId']
        except:
            Product_ID = 'n/a'

        try:
            Item_ID = jsondata['pageDataV4']['page']['pageData']['pageContext']['itemId']
        except:
            Item_ID = 'n/a'

        #try:
        #    prodname1 = jsondata['pageDataV4']['page']['pageData']['pageContext']['titles']['title']
        #except:
        #    prodname1 = 'n/a'

        #try:
        #    prodname2 = jsondata['pageDataV4']['page']['pageData']['pageContext']['titles']['subtitle']
        #except:
        #    prodname2 = ''

        try:
            Product_Name = prodtree.xpath('//div[@id="container"]//h1//text()')[0:]
            Product_Name = str(Product_Name).replace("\\xa0","").replace("', '"," ").replace("['","").replace("']","").replace('["',"").replace('"]',"").replace("\", '"," ").replace("', \""," ").replace('", "'," ")
            Product_Name = re.sub(clean2, '', Product_Name)
        except:
            try:
                Product_Name = jsondata1[0]['name']
            except:
                Product_Name = 'n/a'
        try:
            Tag1 = prodtree.xpath('//div[@class="aMaAEs"]/div/span/img/@src')[0].strip()
            tag1 = '62673a.png'
            if  tag1 in Tag1:
                Tag = 'Flipkart Assured'
            else:
                Tag = 'n/a'
        except:
            Tag = 'n/a'

        try:
            Sale_Price = jsondata['pageDataV4']['page']['pageData']['pageContext']['pricing']['prices'][2]['value']
        except:
            try:
                Sale_Price = jsondata['pageDataV4']['page']['pageData']['pageContext']['pricing']['prices'][1]['value']
            except:
                Sale_Price = 'n/a'

        try:
            MRP = jsondata['pageDataV4']['page']['pageData']['pageContext']['pricing']['prices'][0]['value']
        except:
            MRP = 'n/a'

        try:
            Discount_Percentage = prodtree.xpath('//div[@class="CEmiEU"]/div/div[@class="_3Ay6Sb _31Dcoz"]/span/text()')[0].strip()
            Discount_Percentage = str(Discount_Percentage).replace("% off", "%")
        except:
            Discount_Percentage = 'n/a'
        if Discount_Percentage == 'n/a':
            try:
                Discount_Percentage = prodtree.xpath('//div[@class="CEmiEU"]/div/div[@class="_3Ay6Sb _31Dcoz pZkvcx"]/span/text()')[0].strip()
                Discount_Percentage = str(Discount_Percentage).replace("% off", "%")
            except:
                Discount_Percentage = 'n/a'

        try:
            Discount_Price = prodtree.xpath('//div[@class="_1V_ZGU"]/span/text()')[0].strip()
            Discount_Price = str(Discount_Price).replace('Extra ₹','').replace(' off','')
        except:
            Discount_Price = 'n/a'

        Offers_Promotion = []
        Offers_Promo = prodtree.xpath('//div[@class="_3TT44I"]/div/div/span/li/span[1]')
        offercount = len(Offers_Promo)
        for z in range(offercount):
            p= z+1
            try:
                Offers_Promotion1 = prodtree.xpath('//div[@class="_3TT44I"]/div/div/span['+str(p)+']/li/span[1]//text()')
                try:
                    Offers_Promotion2 = prodtree.xpath('//div[@class="_3TT44I"]/div/div/span['+str(p)+']/li/span[2]//text()')
                except:
                    Offers_Promotion2 = ''
                Offers_Promotion3 = str(Offers_Promotion1) + (": ") + str(Offers_Promotion2)
                Offers_Promotion.append(Offers_Promotion3)
            except:
                Offers_Promotion = 'n/a'
        Offers_Promotion = str(Offers_Promotion).replace("[\'", "").replace("\']", "").replace('", "',' ||| ').replace("\', \'"," ||| ").replace(",","").replace('["', "").replace(']"', "").replace("â‚¹", "₹").replace('[]', "")

        try:
            Reviews = jsondata['pageDataV4']['page']['pageData']['pageContext']['rating']['reviewCount']
        except:
            Reviews = '0'

        try:
            Ratings = jsondata['pageDataV4']['page']['pageData']['pageContext']['rating']['average']
        except:
            Ratings = '0'

        try:
            numberofrating = jsondata['pageDataV4']['page']['pageData']['pageContext']['rating']['count']
        except:
            numberofrating = '0'

        try:
            Availability = prodtree.xpath('//div[@class="DOjaWF gdgoEp col-8-12"]/div/div[1]/text()')
            Availability = str(Availability).replace("[\'", "").replace("\']", "").replace("[]", "n/a")

            # if Availability == 'Currently Unavailable':
            #     Availability = 'No'
            # elif Availability == 'Sold Out':
            #     Availability = 'No'
            # elif Availability == 'NOTIFY ME':
            #     Availability = 'No'
            # else:
            #     Availability = 'Yes'
        except:
            Availability = 'n/a'

        # try:
        #     Availability_Messages1 = prodtree.xpath('//div[@class="_1p3MFP dTTu2M"]/ul/li[2]/form/button/text()')
        #     if Availability_Messages1 == []:
        #         Availability_Messages1 = prodtree.xpath('//div[@class="_1p3MFP"]/ul/li[2]/form/button/text()')
        #     Availability_Messages1 = str(Availability_Messages1).replace("[\'", "").replace("\']", "")
        #     # buynow = 'BUY NOW'
        #     if 'BUY NOW' and 'Buy Now' in  Availability_Messages1:
        #         Availability_Messages = 'Instock'
        #     else:
        #         Availability_Messages = 'OutOfStock'
        # except:
        #     Availability_Messages = 'OutOfStock'
        Availability_Messages = 'n/a'

        try:
            Description = prodtree.xpath('//div[@id="container"]//*[contains(text(), "Description")]/..//p/text()')[0].strip()
            Description = str(Description).replace("['", "").replace("']", "").replace("', '", " ").replace("â€™", '"').replace('\r', '').replace('\t', '').replace('\n', '').replace("\\t", "").replace("\\r", "").replace(".  ", " ").replace("  ", " ").replace('["', '').replace('"]', '').replace("\xa0", "")
            Description = re.sub(clean, '', Description)
        except:
            Description = 'n/a'

        if Description == 'n/a' or Description == '[]':
            try:
                Description = prodtree.xpath('//div[@class="_3nkT-2"]/div/div/text()')[0].strip()
                Description = re.sub(clean, '', Description)
                Description = str(Description).replace("['", "").replace("']", "").replace("', '", " ").replace("â€™", '"').replace('\r', '').replace('\t', '').replace('\n', '').replace("\\t", "").replace("\\r", "").replace(".  ", " ").replace("  ", " ").replace('["', '').replace('"]', '').replace("\xa0", "")
            except:
                Description = 'n/a'

        if Description == 'n/a' or Description == '[]':
            try:
                Description = prodtree.xpath('//div[@class="_1AN87F"]/text()')[0].strip()
                Description = re.sub(clean, '', Description)
                Description = str(Description).replace("['", "").replace("']", "").replace("', '", " ").replace("â€™", '"').replace('\r', '').replace('\t', '').replace('\n', '').replace("\\t", "").replace("\\r", "").replace(".  ", " ").replace("  ", " ").replace('["', '').replace('"]', '').replace("\xa0", "")
            except:
                Description = 'n/a'

        if Description == 'n/a' or Description == '[]':
            try:
                Description = prodtree.xpath('//div[@class="_1YokD2 _3Mn1Gg"]/div[3]/div/div[2]/div/text()')[0].strip()
                if Description == "Manufacturing, Packaging and Import Info":
                    Description = 'n/a'
                Description = re.sub(clean, '', Description)
                Description = str(Description).replace("['", "").replace("']", "").replace("', '", " ").replace("â€™", '"').replace('\r', '').replace('\t', '').replace('\n', '').replace("\\t", "").replace("\\r", "").replace(".  ", " ").replace("  ", " ").replace('["', '').replace('"]', '').replace("\xa0", "")
            except:
                Description = 'n/a'

        try:
            Discalimer = prodtree.xpath('//div[@class="_1UhVsV _3AsE0T"]/div[1]/div/text()')[0].strip()
            if Discalimer == "Important Note:":
                try:
                    Discalimer = \
                    prodtree.xpath('//div[@class="_1UhVsV _3AsE0T"]/div[1]/table/tbody/tr/td/ul/li/text()')[0].strip()
                except:
                    Discalimer = 'n/a'
            else:
                Discalimer = 'n/a'
        except:
            Discalimer = 'n/a'

        try:
            Meta_Title = jsondata['seoMeta']['metadata']['seo']['title']
        except:
            Meta_Title = 'n/a'

        try:
            Meta_Data = 'n/a'
        except:
            Meta_Data = 'n/a'

        try:
            Meta_Description = jsondata['seoMeta']['metadata']['seo']['description']
        except:
            Meta_Description = 'n/a'

        breadcrumb3 = []
        try:
            breadcrumb = jsondata['pageDataV4']['productPageMetadata']['breadcrumbs']
            breadcrumb1 = len(breadcrumb)
            for z in range(breadcrumb1):
                try:
                    breadcrumb2 = jsondata['pageDataV4']['productPageMetadata']['breadcrumbs'][z]['title']
                    breadcrumb3.append(breadcrumb2)
                except:
                    breadcrumb3 = "n/a"
        except:
            breadcrumb3 = 'n/a'
        Breadcrumb = str(breadcrumb3).replace("[\'", "").replace("\']", "").replace("\', \'", " > ")

        Main_Image_URL = ''
        MainImageurlcount = ''
        for i in range(2):
            try:
                try:
                    Main_Image_URL = prodtree.xpath('//div[@class="_3kidJX"]/div/img/@src')[0].strip()
                except:
                    Main_Image_URL = ''
                if Main_Image_URL == '':
                    try:
                        Main_Image_URL = prodtree.xpath('//div[@class="_3kidJX"]/div/div/img/@src')[0].strip()
                    except:
                        Main_Image_URL = 'n/a'
                if Main_Image_URL != None:
                    MainImageurlcount = 1

                Main_Image_URL = str(Main_Image_URL).replace("[\'", "").replace("\']", "")#.replace("/416/416/", "/1080/1080/").replace("/832/832/", "/1080/1080/")
                #Main_Image_URL = str(Main_Image_URL).replace("[\'", "").replace("\']", "")
            except:
                Main_Image_URL = 'n/a'

        Allimageurlcount = ''
        Allimageurlcount1 = ''

        try:
            All_Image_URL = []
            imgurl = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents']
            img_count = len(imgurl)
            for y in range(img_count):
                try:
                    image_type = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['contentType']
                    if image_type == "IMAGE":
                        image = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['url']
                        All_Image_URL.append(image)
                except:
                    image_type = 'n/a'
            Allimageurlcount = len(All_Image_URL)
            All_Image_URL = (str(All_Image_URL).replace("['", "").replace("{@width}/{@height}", "1080/1080")
                             .replace("', '"," ||| ").replace("']", "").replace('{@quality}', '70'))
        except:
            All_Image_URL = 'n/a'

        if All_Image_URL == 'n/a':
            try:
                All_Image_URL = prodtree.xpath(
                    '//div[@id="container"]/div/div[3]/div[1]/div[1]/div[1]//ul/li//img/@src')[0:]
                Allimageurlcount = len(All_Image_URL)
                All_Image_URL = str(All_Image_URL).replace("['", "").replace("/128/128/", "/1080/1080/").replace("', '",
                                                                                                                 " ||| ").replace(
                    "']", "")  # .replace("/128/128/", "/1080/1080/")
                # All_Image_URL = str(All_Image_URL).replace("['", "").replace("', '", " ||| ").replace("']", "")
            except:
                All_Image_URL = 'n/a'


        if "360-view_" in All_Image_URL:
            P4_360Image_Present = "Yes"
        else:
            P4_360Image_Present = "No"
        try:
            image_360 = []
            img_360_url = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents']
            img_360_count = len(img_360_url)
            for y in range(img_360_count):
                try:
                    image_type2 = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['contentType']
                    if image_type2 == "IMAGE_360":
                        image2 = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['media360urls'][0:]
                        image2= (str(image2).replace("['", "").replace("{@width}/{@height}", "1080/1080")
                             .replace("', '"," ||| ").replace("']", "").replace('{@quality}', '70'))
                        image_360.append(image2)
                except:
                    image_type = 'n/a'
            image_360 = (str(image_360).replace("['", "").replace("{@width}/{@height}", "1080/1080")
                             .replace("', '", " ||| ").replace("']", "").replace('{@quality}', '70'))
        except:
            image_360 = 'n/a'

        try:
            Image_URL_Count = str(Allimageurlcount)
            if Image_URL_Count == '0':
                Image_URL_Count = str(int(Allimageurlcount1))
            if Image_URL_Count == '0' and MainImageurlcount == 1:
                All_Image_URL = Main_Image_URL
                Image_URL_Count = str(int(MainImageurlcount))
        except:
            Image_URL_Count = 'n/a'


        try:
            try:
                alt_tag_presence = prodtree.xpath('//div[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]//img/@alt')[0].strip()
                alt_tag_presence = 'YES'
            except:
                alt_tag_presence = 'NO'
        except:
            alt_tag_presence = 'NO'

        try:
            image_alt_tag = prodtree.xpath('//div[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]//img/@alt')[0].strip()
        except:
            image_alt_tag = 'n/a'

        vidurl4 = []
        # vidurl3 = []
        try:
            vidurl = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents']
            vidurl1 = len(vidurl)
            for y in range(vidurl1):
                try:
                    vidurl2 = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['contentType']
                    if vidurl2 == "VIDEO":
                        vidurl2 = jsondata['pageDataV4']['page']['data']['10001'][0]['widget']['data']['multimediaComponents'][y]['value']['url']
                        vidurl4.append(vidurl2)
                except:
                    vidurl2 = 'n/a'
        except:
            vidurl4 = 'n/a'
        try:
            VIDEOS_COUNT = len(vidurl4)
        except:
            VIDEOS_COUNT = 'n/a'
        Video_URL = str(vidurl4).replace("[\'", "").replace("\']", "").replace("\', \'", " ||| ").replace("[]", "n/a")

        specification3 = []
        specscount = prodtree.xpath('//div[contains(@class,"_1UhVsV")]/div')
        try:
            speccount = len(specscount)
        except:
            specount = 0
        for a in range(speccount):
            specification_1 = prodtree.xpath('//div[contains(@class,"_1UhVsV")]/div[' + str(a + 1) + ']/table/tbody/tr/td[@class="_1hKmbr col col-3-12"]/text()')
            keycount = len(specification_1)
            mainspec = prodtree.xpath('//div[contains(@class,"_1UhVsV")]/div[' + str(a + 1) + ']/div/text()')[0].strip()

            for key in range(keycount):
                specification1 = prodtree.xpath('//div[contains(@class,"_1UhVsV")]/div[' + str(a + 1) + ']/table/tbody/tr/td[@class="_1hKmbr col col-3-12"]/text()')[key].strip()
                specification2 = prodtree.xpath('//div[contains(@class,"_1UhVsV")]/div[' + str(a + 1) + ']/table/tbody/tr[' + str(key + 1) + ']/td[@class="URwL2w col col-9-12"]/ul/li/text()')
                specification2 = str(specification2).replace("[\'", "").replace("\']", "").replace("\\n", "").replace("\'", "").replace(", ", ",").replace("  ", "")
                specs = str(mainspec) +(" ### ")+str(specification1) + (" === ") + str(specification2)
                specification3.append(specs)
            #spec1 = str(mainspec) +(" %%% ")+ str(specification3)
            #specification4.append(spec1)
        Specification_1 = str(specification3).replace("[\'", "").replace("\']", "").replace("', '", " ||| ").replace('", "'," ||| ").replace("™", "").replace("®", "").replace("\\n", "").replace("\\t", "").replace('["','').replace('"]','')

        if Specification_1 == '[]':
            try:
                specscount = len(jsondata['pageDataV4']['page']['data']['10006'])
            except:
                specscount = 0
            for sp in range(specscount):
                try:
                    specinfo = jsondata['pageDataV4']['page']['data']['10006'][sp]['widget']['type']
                except:
                    specinfo = 'n/a'
                if specinfo == 'PRODUCT_DETAILS':
                    try:
                        speccount = len(jsondata['pageDataV4']['page']['data']['10006'][sp]['widget']['data']['renderableComponent']['value']['specification'])
                    except:
                        speccount = 0
                    for spec in range(speccount):
                        specification1 = jsondata['pageDataV4']['page']['data']['10006'][sp]['widget']['data']['renderableComponent']['value']['specification'][spec]['name']
                        specification2 = jsondata['pageDataV4']['page']['data']['10006'][sp]['widget']['data']['renderableComponent']['value']['specification'][spec]['values']
                        specification2 = str(specification2).replace("[\'", "").replace("\']", "").replace("\\n", "").replace("\'", "").replace(", ", ",").replace("  ", "")

                        specification = str(specification1) + (" === ") + str(specification2)
                        specification3.append(specification)
                    Specification_1 = str(specification3).replace("['", "").replace("']", "").replace("', '", " ||| ").replace('", "'," ||| ").replace("™", "").replace("®", "").replace("\\n", "").replace("\\t", "").replace('["','').replace('"]','').replace("""", '""", ' ||| ').replace('''', "''', ' ||| ')

        if Specification_1 == '[]':
            try:
                specscount = len(jsondata['pageDataV4']['page']['data']['10005'])
            except:
                specscount = 0
            for sp in range(specscount):
                try:
                    specinfo = jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['type']
                except:
                    specinfo = 'n/a'
                if specinfo == 'PRODUCT_SPECIFICATION':
                    Speched_count = len(jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'])
                    for SH in range(Speched_count):
                        try:
                            speccount = len(jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'][SH]['value']['attributes'])
                        except:
                            speccount = 0
                        try:
                            specificationkey1 = jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'][SH]['value']['key']
                        except:
                            specificationkey1 = 'n/a'
                        for spec1 in range(speccount):
                            try:
                                specificationkey = jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'][SH]['value'][spec1]['key']
                            except:
                                specificationkey = str(specificationkey1)
                            specification1 = jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'][SH]['value']['attributes'][spec1]['name']
                            specification2 = jsondata['pageDataV4']['page']['data']['10005'][sp]['widget']['data']['renderableComponents'][SH]['value']['attributes'][spec1]['values']
                            specification2 = str(specification2).replace("[\'", "").replace("\']", "").replace("\\n", "").replace("\'", "").replace(", ", ",").replace("  ", "")

                            specification = str(specificationkey) + (" ### ") + str(specification1) + (" === ") + str(specification2)
                            specification3.append(specification)
                        Specification_1 = str(specification3).replace("['", "").replace("']", "").replace("', '", " ||| ").replace('", "', " ||| ").replace("™", "").replace("®", "").replace("\\n", "").replace("\\t","").replace('["', '').replace('"]', '').replace("""", '""", ' ||| ').replace('''', "''', ' ||| ')

        if Specification_1 == '[]':
            Specification_1 = 'n/a'

        # try:
        #     ALL_SPECIFICATION= []
        #     Spec_Hed_Count = len(prodtree.xpath('//div[@class="_1OjC5I"]/div'))
        #     for SH in range(Spec_Hed_Count):
        #         Spec_Hed = prodtree.xpath('//div[@class="_1OjC5I"]/div['+str(SH+1)+']/div/text()')[0].strip()
        #         Spec_values_count = len(prodtree.xpath('//div[@class="_1OjC5I"]/div['+str(SH+1)+']/table/tbody/tr'))
        #         for SV in range(Spec_values_count):
        #             try:
        #                 Spec_Key = prodtree.xpath('//div[@class="_1OjC5I"]/div['+str(SH+1)+']/table/tbody/tr['+str(SV+1)+']/td[contains(@class,"+fFi1w")]//text()')
        #                 Spec_Key = str(Spec_Key).replace("['", "").replace("']", "").replace('["', '').replace('"]', '').replace("', '"," ").replace("\", '", " ").replace("', \"", " ").replace('", "', ' ').replace('\\n', '').replace("[]", "  ")
        #             except:
        #                 Spec_Key = ''
        #             try:
        #                 Spec_Value = prodtree.xpath('//div[@class="_1OjC5I"]/div['+str(SH+1)+']/table/tbody/tr['+str(SV+1)+']/td[contains(@class,"Izz52n")]//text()[normalize-space()]')
        #                 Spec_Value = str(Spec_Value).replace("['", "").replace("']", "").replace('["', '').replace('"]', '').replace("', '"," ").replace("\", '", " ").replace("', \"", " ").replace('", "', ' ').replace('\\n', '').replace("[]", " ")
        #             except:
        #                 Spec_Value = ''
        #             Spec = str(Spec_Hed)+ " ### "+str(Spec_Key)+ " === "+str(Spec_Value)
        #             ALL_SPECIFICATION.append(Spec)
        # except:
        #     ALL_SPECIFICATION = 'n/a'
        # ALL_SPECIFICATION = str(ALL_SPECIFICATION).replace("['", "").replace("']", "").replace('["', '').replace('"]', '').replace("', '"," ||| ").replace("\", '", " ||| ").replace("', \"", " ||| ").replace('", "', ' ||| ').replace('\\n', '').replace("[]", "n/a")
        #

        try:
            prodinfocount = prodtree.xpath('//div[@id="container"]//*[contains(text(), "Product Description")]/../../div')
            prodcount = len(prodinfocount)
        except:
            prodcount = 0

        # for x in range(prodcount):
             # prodinfo1 = prodtree.xpath('//div[@class="K4SXrT funtru"]/div/div/div[2]/div[@class="_3qWObK"]/text()')[x]
             # prodinfo2 = prodtree.xpath('//div[@class="K4SXrT funtru"]/div/div/div[2]/div[@class="_3zQntF"]/p/text()')[x]
             ##prodinfo3 = prodtree.xpath('//div[@class="K4SXrT funtru"]/div/div/div/img/@src')[x]
             # prodinfomation = str(prodinfo1) + (" === ") + str(prodinfo2)
             # prodinfo.append(prodinfomation)
        try:
            prodinfo = []
            prodinfo1 = prodtree.xpath('//div[@id="container"]//*[contains(text(), "Product Description")]/../../div/div/div/div/div[2]/div[1]/text()')[0:]
            prodinfo2 = prodtree.xpath('//div[@id="container"]//*[contains(text(), "Product Description")]/../../div//p/text()')[0:]
            for i in range(len(prodinfo1)):
                prodinfomation = str(prodinfo1[i]) + " === " + str(prodinfo2[i])
                prodinfo.append(prodinfomation)
            Aplus_Content = str(prodinfo).replace("['", "").replace("']", "").replace("', '", " ||| ").replace("\'", "'").replace("™", "").replace("®", "").replace("[", "").replace("]", "")
        except:
            Aplus_Content = 'n/a'
        try:
            A_CONTENT_COUNT = len(prodinfo1)
        except:
            A_CONTENT_COUNT = '0'


        try:
            Customer_QA_Count = prodtree.xpath('//div[@class="_1v1N_F"]/div/div/div/div/div/span[2]')
            Customer_QA_Count = len(Customer_QA_Count)
        except:
            Customer_QA_Count = 'n/a'

        customerqa3 = []
        customercount = prodtree.xpath('//div[@class="HKcm+1"]/div/div/div/div/div/span[2]')
        try:
            count = len(customercount)
        except:
            count = 0
        for a in range(count):
            customerqa1 = prodtree.xpath('//div[@class="HKcm+1"]/div/div/div/div/div/span[2]/text()')[a].strip()
            customerqa2 = prodtree.xpath('//div[@class="HKcm+1"]/div/div/div/div/div[2]/div/span[2]/text()')[a].strip()
            customerqa2 = str(customerqa2).replace("[\'", "").replace("\']", "").replace("\\n", "").replace(",", "").replace("  ", "")
            qa = str(customerqa1) + (" === ") + str(customerqa2)
            customerqa3.append(qa)
        Customer_QA = str(customerqa3).replace("[\'", "").replace("\']", "").replace("', '"," ||| ").replace("\\n", "").replace("™", "").replace("®", "").replace('["', '').replace('"+', '')

        # imagereview4 = []
        # try:
            # ImageReview = prodtree.xpath('//div[@class="_2nMSwX _1yGd2h"]/div//@style')
        # except:
            # ImageReview = ''
        # if ImageReview == []:
            # try:
                # ImageReview = prodtree.xpath('//div[@class="_2nMSwX _1yGd2h _33R3aa"]/div//@style')
            # except:
                # ImageReview = ''
        # try:
            # imgcount = len(ImageReview)
        # except:
            # imgcount = '0'
            
        # for x in range(imgcount):
            # try:
                # imagereview1 = prodtree.xpath('//div[@class="_2nMSwX _1yGd2h"]/div//@style')[x]
            # except:
                # imagereview1 = prodtree.xpath('//div[@class="_2nMSwX _1yGd2h _33R3aa"]/div//@style')[x]
            # imagereview2 = str(imagereview1).replace("background-image:url(", "")
            # imageview3 = imagereview2.split(')')[-3]
            # imagereview4.append(imageview3)
        # if ImageReview == []:
            # Image_Review = 'n/a'
        # else:
            # Image_Review = str(imagereview4).replace("[\'", "").replace("\']", "").replace("\', \'", " ||| ").replace(",", "")
        
        
        try:
            Image_Review = []
            imgcount = prodtree.xpath('//div[@class="row"]//div[contains(@style, "background-image")]/@style')[0:]
            for img in imgcount:
                cust_img = str(img).split('),')[0].split('(')[1].strip()
                Image_Review.append(cust_img)
            Image_Review = str(Image_Review).replace("['", "").replace("']", "").replace("', '", " ||| ").replace(",", "")    
            # Image_Review = str(Image_Review).replace("[\'", "").replace("\']", "").replace("\', \'", " ||| ").replace(",", "")    
        except:
            Image_Review = 'n/a'
            
        try:
            Top_Reviews1 = prodtree.xpath('//div[@class="col JOpGWq"]/div[@class="_2c2kV-"]/div/div/div/div/div[@class="t-ZTKy"]//text()')
            Top_Reviews = str(Top_Reviews1).replace("[\'", "").replace("\']", "").replace("', '"," ### ").replace('", "'," ### ").replace("\", '"," ### ").replace("', \""," ### ").replace('### READ MORE ###',' ||| ').replace("### READ MORE","").replace('["','').replace('"]','')
            #Top_Reviews = str(Top_Reviews).replace("[\'", "").replace("\']", "").replace("\', \'", " &&& ").replace("', ", " &&& ").replace("*","").replace("[", "").replace("]", "").replace('"', "").replace("&&& READ MORE &&&"," ||| ").replace("'READ MORE &&&", " ||| ").replace("&&& READ MORE"," ||| ").replace(", 'READ MORE',","")
        except:
            Top_Reviews = 'n/a'
        if Top_Reviews == '[]':
            try:
                Top_Reviews1 = prodtree.xpath('//div[@class="col JOpGWq _33R3aa"]/div[@class="_2c2kV- _33R3aa"]/div/div/div/div/div[@class="t-ZTKy _1QgsS5"]/div/div[@class="_6K-7Co"]//text()')
                Top_Reviews = str(Top_Reviews1).replace("[\'", "").replace("\']", "").replace("', '", " ### ").replace('", "', " ### ").replace("\", '", " ### ").replace("', \"", " ### ").replace('### READ MORE ###', ' ||| ').replace("### READ MORE", "").replace('["', '').replace('"]', "")
            except:
                Top_Reviews = 'n/a'
        if Top_Reviews == '[]':
            Top_Reviews = 'n/a'

        Consumer_Ratings = []
        Consumer_Ratingscount = prodtree.xpath('//div[@class="_2LE14f"]/div/a//div//div[2]')
        try:
            count1 = len(Consumer_Ratingscount)
        except:
            count1 = 0
        for x in range(count1):
            Consumer_Ratings1 = prodtree.xpath('//div[@class="_2LE14f"]/div/a//div//div[2]//text()')[x]
            Consumer_Ratings2 = prodtree.xpath('//div[@class="_2LE14f"]/div/a//div//div[1]//text()')[x]
            Consumer_Ratings_Infomation = str(Consumer_Ratings1) + (": ") + str(Consumer_Ratings2)
            Consumer_Ratings.append(Consumer_Ratings_Infomation)
        Consumer_Ratings = str(Consumer_Ratings).replace("[\'", "").replace("\']", "").replace("\', \'",
                                                                                               " || ").replace(",",
                                                                                                               "").replace(
            "™", "").replace("®", "")

        try:
            Features_Highlights = jsondata['pageDataV4']['page']['data']['10004'][0]['widget']['data']['highlights']['value']['text']
            feature_count = len(Features_Highlights)
            Features_Highlights = str(Features_Highlights).replace("[\'", "").replace("\']", "").replace("\', \'", " ||| ")
        except:
            Features_Highlights = 'n/a'

        try:
            KEY_FEATURES_COUNT = str(feature_count)
        except:
            KEY_FEATURES_COUNT = 'n/a'

        try:
            Product_Includes = prodtree.xpath(
                '//div[@class="_1UhVsV _3AsE0T"]/div[1]/table/tbody/tr[1]/td/ul/li/text()')
            Product_Includes = str(Product_Includes).replace("['", "").replace("']", "").replace("', '", ", ")
        except:
            Product_Includes = 'n/a'

        try:
            User_Manual = 'n/a'
        except:
            User_Manual = 'n/a'

        try:
            Color = prodtree.xpath('//div[@class="_1YokD2 _2GoDe3"]/div/div/div/div[1]/div[1]/ul/li/div/div/text()')
            Color = str(Color).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
        except:
            Color = 'n/a'
        if Color == '[]':
            try:
                Color = prodtree.xpath('//div[@class="_22QfJJ"]/div/ul/li[contains(@id,"-color")]/div/div/text()')
                Color = str(Color).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
            except:
                Color = 'n/a'

        try:
            Size = prodtree.xpath('//div[@class="_1YokD2 _2GoDe3"]/div/div/div/div[2]/div[1]/ul/li/div/div/text()')
            Size = str(Size).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
        except:
            Size = 'n/a'
        if Size == '[]':
            Size = 'n/a'

        varianturl3 = []
        try:
            varianturl = prodtree.xpath('//ul[@class="_1q8vHb"]/li/a/@href')
            variantcount = len(varianturl)
            for x in range(variantcount):
                varianturl1 = prodtree.xpath('//ul[@class="_1q8vHb"]/li/a/@href')[x]
                varianturl2 = "https://www.flipkart.com" + str(varianturl1)
                varianturl3.append(varianturl2)
        except:
            varianturl3 = 'n/a'
        Variant_URL = str(varianturl3).replace("[\'", "").replace("\']", "").replace("\', \'", " ||| ")
        if Variant_URL == '[]':
            Variant_URL = 'n/a'

        try:
            Weight_RAM_Height = prodtree.xpath(
                '//div[@class="_1YokD2 _2GoDe3"]/div/div/div/div[3]/div[1]/ul/li/div/div/text()')
            Weight_RAM_Height = str(Weight_RAM_Height).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
        except:
            Weight_RAM_Height = 'n/a'
        if Weight_RAM_Height == '[]':
            Weight_RAM_Height = 'n/a'

        try:
            sellername = prodtree.xpath('//div[@id="sellerName"]/span/span/text()')[0].strip()
        except:
            sellername = 'n/a'

        try:
            sellercount = prodtree.xpath('//li[@class="_38I6QT"]/a/span[@class="_1_xoMS"]/text()')
            if sellercount == 'more sellers':
                sellercount = "More than 1 seller are present"
            else:
                sellercount = "Only 1 seller is present"
        except:
            sellercount = 'n/a'

        try:
            Sold_By = str(sellername) + (" === ") + str(sellercount)
        except:
            Sold_By = 'n/a'

        try:
            Seller_Info = 'n/a'
        except:
            Seller_Info = 'n/a'

        try:
            EAN = 'n/a'
        except:
            EAN = 'n/a'

        try:
            UPC = 'n/a'
        except:
            UPC = 'n/a'

        try:
            Brand = jsondata['pageDataV4']['page']['pageData']['pageContext']['brand']
            # Brand = str(Brand).replace(" Mobiles", "")
        except:
            Brand = 'n/a'

        try:
            Category = jsondata['pageDataV4']['page']['pageData']['pageContext']['analyticsData']['category']
        except:
            Category = 'n/a'


        try:
            Range_Price = 'n/a'
        except:
            Range_Price = 'n/a'

        try:
            Price_Type = 'n/a'
        except:
            Price_Type = 'n/a'

        try:
            UOM = 'n/a'
        except:
            UOM = 'n/a'
        try:
            Quantity = 'n/a'
        except:
            Quantity = 'n/a'

        try:
            Dimensions = 'n/a'
        except:
            Dimensions = 'n/a'

        Country_of_origin = ''
        try:
            countofcountry =  len(jsondata['pageDataV4']['page']['data']['10005'])
        except:
            countofcountry = 0
        for m in range(countofcountry):
            try:
                maninfo = jsondata['pageDataV4']['page']['data']['10005'][m]['widget']['type']
            except:
                maninfo = 'n/a'
            if maninfo == 'PRODUCT_SPECIFICATION':
                try:
                    count_of_origin = len(jsondata['pageDataV4']['page']['data']['10005'][m]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'])
                except:
                    count_of_origin = 0
                for o in range(count_of_origin):
                    try:
                        Country_of_origin1 = jsondata['pageDataV4']['page']['data']['10005'][m]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][o]['key']
                        if Country_of_origin1 == 'Country of Origin':
                            Country_of_origin = jsondata['pageDataV4']['page']['data']['10005'][m]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][o]['values']
                            Country_of_origin = str(Country_of_origin).replace("['","").replace("']","").replace("', '", " || ")
                    except:
                        Country_of_origin = 'n/a'

        if Country_of_origin == '':
            try:
                countofcountry = len(jsondata['pageDataV4']['page']['data']['10006'])
            except:
                countofcountry = 0
            for m in range(countofcountry):
                try:
                    maninfo = jsondata['pageDataV4']['page']['data']['10006'][m]['widget']['type']
                except:
                    maninfo = 'n/a'
                if maninfo == 'PRODUCT_DETAILS':
                    try:
                        count_of_origin = len(jsondata['pageDataV4']['page']['data']['10006'][m]['widget']['data'][
                                                  'listingManufacturerInfo']['value']['mappedCards'])
                    except:
                        count_of_origin = 0
                    for o in range(count_of_origin):
                        try:
                            Country_of_origin1 = jsondata['pageDataV4']['page']['data']['10006'][m]['widget']['data'][
                                'listingManufacturerInfo']['value']['mappedCards'][o]['key']
                            if Country_of_origin1 == 'Country of Origin':
                                Country_of_origin = \
                                jsondata['pageDataV4']['page']['data']['10006'][m]['widget']['data'][
                                    'listingManufacturerInfo']['value']['mappedCards'][o]['values']
                                Country_of_origin = str(Country_of_origin).replace("['", "").replace("']", "").replace("', '", " || ")
                        except:
                            Country_of_origin = 'n/a'

        if Country_of_origin == '':
            Country_of_origin = 'n/a'

        try:
            Pin_Code = 'n/a'
        except:
            Pin_Code = 'n/a'

        try:
            In_Cart_Status = 'n/a'
        except:
            In_Cart_Status = 'n/a'

        try:
            Shipping_Detail = 'n/a'
        except:
            Shipping_Detail = 'n/a'

        MANUFACTURER_ADDRESS = ''
        try:
            try:
                countofmanadd = len(jsondata['pageDataV4']['page']['data']['10005'])
            except:
                countofmanadd = 0
            for ma in range(countofmanadd):
                try:
                    maninfo = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['type']
                except:
                    maninfo = 'n/a'
                if maninfo == 'PRODUCT_SPECIFICATION':
                    count_of_origin = len(jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'])
                    for o in range(count_of_origin):
                        try:
                            manifacture = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][o]['value']['subTitle']
                            if manifacture == 'Manufactured by:':
                                MANUFACTURER_ADDRESS = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][o]['value']['callouts'][0]
                                MANUFACTURER_ADDRESS = str(MANUFACTURER_ADDRESS).replace("['", "").replace("']", "")
                        except:
                            MANUFACTURER_ADDRESS = 'n/a'
        except:
            MANUFACTURER_ADDRESS = 'n/a'

        if MANUFACTURER_ADDRESS == '':
            try:
                try:
                    countofmanadd = len(jsondata['pageDataV4']['page']['data']['10006'])
                except:
                    countofmanadd = 0
                for ma in range(countofmanadd):
                    try:
                        maninfo = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['type']
                    except:
                        maninfo = 'n/a'
                    if maninfo == 'PRODUCT_DETAILS':
                        count_of_origin = len(jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                                  'listingManufacturerInfo']['value']['detailedComponents'])
                        for o in range(count_of_origin):
                            try:
                                manifacture = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                    'listingManufacturerInfo']['value']['detailedComponents'][o]['value']['subTitle']
                                if manifacture == 'Manufactured by:':
                                    MANUFACTURER_ADDRESS = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                        'listingManufacturerInfo']['value']['detailedComponents'][o]['value'][
                                        'callouts'][0]
                                    MANUFACTURER_ADDRESS = str(MANUFACTURER_ADDRESS).replace("['", "").replace("']", "")
                            except:
                                MANUFACTURER_ADDRESS = 'n/a'
            except:
                MANUFACTURER_ADDRESS = 'n/a'

        if MANUFACTURER_ADDRESS == '':
            MANUFACTURER_ADDRESS = 'n/a'

        try:
            Additional_Information = 'n/a'
        except:
            Additional_Information = 'n/a'
        Manufacturer_Info = ''
        try:
            try:
                maplen = len(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'])
            except:
                maplen = 0
            mapdata = ''
            for p in range(maplen):
                mapkey = jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['key']
                mapvallen = len(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'])
                mapval = ''
                for r in range(mapvallen):
                    if mapvallen != 1:
                        mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r]) + ' || '
                    else:
                        mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r])
                mapdata = mapdata + str(mapkey) + ' : ' + str(mapval) + ' || '
            try:
                detaillen = len(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'])
            except:
                detaillen = 0
            detaildata = ''
            for q in range(detaillen):
                detailkey = jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['subTitle']
                detailvallen = len(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'])
                detailval = ''
                for r in range(detailvallen):
                    if detailvallen != 1:
                        detailval = detailval + str(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r]) + ' || '
                    else:
                        detailval = detailval + str(jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r])
                title = jsondata['pageDataV4']['page']['data']['10005'][4]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['title']
                detaildata = detaildata + str(title) + ' || ' + str(detailkey) + str(detailval)

            Manufacturer_Info = str(mapdata) + str(detaildata)
            Manufacturer_Info = Manufacturer_Info.replace("\'","")

        except:
            Manufacturer_Info = 'n/a'

        if Manufacturer_Info == 'n/a':
            try:
                try:
                    maplen = len(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'])
                except:
                    maplen = 0
                mapdata = ''
                for p in range(maplen):
                    mapkey = jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['key']
                    mapvallen = len(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'])
                    mapval = ''
                    for r in range(mapvallen):
                        if mapvallen != 1:
                            mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r]) + ' || '
                        else:
                            mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r])
                    mapdata = mapdata + str(mapkey) + ' : ' + str(mapval) + ' || '
                try:
                    detaillen = len(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'])
                except:
                    detaillen = 0
                detaildata = ''
                for q in range(detaillen):
                    detailkey = jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['subTitle']
                    detailvallen = len(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'])
                    detailval = ''
                    for r in range(detailvallen):
                        if detailvallen != 1:
                            detailval = detailval + str(jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r]) + ' || '
                        else:
                            detailval = detailval + str(
                                jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r])
                    title = jsondata['pageDataV4']['page']['data']['10005'][3]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['title']
                    detaildata = detaildata + str(title) + ' || ' + str(detailkey) + str(detailval)

                Manufacturer_Info = str(mapdata) + str(detaildata)
                Manufacturer_Info = Manufacturer_Info.replace("\'", "")

            except:
                Manufacturer_Info = 'n/a'

        if Manufacturer_Info == 'n/a':
            try:
                try:
                    maplen = len(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'])
                except:
                    maplen = 0
                mapdata = ''
                for p in range(maplen):
                    mapkey = jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['key']
                    mapvallen = len(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'])
                    mapval = ''
                    for r in range(mapvallen):
                        if mapvallen != 1:
                            mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r]) + ' || '
                        else:
                            mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r])
                    mapdata = mapdata + str(mapkey) + ' : ' + str(mapval) + ' || '
                try:
                    detaillen = len(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'])
                except:
                    detaillen = 0
                detaildata = ''
                for q in range(detaillen):
                    detailkey = jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['subTitle']
                    detailvallen = len(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'])
                    detailval = ''
                    for r in range(detailvallen):
                        if detailvallen != 1:
                            detailval = detailval + str(jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r]) + ' || '
                        else:
                            detailval = detailval + str(
                                jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r])
                    title = jsondata['pageDataV4']['page']['data']['10005'][2]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['title']
                    detaildata = detaildata + str(title) + ' || ' + str(detailkey) + str(detailval)

                Manufacturer_Info = str(mapdata) + str(detaildata)
                Manufacturer_Info = Manufacturer_Info.replace("\'", "")

            except:
                Manufacturer_Info = 'n/a'

            if Manufacturer_Info == 'n/a':
                try:
                    try:
                        maplen = len(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'])
                    except:
                        maplen = 0
                    mapdata = ''
                    for p in range(maplen):
                        mapkey = jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['key']
                        mapvallen = len(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'])
                        mapval = ''
                        for r in range(mapvallen):
                            if mapvallen != 1:
                                mapval = mapval + str(
                                    jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r]) + ' || '
                            else:
                                mapval = mapval + str(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['mappedCards'][p]['values'][r])
                        mapdata = mapdata + str(mapkey) + ' : ' + str(mapval) + ' || '
                    try:
                        detaillen = len(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'])
                    except:
                        detaillen = 0
                    detaildata = ''
                    for q in range(detaillen):
                        detailkey = jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['subTitle']
                        detailvallen = len(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'])
                        detailval = ''
                        for r in range(detailvallen):
                            if detailvallen != 1:
                                detailval = detailval + str(
                                    jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r]) + ' || '
                            else:
                                detailval = detailval + str(jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['callouts'][r])
                        title = jsondata['pageDataV4']['page']['data']['10005'][1]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][q]['value']['title']
                        detaildata = detaildata + str(title) + ' || ' + str(detailkey) + str(detailval)

                    Manufacturer_Info = str(mapdata) + str(detaildata)
                    Manufacturer_Info = Manufacturer_Info.replace("\'", "")
                except:
                    Manufacturer_Info = 'n/a'


        try:
            Ship_By = 'n/a'
        except:
            Ship_By = 'n/a'



        try:
            Warning_Message = 'n/a'
        except:
            Warning_Message = 'n/a'

        try:
            Condition = 'n/a'
        except:
            Condition = 'n/a'

        try:
            Expiry_Date = 'n/a'
        except:
            Expiry_Date = 'n/a'
        try:
            Prescription = 'n/a'
        except:
            Prescription = 'n/a'

        try:
            Composition = 'n/a'
        except:
            Composition = 'n/a'
        try:
            Ingredients = 'n/a'
        except:
            Ingredients = 'n/a'

        BifurcationRatings = []
        try:
            BifurcationRatings1 = prodtree.xpath('//div[@class="row"]/a')[0:]
            BifurcationRatings1_count = len(BifurcationRatings1)
            for b in range(BifurcationRatings1_count):
                BifurcationRatings2 = prodtree.xpath('//div[@class="row"]/a[' + str(b + 1) + ']//text()')[0:]
                Bifratings = str(BifurcationRatings2).replace("['", "").replace("']", "").replace("', '", " === ")
                BifurcationRatings.append(Bifratings)
            BifurcationRatings = str(BifurcationRatings).replace("['", "").replace("']", "").replace("', '", " ||| ")

        except:
            BifurcationRatings = 'n/a'

        if BifurcationRatings == '[]':
            BifurcationRatings = "n/a"
        else:
            pass

        # try:
        #     Bifurcation_Review = ''
        #     stars = prodtree.xpath('//div[@class="row"]//ul[1]/li/div/span[1]/text()')[0:]
        #     review_count = prodtree.xpath('//div[@class="row"]//ul[3]/li//text()')[0:]
        #     for s in range(len(stars)):
        #         Bifurcation_Review += f'{stars[s]} === {review_count[s]} ||| '
        # except:
        #     Bifurcation_Review = 'n/a'
        Bifurcation_Review = 'n/a'

        for i in range(2):
            try:
                MainImageAltTag = prodtree.xpath('//div[@class="_3kidJX"]/div/img/@alt')[0].strip()
            except:
                MainImageAltTag = 'n/a'

        Aplus_Image = []
        try:
            Aplus_Image = prodtree.xpath('//div[@id="container"]//*[contains(text(), "Product Description")]/../../div//img/@src')[0:]
            Aplus_Data_Image = str(Aplus_Image).replace("['", "").replace("']", "").replace("', '", " ||| ").replace("[]", "n/a")
        except:
            Aplus_Data_Image = 'n/a'

        try:
            Aplus_Image_Count = len(prodtree.xpath('//div[@id="container"]//*[contains(text(), "Product Description")]/../../div//img/@src')[0:])
        except:
            Aplus_Image_Count = 'n/a'

        # try:
        #     try:
        #         Image_Review_Count1 = len(ImageReview)
        #     except:
        #         Image_Review_Count1 = 0
        #     Image_Review_Count2 = prodtree.xpath('//div[@class="_2nMSwX _1yGd2h"]/div/span/text()[2]')
        #     if Image_Review_Count2 == []:
        #         Image_Review_Count = int(Image_Review_Count1)
        #     else:
        #         Image_Review_Count2 = str(Image_Review_Count2).replace("['", "").replace("']", "")
        #         Image_Review_Count = int(Image_Review_Count1) + int(Image_Review_Count2)
        # except:
        #     Image_Review_Count = 'n/a'

        try:
            Video_Review = 'n/a'
        except:
            Video_Review = 'n/a'

        try:
            CHANNEL_Name = 'Flipkart'
        except:
            CHANNEL_Name = 'n/a'

        try:
            PLP_URL = 'n/a'
        except:
            PLP_URL = 'n/a'

        try:
            Model_ID = prodtree.xpath("//*[contains(text(),'Model Number')]/../td[2]/ul/li/text()")[0].strip()
        except:
            Model_ID = 'n/a'

        try:
            SERIES = prodtree.xpath("//*[contains(text(),'Model Name')]/../td[2]/ul/li/text()")[0].strip()
        except:
            SERIES = 'n/a'

        try:
            META_ALTTAG = 'n/a'
        except:
            META_ALTTAG = 'n/a'

        try:
            DOCUMENTS = 'n/a'
        except:
            DOCUMENTS = 'n/a'

        try:
            Size_chart = 'n/a'
        except:
            Size_chart = 'n/a'

        try:
            REGULAR_OFFERS = 'n/a'
        except:
            REGULAR_OFFERS = 'n/a'

        try:
            Noofinstock = 'n/a'
        except:
            Noofinstock = 'n/a'

        try:
            DELIVERY_DETAILS = prodtree.xpath('//ul[@class="eWlq4L"]/div/div//text()')
            DELIVERY_DETAILS = str(DELIVERY_DETAILS).replace("['", "").replace("']", "").replace("', '", " ")
            DELIVERY_DETAILS = str(DELIVERY_DETAILS).split("?")[0]
        except:
            DELIVERY_DETAILS = 'n/a'
        if DELIVERY_DETAILS == '[]':
            DELIVERY_DETAILS = "n/a"

        try:
            REPLACEMENT_DETAILS = 'n/a'
        except:
            REPLACEMENT_DETAILS = 'n/a'

        try:
            COUNTRY_OF_MANUFACTURER = 'n/a'
        except:
            COUNTRY_OF_MANUFACTURER = 'n/a'

        IMPORTER_ADDRESS = ''
        try:
            try:
                countofmanadd = len(jsondata['pageDataV4']['page']['data']['10005'])
            except:
                countofmanadd = 0
            for ma in range(countofmanadd):
                try:
                    maninfo = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['type']
                except:
                    maninfo = 'n/a'
                if maninfo == 'PRODUCT_SPECIFICATION':
                    count_of_origin = len(
                        jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo'][
                            'value']['detailedComponents'])
                    for im in range(count_of_origin):
                        try:
                            imposter = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data'][
                                'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['subTitle']
                            if imposter == "Imported by:":
                                IMPORTER_ADDRESS = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][im]['value']['callouts'][0]
                                IMPORTER_ADDRESS = str(IMPORTER_ADDRESS).replace("['", "").replace("']", "")
                        except:
                            IMPORTER_ADDRESS = 'n/a'
        except:
            IMPORTER_ADDRESS = 'n/a'

        if IMPORTER_ADDRESS == '':
            try:
                try:
                    countofmanadd = len(jsondata['pageDataV4']['page']['data']['10006'])
                except:
                    countofmanadd = 0
                for ma in range(countofmanadd):
                    try:
                        maninfo = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['type']
                    except:
                        maninfo = 'n/a'
                    if maninfo == 'PRODUCT_DETAILS':
                        count_of_origin = len(
                            jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data']['listingManufacturerInfo'][
                                'value']['detailedComponents'])
                        for im in range(count_of_origin):
                            try:
                                imposter = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                    'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['subTitle']
                                if imposter == "Imported by:":
                                    IMPORTER_ADDRESS = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data']['listingManufacturerInfo']['value']['detailedComponents'][im]['value']['callouts'][0]
                                    IMPORTER_ADDRESS = str(IMPORTER_ADDRESS).replace("['", "").replace("']", "")
                            except:
                                IMPORTER_ADDRESS = 'n/a'
            except:
                IMPORTER_ADDRESS = 'n/a'

        if IMPORTER_ADDRESS == '':
            IMPORTER_ADDRESS = 'n/a'

        #MARKETER_ADDRESS
        PACKER_ADDRESS = ''
        try:
            try:
                countofmanadd = len(jsondata['pageDataV4']['page']['data']['10005'])
            except:
                countofmanadd = 0
            for ma in range(countofmanadd):
                try:
                    maninfo = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['type']
                except:
                    maninfo = 'n/a'
                if maninfo == 'PRODUCT_SPECIFICATION':
                    count_of_origin = len(
                        jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data']['listingManufacturerInfo'][
                            'value']['detailedComponents'])
                    for im in range(count_of_origin):
                        try:
                            marketer = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data'][
                                'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['subTitle']
                            if marketer == "Packed by:":
                                PACKER_ADDRESS = jsondata['pageDataV4']['page']['data']['10005'][ma]['widget']['data'][
                                    'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['callouts'][0]
                                PACKER_ADDRESS = str(PACKER_ADDRESS).replace("['", "").replace("']", "")
                        except:
                            PACKER_ADDRESS = 'n/a'
        except:
            PACKER_ADDRESS = 'n/a'

        if PACKER_ADDRESS == '':
            try:
                try:
                    countofmanadd = len(jsondata['pageDataV4']['page']['data']['10006'])
                except:
                    countofmanadd = 0
                for ma in range(countofmanadd):
                    try:
                        maninfo = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['type']
                    except:
                        maninfo = 'n/a'
                    if maninfo == 'PRODUCT_DETAILS':
                        count_of_origin = len(
                            jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data']['listingManufacturerInfo'][
                                'value']['detailedComponents'])
                        for im in range(count_of_origin):
                            try:
                                marketer = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                    'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['subTitle']
                                if marketer == "Packed by:":
                                    PACKER_ADDRESS = jsondata['pageDataV4']['page']['data']['10006'][ma]['widget']['data'][
                                        'listingManufacturerInfo']['value']['detailedComponents'][im]['value']['callouts'][0]
                                    PACKER_ADDRESS = str(PACKER_ADDRESS).replace("['", "").replace("']", "")
                            except:
                                PACKER_ADDRESS = 'n/a'
            except:
                PACKER_ADDRESS = 'n/a'

        if PACKER_ADDRESS == '':
            PACKER_ADDRESS = 'n/a'

        try:
            PRODUCT_WARRANTY1 = prodtree.xpath('//div[@class="_1UdlE-"]/div/text()')[0].strip()
            if PRODUCT_WARRANTY1 == 'Warranty':
                PRODUCT_WARRANTY = prodtree.xpath('//div[@class="_1UdlE-"]/div[2]/div/text()')[0].strip()
            else:
                PRODUCT_WARRANTY = 'n/a'
        except:
            PRODUCT_WARRANTY = 'n/a'
        try:
            RETURN_DETAILS = 'n/a'
        except:
            RETURN_DETAILS = 'n/a'

        try:
            MARKETER_ADDRESS = 'n/a'
        except:
            MARKETER_ADDRESS = 'n/a'

        try:
            FAQS = 'n/a'
        except:
            FAQS = 'n/a'

        SPECIFICATION1 = 'n/a'
        SPECIFICATION2 = 'n/a'
        SPECIFICATION3 = 'n/a'
        SPECIFICATION4 = 'n/a'
        SPECIFICATION5 = 'n/a'
        SPECIFICATION6 = 'n/a'
        SPECIFICATION7 = 'n/a'
        SPECIFICATION8 = 'n/a'
        SPECIFICATION9 = 'n/a'
        SPECIFICATION10 = 'n/a'
        IMAGE_URL_3D = 'n/a'


        print(Product_Name)
        print('MRP = ' + str(MRP) + '\t\t Sale Price = ' + str(Sale_Price))
        print('URL Crawled\n')

        date_format = '%Y-%m-%d %I:%M:%S:%Z'
        date = datetime.now(tz=utc)
        date = date.astimezone(timezone('Asia/Kolkata'))
        TimeStamp = date.strftime(date_format)


        # record = [CHANNEL_Name, SKU_ID, Product_ID, PLP_URL, Product_URL, Canonical_URL, Breadcrumb, Category,
        #           Condition, Brand, Product_Name, Model_ID, SERIES, Meta_Title, META_ALTTAG, Meta_Description,
        #           All_Image_URL, Image_URL_Count, alt_tag_presence, image_alt_tag, image_360, Video_URL, VIDEOS_COUNT, Description, Features_Highlights, KEY_FEATURES_COUNT,
        #           Aplus_Content, A_CONTENT_COUNT, Aplus_Data_Image, Aplus_Image_Count, User_Manual, DOCUMENTS, Size_chart, Schemaorg,
        #           Additional_Information, EAN, UPC, MRP, Sale_Price, Discount_Price, Discount_Percentage,
        #           Ratings, numberofrating, BifurcationRatings, Top_Reviews, Reviews,
        #           Bifurcation_Review, Image_Review, Tag, REGULAR_OFFERS, Offers_Promotion,
        #           Availability, Availability_Messages, Noofinstock, In_Cart_Status,
        #           Sold_By, Seller_Info, Ship_By, Shipping_Detail, DELIVERY_DETAILS, REPLACEMENT_DETAILS,
        #           RETURN_DETAILS, Country_of_origin, COUNTRY_OF_MANUFACTURER, MANUFACTURER_ADDRESS, IMPORTER_ADDRESS,
        #           PACKER_ADDRESS, MARKETER_ADDRESS, PRODUCT_WARRANTY, Pin_Code, FAQS, Customer_QA, Variant_URL, Discalimer, Specification_1,
        #           SPECIFICATION1, SPECIFICATION2, SPECIFICATION3, SPECIFICATION4, SPECIFICATION5, SPECIFICATION6,
        #           SPECIFICATION7, SPECIFICATION8, SPECIFICATION9, SPECIFICATION10, TimeStamp, pagestatus]

        record = [CHANNEL_Name, SKU_ID, Product_ID, PLP_URL, Product_URL, Canonical_URL, Breadcrumb, Category,
                  Condition, Product_Name, Brand, Model_ID, SERIES,Meta_Title,META_ALTTAG,Meta_Description,
                  All_Image_URL, Image_URL_Count, Video_URL,VIDEOS_COUNT,Description,Features_Highlights,KEY_FEATURES_COUNT,
                  Aplus_Content,A_CONTENT_COUNT,Aplus_Data_Image,Aplus_Image_Count,User_Manual,DOCUMENTS,Size_chart,Schemaorg,
                  Additional_Information,EAN,UPC,MRP,Sale_Price,Discount_Price, Discount_Percentage,
                  Ratings,numberofrating,BifurcationRatings,Top_Reviews,Reviews,
                  Bifurcation_Review,Image_Review,Tag,REGULAR_OFFERS,Offers_Promotion,Availability,
                  Availability_Messages,Noofinstock,In_Cart_Status,
                  Sold_By,Seller_Info,Ship_By,Shipping_Detail,DELIVERY_DETAILS,REPLACEMENT_DETAILS,
                  RETURN_DETAILS,Country_of_origin,COUNTRY_OF_MANUFACTURER, MANUFACTURER_ADDRESS,IMPORTER_ADDRESS,
                  MARKETER_ADDRESS,PACKER_ADDRESS,PRODUCT_WARRANTY,Pin_Code,FAQS,Customer_QA, Variant_URL,Discalimer,Specification_1,
                  SPECIFICATION1,SPECIFICATION2,SPECIFICATION3,SPECIFICATION4,SPECIFICATION5,
                  SPECIFICATION6,SPECIFICATION7,SPECIFICATION8,SPECIFICATION9,SPECIFICATION10,IMAGE_URL_3D,image_360,image_alt_tag,
                  TimeStamp, pagestatus]

        # for h in range(len(header1)):
        #
        #     header2 = header1[h]
        #     record.append(header2)
        for z in range(len(record)):
            record[z] = str(record[z]).replace('\n', '').replace('\t', '').replace('\r', '')
            if record[z].strip() == "":
                record[z] = 'n/a'
            record[z] = str(record[z]) + '\t'
        record.append(input1)
        with open(r".\Flipkart_P4_Output "  + str(crawled_date) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
             fp.writelines(record)
    except Exception as e:
        print(str(e))


###################################################################################################
############################## P4_Flipkart(Mobile)'s Script Caller ###############################################
###################################################################################################
crawled_date = date.today()
f = open(r".\input.txt")
line = f.readlines()
produrl = list(map(lambda v: v.split('\t')[1], line[1:]))
SKU_ID = list(map(lambda v: v.split('\t')[2], line[1:]))
linecount = len(line)


header = line[0]
header1 = str(header).replace("\n", "").split("\t")

# row = ['CHANNEL NAME', 'SKU', 'PRODUCT ID', 'PLP URL', 'PDP URL', 'CANONICAL URL', 'TAXONOMY',
#        'CATEGORY NAME',
#        'PRODUCT CONDITION', 'BRAND', 'TITLE', 'MODEL', 'SERIES', 'META TITLE', 'META ALTTAG',
#        'META DESCRIPTION',
#        'IMAGE URLS', 'IMAGES COUNT', 'PRESENCE OF ALT IMAGE TAG', 'IMAGE ALT TAG', '360 Images', 'VIDEO URLS', 'VIDEOS COUNT', 'DESCRIPTION', 'KEY FEATURES',
#        'KEY FEATURES COUNT',
#        'A+ CONTENT', 'A+ CONTENT COUNT', 'A+ CONTENT IMAGE', 'A+ CONTENT IMAGE COUNT', 'USER MANUAL',
#        'DOCUMENTS IF ANY', 'SIZE CHART', 'SCHEMA COMPLIANT?',
#        'ADDITIONAL INFORMATION', 'EAN', 'UPC', 'MRP', 'SELLING PRICE', 'DISCOUNT PRICE', 'DISCOUNT PERCENTAGE',
#        'AVG. STAR RATINGS', 'NUMBER OF RATINGS', 'RATINGS BIFURCATED BY FEATURES', 'REVIEWS',
#        'NUMBER OF REVIEWS',
#        'REVIEWS BIFURCATED BY FEATURES', 'CUSTOMER REVIEW IMAGES', 'SPECIAL TAGS', 'REGULAR OFFERS',
#        'BANK OFFERS',
#        'STOCK AVAILABILITY', 'STOCK AVAILABILITY DETAILS', 'NUMBER OF UNITS AVAILABLE (STOCK)',
#        'SHOPPING CART ACTIVE?',
#        'SOLD BY', 'SELLER DETAILS', 'SHIP BY', 'SHIPPING DETAILS', 'DELIVERY DETAILS', 'REPLACEMENT DETAILS',
#        'RETURN DETAILS', 'COUNTRY OF ORIGIN', 'COUNTRY OF MANUFACTURER', 'MANUFACTURER ADDRESS',
#        'IMPORTER ADDRESS',
#        'PACKER ADDRESS', 'MARKETER ADDRESS', 'PRODUCT WARRANTY', 'PIN CODE', 'FAQS', 'Q&A', 'VARIANT URLS',
#        'DISCALIMER', 'ALL SPECIFICATION',
#        'SPECIFICATION 1', 'SPECIFICATION 2', 'SPECIFICATION 3', 'SPECIFICATION 4', 'SPECIFICATION 5',
#        'SPECIFICATION 6',
#        'SPECIFICATION 7', 'SPECIFICATION 8', 'SPECIFICATION 9', 'SPECIFICATION 10', 'TIMESTAMP', 'PAGE_STATUS', ]
row = ["CHANNEL NAME","SKU","PRODUCT ID","PLP URL","PDP URL","CANONICAL URL","TAXONOMY","CATEGORY NAME","PRODUCT CONDITION","TITLE",
       "BRAND","MODEL","SERIES","META TITLE","META ALTTAG","META DESCRIPTION","IMAGE URLS","IMAGES COUNT","VIDEO URLS","VIDEOS COUNT",
       "DESCRIPTION","KEY FEATURES","KEY FEATURES COUNT","A+ CONTENT","A+ CONTENT COUNT","A+ CONTENT IMAGE","A+ CONTENT IMAGE COUNT",
       "USER MANUAL","DOCUMENTS IF ANY","SIZE CHART","SCHEMA COMPLIANT?","ADDITIONAL INFORMATION","EAN","UPC","MRP","SELLING PRICE",
       "DISCOUNT PRICE","DISCOUNT PERCENTAGE","AVG. STAR RATINGS","NUMBER OF RATINGS","RATINGS BIFURCATED BY FEATURES","REVIEWS",
       "NUMBER OF REVIEWS","REVIEWS BIFURCATED BY FEATURES","CUSTOMER REVIEW IMAGES","SPECIAL TAGS","REGULAR OFFERS","BANK OFFERS",
       "STOCK AVAILABILITY","STOCK AVAILABILITY DETAILS","NUMBER OF UNITS AVAILABLE (STOCK)","SHOPPING CART ACTIVE?","SOLD BY","SELLER DETAILS",
       "SHIP BY","SHIPPING DETAILS","DELIVERY DETAILS","REPLACEMENT DETAILS","RETURN DETAILS","COUNTRY OF ORIGIN","COUNTRY OF MANUFACTURER",
       "MANUFACTURER ADDRESS","IMPORTER ADDRESS","MARKETER ADDRESS","PACKER ADDRESS","PRODUCT WARRANTY","PIN CODE","FAQS","Q&A","VARIANT URLS",
       "DISCALIMER","ALL SPECIFICATION","SPECIFICATION 1","SPECIFICATION 2","SPECIFICATION 3","SPECIFICATION 4","SPECIFICATION 5",
       "SPECIFICATION 6","SPECIFICATION 7","SPECIFICATION 8","SPECIFICATION 9","SPECIFICATION 10","3D IMAGE URL","360° IMAGE URL",
       "IMAGE ALT TAGS","TIMESTAMP", "PAGE_STATUS" ]
for h in range(len(header1)):
    header2 = header1[h]
    row.append(header2)
for z in range(len(row)):
    row[z] = str(row[z]) + '\t'
row.append('\n')
with open(r".\Flipkart_P4_Output "  + str(crawled_date) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
# with open(r"D:\OneDrive - CONTEXIO LLP\Desktop\Flipkart_FSN_Output1 " + str(crawled_date) + '.txt', 'a+',newline='', encoding="utf-8") as fp:
    fp.writelines(row)
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(productcrawl, produrl, SKU_ID,  line[1:])

print('Done')