import datetime
import random
import time
import requests
from lxml import html
import pandas as pd
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
from urllib.parse import urlencode
clean = re.compile('P.*?"videos":')
clean1 = re.compile(',"lazy.*?;')
clean2 = re.compile('A.trigger.*?]')
clean3 = re.compile('<.*?>')
rev_clean = re.compile('.*?,')
rat_clean = re.compile(',*?.')

num = input("Input No. = ")

def proxyselector():
    proxy_list = [

    ]
    return random.choice(proxy_list)
API_KEY = ''
NUM_RETRIES = 3
NUM_THREADS = 1
def useragentselector():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 ',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',

        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',


    ]
    return random.choice(user_agent)

#def productcrawl(produrl):
def productcrawl(produrl,articalcode,channel,channelid):
    def get_scraperapi_url(produrl):
        """
            Converts url into API request for ScraperAPI.
        """
        payload = {'api_key': API_KEY, 'url': produrl}
        proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
        return proxy_url
   # proxies = proxyselector()
    useragent = useragentselector()
    # articalcode = 'B07N1KZZQW'
    produrl1 = 'https://www.amazon.in/ask/questions/asin/'+str(articalcode) + '/ref=ask_dp_dpmw_ql_hza?isAnswered=true'
    produrl2 = 'https://www.amazon.in/product-reviews/'+str(articalcode)+'/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

    headers = {
        'authority': 'www.amazon.in',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,mr;q=0.8',
        #'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'user-Agent': useragent,
    }

    #for i in range(2):
        # try:
        #     sleeptime = random.randint(2, 3)
        #     time.sleep(sleeptime)
        #     resp = requests.get(produrl, headers=headers, timeout=30) #proxies=proxies
        #     if resp.status_code == 200:
        #         break
        # except Exception as e:
        #     print(str(e))
        #     if i > 0:
        #         return produrl + ' ^^ ' + str(e), 'Error'
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    prefs = {'profile.default_content_setting_values': {'images': 2}}
    chrome_options.add_experimental_option('prefs', prefs)
    # chrome_options.add_argument("--headless")


    chrome_options1 = Options()
    chrome_options1.add_argument("--incognito")
    chrome_options1.add_argument("--headless")


    chrome_options2 = Options()
    chrome_options2.add_argument("--incognito")
    chrome_options2.add_argument("--headless")

    instance_driver = r"C:\Users\Administrator\Desktop\chromedriver.exe"
    local_driver  = r"D:\chromedriver.exe"
    s = Service(local_driver)
    s1 = Service(local_driver)
    s2 = Service(local_driver)

    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(get_scraperapi_url(produrl))
    time.sleep(1)
    try:

        # elementAplus = driver.find_element(By.XPATH, '//*[@id="aplus"]')
        # driver.execute_script("return arguments[0].scrollIntoView();", elementAplus)
        # time.sleep(2)

        scroll_amount = 100
        page_height = driver.execute_script("return document.body.scrollHeight")

        while scroll_amount < 1200:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(1)
            scroll_amount += 100 # Adjust this value as needed
            # wait = WebDriverWait(driver, 2)
            # wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "img")))


    except:
        pass
    # driver.refresh()
    # time.sleep(2)
    resp = driver.page_source


    driver1 = webdriver.Chrome(service=s1, options=chrome_options1)
    driver1.get(get_scraperapi_url(produrl1))
    time.sleep(1)
    # driver1.refresh()
    # time.sleep(1)
    resp1 = driver1.page_source


    driver2 = webdriver.Chrome(service=s2, options=chrome_options2)
    driver2.get(get_scraperapi_url(produrl2))
    time.sleep(1)
    # driver2.refresh()
    # time.sleep(1)
    resp2 = driver2.page_source



    try:
        prodtree = html.fromstring(resp)
        prodtree1 = html.fromstring(resp1)
        prodtreeRev = html.fromstring(resp2)

        try:
            partjson = prodtree.xpath('//*[@id="ajaxBlockComponents_feature_div"]/script[@type="text/javascript"]/text()')[0]
            partjson = partjson.split("parseJSON('")[1].split("');")[0]

            partjson = json.loads(partjson)
        except:
            partjson ={}

        #New added for high res images
        try:
            JSONDATA = prodtree.xpath('//*[@id="imageBlock_feature_div"]/script[1]/text()')[0].split('var data =')[1].split("'colorToAsin': {'initial': {}}")[0].replace('\n','').replace("                ","").replace('\'','"').strip()[:-1] + '}'
        except:
            JSONDATA = 'n/a'

        try:
            data = json.loads(JSONDATA)
        except:
            data = 'n/a'
        #end

        ###################for offers########################
        try:
            element1 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[5]/a//span')
            element1.click()
            time.sleep(1)
            prodtree0 = html.fromstring(driver.page_source)
            try:
                element2 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[3]//div/div/span/span[2]/span/span/span/span[2]//span[@role="button"]')
                element2.click()
                time.sleep(1)
                prodtree1 = html.fromstring(driver.page_source)
                element3 = driver.find_element(By.XPATH,'//*[@id="a-popover-7"]/div/header/button')
                element3.click()
                time.sleep(1)
            except:
                try:
                    element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span/a')
                    element1.click()
                    time.sleep(1)
                    prodtree1 = html.fromstring(driver.page_source)
                    driver.refresh()
                except:
                    pass
            try:
                element4 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[4]/div//div/div/span/span[2]/span/span/span/span[2]/span/span[2]/../span[@role="button"]')
                element4.click()
                time.sleep(1)
                prodtree2 = html.fromstring(driver.page_source)
                element5 = driver.find_element(By.XPATH,'//*[@id="a-popover-8"]/div/header/button')
                element5.click()
                time.sleep(1)
            except:
                try:
                    element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span/a')
                    element2.click()
                    time.sleep(1)
                    prodtree2 = html.fromstring(driver.page_source)
                    driver.refresh()
                except:
                    pass
        except:
            try:
                try:
                    element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span/a')
                    element1.click()
                except:
                    element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span')
                    element1.click()
                time.sleep(1)
                prodtree1 = html.fromstring(driver.page_source)
                driver.refresh()
            except:
                pass
            try:
                try:
                    element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span/a')
                    element2.click()
                except:
                    element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span')
                    element2.click()
                time.sleep(1)
                prodtree2 = html.fromstring(driver.page_source)
                driver.refresh()
            except:
                pass

        ######################################################

        # htmlelement = driver.find_element_by_tag_name('html')
        # # # Scrolls down to the bottom of the page
        # htmlelement.send_keys(Keys.END)
        # #htmlelement.send_keys(Keys.HOME)

        # Get the xpath of a certain word on webpage
        element = driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]')
        # Scroll to where the xpath is in
        driver.execute_script("return arguments[0].scrollIntoView();", element)
        # try:
        #     element1 = driver.find_element(By.XPATH, '//div[@data-mediatype="IMAGE"]//a[@class="a-link-emphasis"]')
        #     element1.click()
        #     reviewImagesRes = html.fromstring(driver.page_source)
        #     # Scroll to where the xpath is in
        # except:
        #     pass


        # time.sleep(1)



        print(produrl)
        print('Artical Code = ' + str(articalcode) + '\t\tChannel ID = '+ str(channelid))
        # print(channel)
        # print(channelid)


        try:
            MetaTitle=prodtree.xpath('//div[@id="a-page"]/title/text()')[0]
        except:
            MetaTitle='n/a'
        print(MetaTitle)

        try:
            MetaDesc=prodtree.xpath('//div[@id="a-page"]/title/text()')[0]
        except:
            MetaDesc='n/a'
        # print(MetaDesc)

        try:
            Retailer = 'Amazon.in'

        except:
            Retailer = 'n/a'
        #print(Retailer)

        # try:
        #     Brand = prodtree.xpath('//a[@id="bylineInfo"]/text()')[0].strip()
        # except:
        #     try:
        #         Brand = prodtree.xpath('//div[@id="bylineInfo"]/span/a/text()')[0].strip()
        #         Brand = str('Brand: ' + Brand)
        #     except:
        #         Brand = 'n/a'
        # print(Brand)

        try:
            try:
                Brand = prodtree.xpath('//*[@id="productOverview_feature_div"]/div/table//tr[@class="a-spacing-small po-brand"]/td[2]/span/text()')[0].strip().replace('‎','').replace('Brand:','')
            except:
                Brand = ''
            if Brand == "":
                try:
                    Brand = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr[1]/td/text()')[0].strip().replace('&lrm;', '').replace('‎','').replace('Brand:','')
                except:
                    Brand = ''
            if Brand == "":
                try:
                    Brand = prodtree.xpath('//*[@id="poExpander"]/div[1]/div/table//tr[contains(text(), "brand")]/td//span//text()')
                    Brand =str(Brand).replace('&lrm;', '').replace('‎','').replace('Brand:','').replace('Brand','').replace("[","").replace(']','').replace("'",'').replace(",","").strip()
                except:
                    Brand = ''
            if Brand == "":
                try:
                    Brand = prodtree.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
                except:
                    Brand = 'n/a'

            Brand = str(Brand).replace('Visit the ','').replace('Store','').strip()
        except:
            Brand = 'n/a'

        #print(Brand)


        try:
            ProductName = prodtree.xpath('//span[@id="productTitle"]/text()')[0].strip()

        except:
            ProductName = 'n/a'
        print(ProductName)

        # try:
        #     product_name_len = len(ProductName)
        # except:
        #     product_name_len = 'n/a'


        try:
            ProductPrice = prodtree.xpath('//span[@id="priceblock_ourprice"]/text()')[0].replace('₹', '')
        except:
            try:
                ProductPrice2 = prodtree.xpath('//div[@id="olp_feature_div"]/div[2]/span/a/span[2]/text()')[0].replace('₹', '')
                ProductPrice = ProductPrice2
            except:
                try:
                        ProductPrice3 = prodtree.xpath('//span[@id="priceblock_saleprice"]/text()')[0].replace('₹', '')
                        ProductPrice = ProductPrice3
                except:
                    try:
                        ProductPrice4 = prodtree.xpath('//span[@class="a-price a-text-price a-size-medium"]/span/text()')[0].replace('₹', '')
                        ProductPrice=ProductPrice4
                    except:
                        try:
                            ProductPrice5 =prodtree.xpath('//span[@id="price_inside_buybox"]/text()')[0].replace('₹', '')
                            ProductPrice = ProductPrice5
                        except:
                            try:
                                ProductPrice6 = prodtree.xpath('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()')[0].replace('₹', '')
                                ProductPrice = ProductPrice6
                            except:
                                try:
                                    ProductPrice7 = prodtree.xpath('//span[@class="a-price-whole"]/text()')[0].replace('₹', '')
                                    ProductPrice = ProductPrice7
                                except:
                                    try:
                                        ProductPrice8 = prodtree.xpath('//td[@class="a-span12"]/span[@class="a-price a-text-price a-size-medium apexPriceToPay"]/span[2]/text()')[0].replace('₹', '')
                                        ProductPrice = ProductPrice8
                                    except:
                                        ProductPrice = 'n/a'


        # print(ProductPrice)

        for i in range(2):
            try:
                RegularPrice = prodtree.xpath('//td/span[@class="priceBlockStrikePriceString a-text-strike"]/text()')[0].replace('₹', '').strip()
                #RegularPrice = str(RegularPrice).replace('₹', '')
            except:
                try:
                    RegularPrice2 = prodtree.xpath('//span[@class="a-price a-text-price a-size-base"]/span[@class="a-offscreen"]/text()')[0].replace('₹', '')
                    RegularPrice = RegularPrice2
                except:
                    try:
                        RegularPrice3 = prodtree.xpath('//div[@class="a-box-inner"]/div/div[2]/div/ul/li[2]/span/span[2]/text()')[0].replace('₹', '')
                        RegularPrice = RegularPrice3
                    except:
                        try:
                            RegularPrice4 = prodtree.xpath('//div[@class="a-section a-spacing-small aok-align-center"]/span/span/span[@class="a-price a-text-price"]/span[@class="a-offscreen"]/text()')[0].replace('₹', '')
                            RegularPrice = RegularPrice4
                        except:
                            try:
                                RegularPrice5 = prodtree.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span/span[2]')[0].replace('₹', '')
                                RegularPrice = RegularPrice5
                            except:
                                try:
                                    RegularPrice6 = prodtree.xpath('//div[@class="a-section a-spacing-small aok-align-center"]/span/span/span[@class="a-price a-text-price"]/span[1]/text()')[0].replace('₹', '')
                                    RegularPrice = RegularPrice6
                                except:
                                    try:
                                        RegularPrice7 = prodtree.xpath('//div[@class="a-section a-spacing-small aok-align-center"]/span/span/span[@class="a-price a-text-price"]/span[2]')[0].replace('₹', '')
                                        RegularPrice = RegularPrice7
                                    except:
                                        RegularPrice = 'n/a'


        print('MRP = ' + str(RegularPrice) + '\t\tSale price = '+ str(ProductPrice))

        try:
            Shipping=prodtree.xpath('//div[@id = "ddmDeliveryMessage"]/a/text()')[0].strip()
            ShippingDetails = prodtree.xpath('//div[@id = "ddmDeliveryMessage"]/b/text()')[0].strip()
            ShippingDetails=Shipping+':'+ShippingDetails
        except:
            ShippingDetails = 'n/a'
        # print(ShippingDetails)

        try:
            Availability = prodtree.xpath('//div[@id="availability"]/span/text()')[0].strip()

        except:
            try:
                Availability = prodtree.xpath('//span[@id="availability"]/span/text()')[0].strip()

            except:
                Availability = 'n/a'
        if Availability != 'Currently unavailable.':
            Availability = 'Yes'
        else:
            Availability = 'No'



        #edited by pankaj
        # try:
        #     image = prodtree.xpath('//div[@id="altImages"]//ul//li//span//img/@src')
        #     image = str(image).replace("', '", " || ").replace("\'", "").replace('[', '').replace(']', '').replace('._SX38_SY50_CR,0,0,38,50_', '').replace('SX38_SY50_CR,0,0,38,50', '').replace('https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif','')
        # except:
        #     image = 'n/a'
        #high resolution images Edited
        try:
            high_res_count = data['colorImages']['initial']
        except:
            high_res_count = 'n/a'

        len1 = len(high_res_count)
        images = ""
        for i in range(len1):
            try:
                image = high_res_count[i]['hiRes']
                if image == None:
                    image = high_res_count[i]['large']
            except:
                image = 'n/a'
            images = images + image + " ||| "
        print(images)
        #High resolution images end of editing

        try:
            image_count =len(high_res_count)
            image_count = float(image_count)
        except:
            image_count = 'n/a'




        try:
            Style=prodtree.xpath('//div[@id="productDescription"]/div/text()')[0].strip()
            ProdDescTile = prodtree.xpath('//div[@id="productDescription"]/div/strong/text()')[0]
            ProdDesc = prodtree.xpath('//div[@id="productDescription"]/p/text()')[0]
            ProdDesc=Style+':'+ProdDescTile+'|||'+ProdDesc
            ProdDesc = str(ProdDesc).replace('[', '').replace(']', '').replace('\n', '').replace("'", "").replace(',','').replace("'",'')
        except:
            try:
                Style=prodtree.xpath('//div[@id="prodDetails"]/span/text()')[0].strip()
                ProdDesc = prodtree.xpath('//div[@id="prodDetails"]/span/strong/text()')
                ProdDesc = str(ProdDesc).replace('[', '').replace(']', '').replace('\n', '').replace("'", "").replace(',', '').replace("'", '').replace('\\n','')
                ProdDesc = Style +''+ ProdDesc
                if(ProdDesc==''):
                    try:
                        ProdDesc = prodtree.xpath('//div[@id="productDescription"]/p/text()')[0].strip()
                        ProdDesc = str(ProdDesc).replace('[', '').replace(']', '').replace('\n', '').replace("'","").replace(',', '').replace("'", '').replace('\\n', '')
                    except:
                        pass
            except:
                try:
                    ProdDesc = prodtree.xpath('//div[@id="productDescription"]/p/text()')[0].strip()
                    ProdDesc = str(ProdDesc).replace('[', '').replace(']', '').replace('\n', '').replace("'", "").replace(',', '').replace("'", '').replace('\\n', '')
                except:
                    try:
                        ProdDesc = prodtree.xpath('//div[@id="aplus"]/div/div[2]/div/p/text()').strip()
                    except:
                        ProdDesc='n/a'
        if ProdDesc == '':
            try:
                ProdDesc = prodtree.xpath('//div[@id="feature-bullets"]/ul/li/span/text()')
                ProdDesc = str(ProdDesc).replace("  ', ' ",' ||| ').replace("[\'",'').replace("']",'').replace(', " ',' ||| ').replace(", '"," ||| ").replace(" ' ","").replace(' " ','').replace('  ',' ').strip()
            except:
                pass
        # print(ProdDesc)


        try:
            ImpInfo = prodtree.xpath('//div[@id="important-information"]/div/p/text()')[0]
            ImpInfo= str(ImpInfo).replace('[', '').replace(']', '').replace('\\n', '').replace("'", "").replace(',','|||')
        except:
            try:
                ImpInfo = prodtree.xpath('//div[@id="important-information"]/div[2]/p[2]/text()')[0]
            except:
                ImpInfo='n/a'
        # print(ImpInfo)


        try:
            Highlights = prodtree.xpath('//div[@id="feature-bullets"]//ul//li//text()')
            try:
                key_features_count = len(Highlights)
                key_features_count = float(key_features_count)
            except:
                key_features_count = 0
            Highlights= str(Highlights).replace("[\' ","").replace("  ', ' "," ||| ").replace("']","").replace("['","").replace('"',"").replace(',', ' ').replace("'  '"," ||| ").strip()
        except:
            Highlights = 'n/a'
            key_features_count = 'n/a'
        # print(Highlights)


        try:
            Reviews = prodtreeRev.xpath('//*[@id="filter-info-section"]/div/text()')[0].strip()
            Review_count = Reviews.replace('total ratings,', '|').split('|')[1].strip().split(' ')[0]
            Rating_count = Reviews.replace('total ratings,', '|').split('|')[0]
        except:
            try:
                #Reviews = prodtree.xpath('//span[@id = "acrCustomerReviewText"]/text()')[0].strip()
                Reviews = prodtreeRev.xpath('//*[@id="filter-info-section"]/div/span/text()')[0].strip()
                Review_count = Reviews.replace('total ratings,', '|').split('|')[1].strip().split(' ')[0]
                Rating_count = Reviews.replace('total ratings,', '|').split('|')[0]

            except:
                try:
                    Reviews = prodtreeRev.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[3]/span/text()')[0].strip()
                    Review_count = Reviews.replace('total ratings,', '|').split('|')[1].strip().split(' ')[0]
                    Rating_count = Reviews.replace('total ratings,', '|').split('|')[0]
                except:
                    Reviews = 'n/a'
                    Review_count = 'n/a'
                    Rating_count = 'n/a'


        # print(Reviews)

        try:
            Ratings = prodtree.xpath('//span[@id="acrPopover"]/span[1]/a/i[1]/span/text()')[0].strip()
            Ratings = str(Ratings).replace('out of 5 stars', '')
        except:
            Ratings = 'n/a'


        try:
            QuestionAnswerd = prodtree.xpath('//a[@id="askATFLink"]/span/text()')[0].strip()
            QuestionAnswerd = str(QuestionAnswerd).replace('answered questions','')

        except:
            QuestionAnswerd = 'n/a'
        print('Q & A = ' + str(QuestionAnswerd))

        try:
            breadcrum = prodtree.xpath('//div[@id="wayfinding-breadcrumbs_feature_div"]//ul//li//span//a/text()')[0:]
            breadcrum = str(breadcrum).replace('[', '').replace(']', '').replace("\\n", "").lstrip().rstrip()
            breadcrum = str(breadcrum).replace(',', ' > ').replace("'", "").replace('                ', '').replace('           ','').lstrip().rstrip()

        except:
            breadcrum = 'NA'
        # print(breadcrum)

        try:
            category = prodtree.xpath('//div[@id="wayfinding-breadcrumbs_feature_div"]//ul//li//span//a/text()')[-1].replace('\n','').replace('\t','').replace('  ','')
        except:
            category = 'n/a'
        try:
            date_format = '%Y-%m-%d %H:%M:%S'
            CrawlDate = datetime.datetime.today()
            crawldate = CrawlDate.strftime(date_format)
        except:
            crawldate = 'n/a'
        # print(crawldate)

        try:
            DiscoutPrice = prodtree.xpath('//tr[@id="regularprice_savings"]/td[2]/text()')[0].replace('₹', '').strip()
        except:
            try:
                DiscoutPrice=prodtree.xpath('//tr[@id="dealprice_savings"]/td[2]/text()')[0].replace('₹', '').strip()
            except:
                try:
                    DiscoutPrice=prodtree.xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr[3]/td[2]/span[1]/span/span[2]/text()')[0].replace('₹', '').strip()
                except:
                    DiscoutPrice = 'n/a'
        print(DiscoutPrice)

        try:
            MerchantName = prodtree.xpath('//div[@id="outOfStock"]/div/div[1]//text()')[1]
            # MerchantName = str(MerchantName).replace("[\'","").replace("\']","").replace("\'","").replace(',','').replace('\\n','').replace('.','').strip()
        except:
            MerchantName = ''
        if str(MerchantName) == '':
            try:
                MerchantName = prodtree.xpath('//div[@id="merchant-info"]//text()')
                MerchantName = str(MerchantName).replace("[\'","").replace("\']","").replace("\'","").replace(',','').replace('\\n','').replace('.','').strip()
            except:
                MerchantName = ''




        # try:
        #     OffersHeads = prodtree.xpath('//span[@class="sopp-offer-title"]/text()')
        #     OffersHeadslen=len(OffersHeads)
        #     Offers=''
        #     for i in range(OffersHeadslen):
        #         OffersHead = prodtree.xpath('//span[@class="sopp-offer-title"]/text()')[i]
        #         OfferValues = prodtree.xpath('//span[@class="description"]/text()')[i]
        #         Offers=Offers+OffersHead+""+OfferValues+"|||"
        #         Offers=str(Offers).replace('[','').replace(']','').replace("'",'')
        # except:
        #     Offers = 'n/a'


        try:
            amazonchoice1 = prodtree.xpath('//div[@id="acBadge_feature_div"]/div/span[1]/span[1]/span[1]/text()')[0]
            amazonchoice2 = prodtree.xpath('//div[@id="acBadge_feature_div"]/div/span[1]/span[1]/span[2]/text()')[0]
            amazonchoice = amazonchoice1 + "" + amazonchoice2
        except:
            amazonchoice = 'n/a'


        try:
            prime = prodtree.xpath('//div[@id="olp_feature_div"]/div[2]/i')
            if (prime != ''):
                prime = 'Prime'

        except:
            prime = 'n/a'


        try:
            SellerCount = prodtree.xpath('//div[@id="olp_feature_div"]/div[2]/span/a/span[1]/text()')[0].strip(). \
                replace('New', '').replace('from', '').replace('(', '').replace(')', '')

        except:
            SellerCount = 'n/a'


        try:
            Specshead = prodtree.xpath('//table[@id="productDetails_techSpec_section_1"]//tr/th/text()')
            SpecsHeadlength=len(Specshead)
            specvalues=''
            for i in range(SpecsHeadlength):
                NewSpecsHead = prodtree.xpath('//table[@id="productDetails_techSpec_section_1"]//tr/th/text()')[i].strip()
                Specs= prodtree.xpath('//table[@id="productDetails_techSpec_section_1"]//tr/td/text()')[i]
                Specs = str(Specs).replace('\\n', '').replace('200e', '').replace('\\u', '').replace('[', '').replace("'", "").replace(']', '').strip() #.replace(',', '||')
                specvalues=specvalues+" "+NewSpecsHead+" === "+Specs+" ||| "
                specvalues=str(specvalues).replace('\n','').lstrip().replace('‎','').replace('  ','').replace('‏', '' )

            if(specvalues==''):
                NewSpecsHead = prodtree.xpath('//div[@id="detailBullets_feature_div"]/ul/li/span/span[1]/text()')
                SpecsHeadlength = len(NewSpecsHead)
                head = []
                for i in NewSpecsHead:
                    try:
                        head.append(i.strip())
                        i = str(i).strip()
                    except:
                        pass
                specvalues = ''
                for i in range(SpecsHeadlength):
                    try:
                        headvalue = head[i]
                        features = prodtree.xpath('//div[@id="detailBullets_feature_div"]/ul/li/span/span[2]/text()')
                        features = [s.replace('\n', '') for s in features]
                        features = list(filter(str.strip, features))
                        features = features[i]
                        specvalues = specvalues+ headvalue + '===' + features + '|||'
                        specvalues = str(specvalues).replace('\n', '').replace('‎','').replace('  ','').replace('‏', '' ).replace('===:','===').replace(':===','===')
                        specvalues = str(specvalues).replace('                                    â€                                        :                                    ',' = ')
                    except:
                        pass
        except:
            specvalues = 'n/a'


        try:
            headingvalue=prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr/th/text()')
            headinglen = len(headingvalue)
            head=[]
            for i in headingvalue:
                try:
                    head.append(i.strip())
                    i=str(i).strip()
                    if(i=='Best Sellers Rank'):
                        head.remove(i.strip())
                        pass
                except:
                    pass
            AdditionalDetails=''
            for i in range(headinglen):
                try:
                    headvalue=head[i]
                    features = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr/td/text()')
                    features=[s.replace('\n','') for s in features]
                    features=list(filter(str.strip,features))
                    features=features[i]
                    AdditionalDetails=AdditionalDetails+headvalue+' === '+features+'|||'
                    AdditionalDetails=str(AdditionalDetails).replace('\n','')
                    AdditionalDetails = re.sub(' +', ' ', AdditionalDetails)
                except:
                    pass
        except:
            AdditionalDetails='n/a'


        # try:
        #     ASIN = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[1]/td/text()')[0].strip()
        # except:
        #     ASIN = 'n/a'



        try:
            TYBSR = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/span/span[1]/text()')[0].strip().replace('(','')
        except:
            try:
                TYBSR =prodtree.xpath('//div[@id = "detailBulletsWrapper_feature_div"]/ul[1]/li/span/text()')[1].strip().replace('(', '')
            except:
                try:
                    TYBSR = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[2]/td/span/span[1]/text()')[0].strip().replace('(', '')
                except:
                    TYBSR = 'n/a'
        print(TYBSR)

        try:
            OTBSR1 =prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/span/span[2]/text()')[0].strip()
            OTBSR2 =prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/span/span[2]/a/text()')[0].strip()
            OTBSR=OTBSR1+' '+OTBSR2
        except:
            try:
                OTBSR1 = prodtree.xpath('//div[@id="detailBulletsWrapper_feature_div"]/ul[1]/li/span/ul/li/span/text()')[0].strip()
                OTBSR2 = prodtree.xpath('//div[@id="detailBulletsWrapper_feature_div"]/ul[1]/li/span/ul/li/span/a/text()')[0].strip()
                OTBSR = OTBSR1 + ' ' + OTBSR2
            except:
                try:
                    OTBSR1 = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[2]/td/span/span[2]/text()')[0].strip()
                    OTBSR2 = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[2]/td/span/span[2]/a/text()')[0].strip()
                    OTBSR = OTBSR1 + ' ' + OTBSR2
                except:
                    OTBSR = 'n/a'
        print(OTBSR)

        try:

            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()
            DFAlen= len(DFA)
            if(DFAlen>=16 or DFAlen<=11):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[0].strip()
                    #DFAlen = len(DFA)
                except:
                    pass
            if(DFAlen<=10 or DFAlen>=20):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[2]/td/text()')[0].strip()
                    #DFAlen = len(DFA)
                except:
                    pass
            if(DFAlen==15):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[0].strip()
                    try:
                        if (DFA == ''):
                            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()
                    except:
                        pass
                except:
                    pass
            if (DFAlen == 7):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[
                        0].strip()
                    try:
                        if (DFA == ''):
                            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()
                    except:
                        pass
                except:
                    pass
            if(DFAlen==14):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[0].strip()
                    try:
                        if (DFA == ''):
                            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()

                    except:
                        pass
                except:
                    pass
            if (DFAlen == 13):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[0].strip()
                    try:
                        if(DFA==''):
                            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()
                    except:
                        pass
                except:
                    pass
            if (DFAlen == 12):
                try:
                    DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[3]/td/text()')[0].strip()
                    try:
                        if (DFA == ''):
                            DFA = prodtree.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr[4]/td/text()')[0].strip()
                    except:
                        pass
                except:
                    pass
        except:
            DFA = 'n/a'
        print(DFA)

        try:
            star = prodtree.xpath('//table[@id="histogramTable"]//tr/td/span[1]/a/text()')
            rating = prodtree.xpath('//table[@id="histogramTable"]//tr/td/span[2]/a/text()')
            key2 = []
            for i in star:
                key2.append(i.strip())

            value2 = []
            for i in rating:
                if i == 'Learn More':
                 print()
                else:
                    value2.append(i.strip())
            #histogram = list(key2)
            histogram = dict(zip(key2,value2))
            histogram  = str(histogram).replace(",", '|||').replace("'", '').replace('\\n', '').replace(
                '[', '').replace(']', '').replace('200e', '').replace('\\u', '').replace('{', '').replace('}', '')
        except:
            histogram  = "n/a"
        print(histogram)

        try:
            try:
                brand_d = prodtree.xpath('//*[@id="aplus"]/h2//text()')[0].strip()
            except:
                brand_d = ''
            brand_data = ''
            brand_dataUniqueList = []
            try:
                brand_dataList = prodtree.xpath('//*[@id="aplus"]//img/@src')
                for aplusImage in brand_dataList:
                    if '.svg' not in aplusImage:
                        if aplusImage not in brand_dataUniqueList:
                            brand_dataUniqueList.append(aplusImage)
                            brand_data = brand_data + aplusImage + '|||'
            except:
                brand_data = ''

            if brand_data == '':
                try:
                    brand_data = prodtree.xpath('//*[@id="aplus"]//img//@data-src')
                    brand_data = str(brand_data).strip().replace('[', '').replace(']', '').replace(', ', ' ||| ').replace("'","")
                except:
                    brand_data = ''

            if brand_data == '':
                try:
                    brand_data = prodtree.xpath('//*[@id="aplus"]//img/@src')
                    brand_data = str(brand_data).strip().replace('[', '').replace(']', '').replace(', ', ' ||| ').replace("'","")
                except:
                    brand_data = ''

            if brand_data == '':
                try:
                    brand_data = prodtree.xpath('//*[contains(@id,"")]/div/div/div/div/img/@data-a-hires')
                    brand_data = str(brand_data).strip().replace('[', '').replace(']', '').replace(', ', ' ||| ').replace("'", "")
                except:
                    brand_data = ''
            try:
                brand_img_new = prodtree.xpath('//*[@id="aplus"]//img/@data-src')
                brand_img_new = str(brand_img_new).strip().replace('[', '').replace(']', '').replace(', ', ' ||| ').replace("'", "")
            except:
                brand_img_new = ''

            try:
                brand_data_img = str(brand_data).count('.jpg') + str(brand_data).count('.png') + str(brand_data).count('.jpeg')
            except:
                brand_data_img = 'n/a'
                #------------A+ images = Brand Desc----------------------------------------------
            Brand_desc = str(brand_d) + ' === ' + str(brand_data)# +' ||| '+ str(brand_img_new)
        except:
            Brand_desc = 'n/a'

        try:
            try:
                brand_data1 = prodtree.xpath('//*[@id="aplus"]/div/div/div/div[1]/div[1]/div/div[2]/p//text()')[0].strip()
            except:
                brand_data1 = ''

            if brand_data1 == '':
                try:
                    brand_data1 = prodtree.xpath('//*[@id="aplus"]//div//div//div//div//*[@class="aplus-p2"]//text()')
                    brand_data1 = str(brand_data1).replace('\\n', '').replace('[', '').replace(']', '').replace(',', '').replace("'","").replace('\\t', '').replace('  ', '').strip()
                except:
                    brand_data1 = ''

            if brand_data1 == '':
                try:
                    brand_data1 = prodtree.xpath('//*[@id="aplus"]/div/div/div/div[1]//div[1]/div/table//text()')
                    brand_data1 = str(brand_data1).replace('[','').replace(']','').replace('\\t','').replace("  ", "").replace("\\n","").replace("', '', '",":::").replace("', '"," ").strip()
                    brand_data1 = re.sub(' +', ' ', brand_data1)
                    brand_data1 = re.sub('::::+', ' ', brand_data1)
                    brand_data1 = re.sub('  +', '|||', brand_data1)

                    #brand_data1 = str(brand_data1).replace('\\n', '').strip().replace(",","").replace("'","").replace('                ','').replace('[','').replace(']','').replace('\\t','').strip()
                except:
                        brand_data1 = ''

            if brand_data1 == '':
                try:
                    brand_data1 = prodtree.xpath('//*[@id="aplus"]//div//div//div/div//div//div/div//div//text()')
                    brand_data1 = str(brand_data1).replace('\\n', '').replace('[', '').replace(']', '').replace(',', '').replace("'", "").replace('\\t','').replace('                ','').strip()
                except:
                    brand_data1 = ''

            if brand_data1 == '':
                try:
                    brand_data1 =''
                    for i in range(len(prodtree.xpath('//*[@id="aplus"]/div/div[5]/div/div/div/div/table//tr[2]/td'))):
                        brand_data1_1 = prodtree.xpath('//*[@id="aplus"]/div/div[5]/div/div/div/div/table//tr/td['+str(i+1)+']/div//text()')
                        brand_data1_1 = str(brand_data1_1).replace('[', '').replace(']', '').replace('  ','').replace('\\n','').replace("'", '').replace(',','').replace('   ',' ')
                        brand_data1_1 = re.sub(' +', ' ', brand_data1_1)
                        brand_data1= str(brand_data1) + str(brand_data1_1) + '|||'
                except:
                    brand_data1 = ''

            Brand_desc1 = str(brand_d)+' === '+str(brand_data1)
        except:
            Brand_desc1 = 'n/a'




        # try:
        #     brand_data_img = prodtree.xpath('//*[@id="aplus"]/div/div/div/img/@data-src')
        #     brand_data_img = str(len(brand_data_img))
        # except:
        #     brand_data_img = ''
        #
        # if brand_data_img == '0':
        #     try:
        #         brand_data_img = prodtree.xpath('//*[@id="aplus"]/div/div/div/div/div/div//div//img//@data-src')
        #         brand_data_img = str(len(brand_data_img))
        #     except:
        #         brand_data_img = ''
        #
        # if brand_data_img == '0':
        #     try:
        #         brand_data_img = prodtree.xpath('//*[@id="aplus"]/div/div//div//div//div//img/@src')
        #         brand_data_img = str(len(brand_data_img))
        #     except:
        #         brand_data_img = ''
        #
        # if brand_data_img == '0':
        #     try:
        #         brand_data_img = prodtree.xpath('//*[contains(@id,"")]/div/div/div/div/img/@data-a-hires')
        #         brand_data_img = str(len(brand_data_img))
        #     except:
        #         brand_data_img = ''

        # try:
        #     brand_data_new_img = len(prodtree.xpath('//*[@id="aplus"]/div/div[5]/div/div/div/div/table//tr[1]//img/@data-src'))
        # except:
        #     brand_data_new_img = 0
        #
        # brand_data_img = int(brand_data_img) + int(brand_data_new_img)


        try:
            canonical_url = prodtree.xpath('//link[@rel="canonical"]/@href')[0].strip()
        except:
            canonical_url = 'n/a'

        try:
            main_image = high_res_count[0]['hiRes']
            if main_image == None:
                main_image = high_res_count[0]['large']
        except:
            main_image = 'n/a'
        main_image_alt = ""
        try:
            main_image_altList = prodtree.xpath('//div[@id="imageBlock"]//img/@alt')
            for alttag in main_image_altList:
                main_image_alt = main_image_alt + alttag + '|||'

        except:
            main_image_alt = 'n/a'





        try:
            in_box = prodtree.xpath('//*[@id="whatsInTheBoxDeck"]//text()')
            in_box = str(in_box).replace("'",'').replace('[','').replace(']','').replace(',  ',' ')
        except:
            in_box = 'n/a'

        try:
            review_imageList = prodtreeRev.xpath('//div[@class="a-section a-spacing-medium review-image-container"]//img/@src')
            review_image = str(review_imageList).replace('[', '').replace(']', '').replace("',", " ||| ").replace("'","")
        except:
            review_imageList = ['n/a']
            review_image = 'n/a'

        try:
            review_image_count = len(review_imageList)

        except:
            review_image_count = 'n/a'

        try:
            qNa_len = prodtree1.xpath('//*[contains(@id,"question-")]/div/div/a/span/text()')
            c = len(qNa_len)
            qsts=[]
            answ=[]
            qNa=""
            for qn in range(c):
                qst = prodtree1.xpath('//*[contains(@id,"question-")]/div/div/a/span/text()')[qn].strip()
                qsts.append(qst)
                ans = prodtree1.xpath('//div[@class="a-fixed-left-grid-col a-col-right"]//div[@class="a-fixed-left-grid a-spacing-base"]/div/div[2]/span/text()')[qn].strip()
                answ.append(ans)

            for i in range(c):
                qa = str(i) +' ::: '+qsts[i]+' === '+answ[i]
                qNa = qNa + qa + ' ||| '

            qNa = str(qNa)
        except:
            qNa = 'n/a'



        try:
            prod_desc = prodtree.xpath('//*[@id="productDescription"]/p/span//text()')
            prod_desc = str(prod_desc).replace('[','').replace(']','').replace("\'","").replace(',','').replace('\\xa0','').replace('"','').strip()
            prod_desc =  re.sub(clean3, '',prod_desc)
        except:
            prod_desc = 'n/a'

        try:
            prod_desc_len = len(prod_desc)
        except:
            prod_desc_len = 'n/a'

        try:
            techdet = []
            tech_hed =[]
            tech_val = []
            techdet_hed_len = prodtree.xpath('//*[@id="tech"]/div[3]/div/div/div/table//tr/td[1]/p')
            #techdet_hed_len = prodtree.xpath('// div[@class ="content-grid-row-wrapper "]/div/div/div//table//tbody//tr')
            techdet_hed_len = len(techdet_hed_len)
            for i in range(techdet_hed_len):
                hed = prodtree.xpath('//*[@id="tech"]/div[3]/div/div/div/table//tr/td[1]/p//text()')[i].strip()
                val = prodtree.xpath('//*[@id="tech"]/div[3]/div/div/div/table//tr/td[2]/p//text()')[i].strip()
                tech_hed.append(hed)
                tech_val.append(val)

            for i in range(techdet_hed_len):
                keyval = tech_hed[i]+ " === " +tech_val[i]
                techdet.append(keyval +' ||| ')

            techdet = str(techdet)
        except:
            techdet = 'n/a'
        try:
            user_manual = prodtree.xpath('//*[@id="productDocuments_feature_div"]//a/@href')[0]
        except:
            user_manual = 'n/a'
        Doc = ""
        try:
            Doc_if_any = prodtree.xpath('//*[@id="productDocuments_feature_div"]//a/@href')
            for doc in Doc_if_any:
                Doc = Doc + doc + ' ||| '
        except:
            Doc = 'n/a'



        upc = 'n/a'

        try:
            rev1 = prodtree.xpath('//*[contains(@id,"customer_review-")]/div[2]/a[2]/span//text()')
            rev2 = prodtree.xpath(' //*[contains(@id,"customer_review-")]/div[4]/span/div/div[1]/span//text()[1]')
            top_rev = ""
            for i in range(len(rev1)):
                try:
                    rev1H = rev1[i]
                except:
                    rev1H = ''
                try:
                    rev2H = rev2[i]
                except:
                    rev2H = ''
                a = rev1H+' === '+rev2H
                top_rev = top_rev + a  + ' ||| '
            top_rev = str(top_rev).replace('[','').replace(']','').replace("'","").replace(",","").replace("\xa0", ' ')

        except:
            top_rev = ''

        if top_rev == '':
            try:
                rev1 = prodtreeRev.xpath('//div[@id="cm_cr-review_list"]/div[@data-hook="review"]//*[contains(@id,"customer_review")]//a[@data-hook="review-title"]/span[2]/text()')
                rev2 = prodtreeRev.xpath('//div[@id="cm_cr-review_list"]/div[@data-hook="review"]//*[contains(@id,"customer_review")]//span[@data-hook="review-body"]/span/text()')
                top_rev = ""
                for i in range(len(rev1)):
                    try:
                        rev1H = rev1[i]
                    except:
                        rev1H = ''
                    try:
                        rev2H = prodtreeRev.xpath('//div[@id="cm_cr-review_list"]/div[@data-hook="review"]['+str(i+1) +']//*[contains(@id,"customer_review")]//span[@data-hook="review-body"]/span/text()')
                        rev2H = ('').join(rev2H)
                    except:
                        rev2H = ''
                    a = rev1H + ' === ' + rev2H
                    top_rev = top_rev + a + ' ||| '
                top_rev = str(top_rev).replace('[', '').replace(']', '').replace("'", "").replace(",", "").replace("\xa0",' ')
            except:
                top_rev = 'n/a'

        try:
            short_desc = []
            tr = prodtree.xpath('//table[@class="a-normal a-spacing-micro"]//tr')
            len1 = len(tr)
            for p in range(1, len1 + 1):
                xpath = '//table[@class="a-normal a-spacing-micro"]//tr[' + str(p) + ']/td[@class="a-span9"]//text()'
                short_desc_val = prodtree.xpath(xpath)[1]
                short_desc_key = prodtree.xpath(
                    '//table[@class="a-normal a-spacing-micro"]//td[@class="a-span3"]/span/text()')
                # try:
                #     short_desc_val = prodtree.xpath('//table[@class="a-normal a-spacing-micro"]//span[@class="a-size-base"]/text()')
                #     for sdk in range(len(short_desc_key)):
                #         sd = short_desc_key[sdk]+" = "+short_desc_val[sdk] + " |||"
                sd = short_desc_key[p - 1] + " === " + str(short_desc_val) + " |||"

                short_desc.append(sd)

            short_desc = str(short_desc).replace('[', '').replace(']', '').replace("'", '').replace('|||,', '|||')
        except:
            short_desc = 'n/a'


        prodtree3 = driver.page_source
        prodtree3 = html.fromstring(prodtree3)

        present_360 = ""
        image360Count = ""
        try:
            present_360_json = json.loads(
                prodtree.xpath('//*[@id="spin360_feature_div"]//script[@type="text/javascript"]/text()')[0].split(
                    'dataModule.setData(')[1].strip().split(');')[0])
            view_360 = present_360_json['fullImageURLs']
            for imag in view_360:
                present_360 = present_360 + view_360[imag] + ' ||| '
                image360Count = 1

        except:
            present_360 = '360_Image_Not_Present'
            image360Count = 0
        image_360 = present_360


        try:
            review_bifurcation = []
            rev_bifurcation = prodtree.xpath('//table[@id="histogramTable"]//tr/td[3]/a/@aria-label')[0:]
            for rev in range(len(rev_bifurcation)):
                star = rev_bifurcation[rev].split('have')[1].strip()
                percent = rev_bifurcation[rev].split(' ')[0].strip() + '%'
                star_percent = str(star) + ' === ' + str(percent)
                review_bifurcation.append(star_percent)
            review_bifurcation = str(review_bifurcation).replace('[','').replace(']','').replace('\\n','').replace("', '"," ||| ")
        except:
            review_bifurcation = 'n/a'


        try:
            ratings_by_feature = []
            rbf_key = prodtree3.xpath('//*[contains(@id,"cr-summarization-attribute-")]/div/div/div/div/span/text()')
            rbf_val = prodtree3.xpath('//*[contains(@id,"cr-summarization-attribute-")]/div/div/div[2]/i/span/text()')
            for i in range(len(rbf_key)):
                rbf_kv = rbf_key[i]+"==="+rbf_val[i]
                ratings_by_feature.append(rbf_kv)

            ratings_by_feature = str(ratings_by_feature).replace("['",'').replace("']",'').replace("'",'').replace(",", " ||| ").strip()


        except:
            ratings_by_feature = 'n/a'

        MetaData = 'n/a'

        itemid= 'n/a'

        try:
            modelid = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//th[contains(text(),"Item model number")]/../td[@class="a-size-base prodDetAttrValue"]/text()')[0].strip()
            modelid = str(modelid).replace('‎','')
        except:
            try:
                modelid = prodtree.xpath('//tr[contains(@class,"a-spacing-small po-model_name")]/td[2]/span/text()')[0].strip()
                modelid = str(modelid).replace('‎', '')
            except:
                try:
                    modelid = prodtree.xpath("//div[@class='a-row a-spacing-base']/div/div/div/div/table//tr/th[contains(text(), 'Model')]/../td/text()")[0].strip()
                    modelid = str(modelid).replace('‎', '')
                except:
                    try:
                        modelid = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Item model number")]/../span[2]/text()')[0].strip()
                    except:
                        modelid = 'n/a'



        try:
            DiscountPercent = prodtree.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/text()')[0].strip()
            DiscountPercent = str(DiscountPercent).replace('-','')
        except:
            try:
                DiscountPercent =prodtree.xpath('//*[@id="corePrice_desktop"]/div/table//tr[3]/td[2]/span[1]/text()')
                DiscountPercent = str(DiscountPercent).replace('-', '').replace("['","").replace("']","").replace(",","").replace("'",'').replace("(","").replace(")","").strip()
            except:
                DiscountPercent = 'n/a'

        if DiscountPercent == []:
            DiscountPercent = 'n/a'



        rangeprice = 'n/a'

        price_type = 'n/a'

        UOM = 'n/a'

        dimensions = 'n/a'

        Country = 'n/a'

        Pincode = 'n/a'



        # try:
        #     variant1 = prodtree.xpath('//*[contains(@id,"a-autoid-")]/div/div/p//text()')
        #     variant1 = str(variant1).replace('[', '').replace(']', '')
        # except:
        #     variant1 = 'n/a'
        #
        # try:
        #     variant2 = prodtree.xpath('//*[contains(@id,"a-autoid")]/div/div[1]/img/@alt')
        #     variant2 = str(variant2).replace('[', '').replace(']', '')
        # except:
        #     variant2 = 'n/a'

        availbility_message = 'n/a'

        IncartSatus = 'n/a'

        condition = 'New'

        try:
            color = prodtree.xpath('//*[@id="variation_color_name"]/div/span/text()')
            color = str(color).replace('[','').replace(']','').replace('\\n','').replace("'","").strip()
        except:
            color = 'n/a'

        size = 'n/a'

        weight_ram_height = 'n/a'

        varaint_url = 'n/a'

        shipby= MerchantName

        soldby= MerchantName

        Disclaimer = 'n/a'

        ean ='n/a'

        Quantity='n/a'


        try:
            rating_count = prodtree2.xpath('//*[@id="filter-info-section"]/div/text()')[0].strip()
            rating_count = str(rating_count)
            character = 'total ratings'
            before,sep,after = rating_count.partition('total ratings')
            rating_count = before

        except:
            try:
                rating_count = prodtree2.xpath('//*[@id="filter-info-section"]/div/span/text()')[0].strip()
                rating_count = str(rating_count)
                character = 'total ratings'
                before, sep, after = rating_count.partition('total ratings')
                rating_count = before

            except:
                try:
                    rating_count = prodtree2.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[3]/span/text()')[0].strip()
                    rating_count = str(rating_count)
                    character = 'total ratings'
                    before, sep, after = rating_count.partition('total ratings')
                    rating_count = before
                except:
                    rating_count = 'n/a'

        print(rating_count)

        try:
            videourls = []
            ptlen = len(partjson['videos'])
            for i in range(ptlen):
                video_url = partjson['videos'][i]['url']
                videourls.append(video_url+" ||| ")

            video_url = str(videourls).replace('[','').replace(']','').replace("'","").replace('||| ,','|||')
        except:
            video_url = 'n/a'

        try:
            # video_count = prodtree.xpath('//div[@id="altImages"]/ul/li//text()')
            # video_count = str(video_count).replace('[', '').replace(']', '').replace(',', '').replace("'", '').strip()
            video_count = ptlen
            video_count = float(video_count)
        except:
            video_count = 'n/a'


        #specs_extra = str(specvalues) + str(short_desc)
        specs_extra = 'n/a'

        sellerinfo = 'n/a'

        manufacturerinfo = 'n/a'

        try:
            review_video = prodtree2.xpath('//input[@class="video-url"]/@value')
            review_video = str(review_video).replace('[', '').replace(']','').replace("', '"," ||| ")
        except:
            review_video = 'n/a'

        try:
            review_video_count = len(prodtree2.xpath('//input[@class="video-url"]/@value'))
        except:
            review_video_count = 'n/a'


        schemaorg ='yes'

        try:
            buying_opt_data = []
            buying_opt_data1 = prodtree.xpath('//div[@data-buying-option-index="0"]/span/div[2]//a//text()')
            buying_opt_data1 = str(buying_opt_data1).replace('\\n', '').replace('\\t', '').replace('\\r', '').replace("['", "").replace("']", "").replace(',', ' ||| ').replace("'", '')
            buying_opt_data2 = prodtree.xpath('//div[@data-buying-option-index="0"]/div[2]//a//text()')
            buying_opt_data2 = str(buying_opt_data2).replace('\\n','').replace('\\t','').replace('\\r','').replace("['","").replace("']","").replace(',',' ||| ').replace("'",'')
            buying_opt_data = str(buying_opt_data1)+' ||| '+ str(buying_opt_data2)
            buying_opt_data = str(buying_opt_data).replace('\\n','').replace('\\t','').replace('\\r','').replace("['","").replace("']","").replace(',',' ||| ').replace("'",'')
        except:
            buying_opt_data = 'n/a'
        if buying_opt_data == '[] ||| []':
            try:
                buying_opt_data = prodtree.xpath('//*[@id="productSupportAndReturnPolicy-return-policy-anchor-text"]/text()')[0].strip()
            except:
                buying_opt_data = 'n/a'

    #-----------------------------Edited 12th Oct -----------New Headers---------------------------------------------------------------------------------------------------
        Deliverly_Details = ""
        try:
            Delivery = prodtree.xpath('//div[@id="mir-layout-DELIVERY_BLOCK"]/div//text()')
            for msg in Delivery:
                Deliverly_Details = Deliverly_Details + msg.strip() + ' '
        except:
            Deliverly_Details = 'n/a'

        try:
            replace = prodtree.xpath('//div[@class="a-section a-spacing-none icon-content"]/a/text()')[1]
        except:
            replace = 'n/a'
#------------------content from technical details block ----------------------------------------------------
        try:
            specification = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr')

        except:
            specification = ['n/a']
        # spec_table1_len = len(specification)
        # ASIN_NO = ''
        # series = ''
        # country_origin = ''
        # Manufacturer_add = ''
        # country_of_manufacturer = ''
        # for specs in range(spec_table1_len):
        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Model Name")]')
        try:
            series = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Model Name")]/../td/text()')[0].strip()
            series =  str(series).replace('[','').replace(']','').replace('\n','').replace('\t','')
            if series == []:
                series = 'n/a'
        except:
            series = 'n/a'

        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Country of Origin")]'):
        try:
            country_origin = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Country of Origin")]/../td/text()')[0].strip()
        except:
            try:
                country_origin = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Country of Origin")]/../span[2]/text()')[0].strip()
            except:
                country_origin = 'n/a'


        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th/text()')[specs].strip() == 'Manufacturer':
        try:
            Manufacturer_add = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Manufacturer")]/../td//text()')[0].strip()
        except:
            try:
                Manufacturer_add = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Manufacturer")]/../span[2]/text()')[2]
            except:
                Manufacturer_add = 'n/a'

        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th/text()')[specs].strip() == 'Country of Origin':
        try:
            country_of_manufacturer = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"Country of Origin")]/../td/text()')[0].strip()
        except:
            try:
                country_of_manufacturer = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Country of Origin")]/../span[2]/text()')[0].strip()
            except:
                country_of_manufacturer = 'n/a'



        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th/text()')[specs].strip() == 'Brand':
            # try:
            #     Brand = prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/td/text()')[specs].strip()
            # except:
            #     Brand = Brand

        #if prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th/text()')[specs].strip() == 'ASIN':
        try:
            ASIN_NO =prodtree.xpath('//*[@id="productDetails_techSpec_section_1"]//tr/th[contains(text(),"ASIN")]/../td/text()')[0].strip()
        except:
            try:
                ASIN_NO = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"ASIN")]/../span[2]/text()')[0].strip()
            except:
                try:
                    ASIN_NO = prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//th[contains(text(),"ASIN")]/../td/text()'[0].strip())
                except:
                    ASIN_NO = 'n/a'
#----------------content from additional information block ------------------------------------------
        try:
            specification2 = prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr')

        except:
            specification2 = ['n/a']
        spec_table2_len = len(specification2)
        #importer_address = ""
        #for specs in range(spec_table2_len):

        try:
            importer_address = prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr/th[contains(text(),"Importer")]/../td/text()')[0].strip()
        except:
            try:
                importer_address = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Importer")]/../span[2]/text()')[0].strip()
            except:
                importer_address = 'n/a'

            # if prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr/th/text()')[specs].strip() == 'ASIN':
            #     try:
            #         ASIN_NO = prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr/td/text()')[specs].strip()
            #     except:
            #         ASIN_NO = ASIN_NO
        # ----------------content from additional information block end------------------------------------------
        try:
            warranty = prodtree.xpath('//div[@id="WARRANTY"]/div/a/text()')[0]
        except:
            warranty = 'n/a'

        try:
            stock_avail_details = prodtree.xpath('//*[@id="availability"]/span/text()')[0]
        except:
            stock_avail_details = 'n/a'

        try:
            return_details = prodtree.xpath('//*[@id="creturns-policy-anchor-text"]/text()')[0]
        except:
            return_details = 'n/a'
        try:
            special_tags = prodtree.xpath('//*[@id="dealBadgeSupportContent_feature_div"]/span/span/text()')[0]
        except:
            special_tags = 'n/a'
        #----------------------variant block ---------------------------------------
        try:
            DATA = prodtree.xpath('//script[@type="text/javascript"]/text()')
            for i in range(52,len(DATA)):
                data = DATA[i].strip()
                if re.search('P.register',data):
                    partjson = json.loads(data.split('"dimensionValuesDisplayData" : ')[1].split(']},')[0] + ']}')
                    break


        except:
            partjson = ['n/a']
        varaint_url = ""
        for ASIN1 in partjson:

            try:
                variant_url = 'https://www.amazon.in/dp/' + str(ASIN1) + '?&th=1&psc=1'
            except:
                variant_url = 'n/a'

            varaint_url = varaint_url + variant_url + ' || '
        #----------------------Variant Url block end------------------------------

        try:
            prod_desc = prodtree.xpath('//*[@id="productDescription"]/p/span//text()')
            prod_desc = str(prod_desc).replace('[','').replace(']','').replace("\'","").replace(',','').replace('\\xa0','').replace('"','').strip()
            prod_desc =  re.sub(clean3, '',prod_desc)
        except:
            prod_desc = 'n/a'

        # try:
        #     bankOffersHeads = prodtree.xpath('//span[@class="sopp-offer-title"]/../span[contains(text(),"Bank Offer")]')
        #     bankOffersHeadslen = len(bankOffersHeads)
        #     bankOffers = ''
        #     for i in range(bankOffersHeadslen):
        #         bankOffersHead = prodtree.xpath('//span[@class="sopp-offer-title"]/../span[contains(text(),"Bank Offer")]/text()')[i]
        #         bankOfferValues = prodtree.xpath('//span[@class="sopp-offer-title"]/../span[contains(text(),"Bank Offer")]/..//span[@class="description"]/text()')[i]
        #         bankOffers = bankOffers + bankOffersHead + "" + bankOfferValues + "|||"
        #         bankOffers = str(bankOffers).replace('[', '').replace(']', '').replace("'", '')
        # except:
        #     bankOffers = 'n/a'


        try:
            packer = prodtree.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr/th[contains(text(),"Packer")]/../td/text()')[0].strip()
        except:
            try:
                packer = prodtree.xpath('//*[@id="detailBullets_feature_div"]//span[contains(text(),"Packer")]/../span[2]/text()')[0].strip()
            except:
                packer ='n/a'

################## if offer and promotion not captured in lxml method then clickable will start from here ####################
                #if Offers_Promotion == 'n/a' or Offers_Promotion == '':
        # try:
        #     element1 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[5]/a//span')
        #     element1.click()
        #     time.sleep(1)
        #     prodtree0 = html.fromstring(driver.page_source)
        #     try:
        #         element2 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[3]//div/div/span/span[2]/span/span/span/span[2]//span[@role="button"]')
        #         element2.click()
        #         time.sleep(1)
        #         prodtree1 = html.fromstring(driver.page_source)
        #         element3 = driver.find_element(By.XPATH,'//*[@id="a-popover-7"]/div/header/button')
        #         element3.click()
        #         time.sleep(1)
        #     except:
        #         try:
        #             element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span/a')
        #             element1.click()
        #             time.sleep(3)
        #             prodtree1 = html.fromstring(driver.page_source)
        #             driver.refresh()
        #         except:
        #             pass
        #     try:
        #         element4 = driver.find_element(By.XPATH,'//*[@id="sopp-primary-ingress-0"]/div/div[4]/div//div/div/span/span[2]/span/span/span/span[2]/span/span[2]/../span[@role="button"]')
        #         element4.click()
        #         time.sleep(1)
        #         prodtree2 = html.fromstring(driver.page_source)
        #         element5 = driver.find_element(By.XPATH,'//*[@id="a-popover-8"]/div/header/button')
        #         element5.click()
        #         time.sleep(1)
        #     except:
        #         try:
        #             element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span/a')
        #             element2.click()
        #             time.sleep(3)
        #             prodtree2 = html.fromstring(driver.page_source)
        #             driver.refresh()
        #         except:
        #             pass
        # except:
        #     try:
        #         try:
        #             element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span/a')
        #             element1.click()
        #         except:
        #             element1 = driver.find_element(By.XPATH,'//*[@id="itembox-InstantBankDiscount"]/span')
        #             element1.click()
        #         time.sleep(3)
        #         prodtree1 = html.fromstring(driver.page_source)
        #         driver.refresh()
        #     except:
        #         pass
        #     try:
        #         try:
        #             element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span/a')
        #             element2.click()
        #         except:
        #             element2 = driver.find_element(By.XPATH,'//*[@id="itembox-Partner"]/span')
        #             element2.click()
        #         time.sleep(3)
        #         prodtree2 = html.fromstring(driver.page_source)
        #         driver.refresh()
        #     except:
        #         pass

        try:
            bankoffers = prodtree1.xpath('//*[@id="InstantBankDiscount-sideSheet"]/div[2]/div/div/p/text()')
            bankoffers = str(bankoffers).replace("['", '').replace("']", '').replace("', '", ' || ')
        except:
            bankoffers = ''
        if bankoffers == '[]' or bankoffers == '':
            try:
                bankoffers = prodtree1.xpath('//*[@id="sopp-instantBank-offers"]/div/div/text()[1]')
                bankoffers = str(bankoffers).replace("['", '').replace("']", '').replace("', '", ' || ')
            except:
                bankoffers = ''
        if bankoffers == '[]' or bankoffers == '':
            try:
                bankoffers = prodtree1.xpath('//*[@id="InstantBankDiscount-single-offer"]/div/h1/text()')[0]
                bankoffers = str(bankoffers).replace("['", '').replace("']", '').replace("', '", ' || ')
            except:
                bankoffers = ''

        try:
            partneroffers = prodtree2.xpath('//*[@id="Partner-single-offer"]/div/h1/text()[1]')[0].strip()
            partneroffers = str(partneroffers).replace("['", '').replace("']", '').replace("', ' ', '",
                                                                                           ' || ')
        except:
            partneroffers = ''
        if partneroffers == '[]' or partneroffers == '':
            try:
                partneroffers = prodtree2.xpath(
                    '//*[@id="sopp-seller-promotion-secondary-view"]/div[1]/div/text()[1]')
                partneroffers = str(partneroffers).replace("['", '').replace("']", '').replace("', ' ', '",
                                                                                               ' || ')
            except:
                partneroffers = ''

        # try:
        #     Offers_Promotion = str(bankoffers) + " || " + str(partneroffers)
        # except:
        #     Offers_Promotion = 'n/a'
#################### end of clickable and data fetching for offers and promoptions  #######################
        try:
            ratings_by_feature = []
            rbf_key = prodtree.xpath('//*[@id="aspect-button-group-0"]/button/span/text()')
            rbf_val = prodtree.xpath('//*[@id="aspect-button-group-0"]/button/@aria-describedby')
            for i in range(len(rbf_key)):
                rbf_kv = rbf_key[i]+"==="+rbf_val[i]
                ratings_by_feature.append(rbf_kv)

            ratings_by_feature = str(ratings_by_feature).replace('[','').replace(']','').replace("'",'').replace(",", " ||| ").strip()


        except:
            ratings_by_feature = 'n/a'

        if ASIN_NO == []:
            ASIN_NO = articalcode

        print('Review Bifc = '+ str(review_bifurcation))
        print('URL Crawled\n  -  -  -  -  -  -  -  -  -  -  -  -  -\n')

        driver.quit()
        driver1.quit()
        driver2.quit()

        # date_format = '%Y-%m-%d %I:%M:%S:%Z'
        # date = datetime.now(tz=utc)
        # date = date.astimezone(timezone('Asia/Kolkata'))
        # TimeStamp = date.strftime(date_format)

        PLP_URL = 'n/a'
        META_ALTTAG = 'n/a'
        Size_chart = 'n/a'
        Noofinstock = 'n/a'
        In_Cart_Status = 'n/a'
        MARKETER_ADDRESS = 'n/a'
        Pin_Code = 'n/a'
        FAQS = 'n/a'
        IMAGE_URL_3D = 'n/a'

        record = [channel,ASIN_NO,articalcode,produrl,canonical_url,breadcrum,category,condition,
                Brand,ProductName,modelid,series,MetaTitle,"n/a",MetaDesc,images,image_count, main_image_alt,video_url,
                video_count,image_360,image360Count,prod_desc,Highlights,key_features_count,Brand_desc1,'n/a',Brand_desc,brand_data_img,user_manual,
                Doc,"n/a",schemaorg,AdditionalDetails,ean,upc,RegularPrice,ProductPrice,
                DiscoutPrice,DiscountPercent,Ratings,Rating_count,ratings_by_feature,
                top_rev,Review_count,review_bifurcation,review_image,special_tags,partneroffers,
                bankoffers,Availability,stock_avail_details,"n/a",Availability,
                soldby,sellerinfo,shipby,ShippingDetails,Deliverly_Details,replace,return_details,
                country_origin,country_of_manufacturer,Manufacturer_add,importer_address,sellerinfo,packer,warranty,
                "n/a","n/a",qNa,varaint_url,Disclaimer,specvalues,"n/a","n/a",
                "n/a","n/a","n/a","n/a","n/a","n/a",
                "n/a","n/a",crawldate, recdno, produrl, articalcode, channel, channelid]

        record = [channel, ASIN_NO, articalcode, PLP_URL, produrl, canonical_url, breadcrum, category,
                  condition, ProductName, Brand, modelid, series, MetaTitle, META_ALTTAG, MetaDesc,
                  images, image_count, video_url, video_count, prod_desc, Highlights,
                  key_features_count,
                  Brand_desc1,'n/a',Brand_desc,brand_data_img, user_manual, Doc,
                  Size_chart, schemaorg,
                  AdditionalDetails, ean, upc, RegularPrice, ProductPrice, DiscoutPrice, DiscountPercent,
                  Ratings, Rating_count, ratings_by_feature, top_rev, Review_count,
                  review_bifurcation, review_image, special_tags, partneroffers, bankoffers, Availability,
                  stock_avail_details, Noofinstock, In_Cart_Status,
                  soldby, sellerinfo, shipby, ShippingDetails, Deliverly_Details, replace,
                  return_details, country_origin,country_of_manufacturer,Manufacturer_add,importer_address,
                  MARKETER_ADDRESS, packer,warranty, Pin_Code, FAQS, qNa, varaint_url,Disclaimer,specvalues,
                  "n/a", "n/a",
                  "n/a", "n/a", "n/a", "n/a", "n/a", "n/a",
                  "n/a", "n/a", IMAGE_URL_3D,
                  image_360, main_image_alt,
                  crawldate, recdno, produrl, articalcode, channel, channelid]

        for z in range(len(record)):
            record[z] = str(record[z]).replace('\n', '').replace('\t', '').replace('\r', '')
            record[z] = str(record[z]) + '\t'
        record.append('\n')
        with open(r".\Amazon_P4_Output_ " + str(num) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
            fp.writelines(record)


    except Exception as e:
        print(str(e))

###################################################################################################
############################## Header Structure ###############################################
###################################################################################################

# row = ['P4_Record_No','CHANNEL NAME','P4_Canonical_URL','P4_Product_URL', 'P4_Breadcrumb', 'P4_Meta_title', 'P4_Meta_Description','P4_Meta_Data','P4_Product_ID', 'P4_Item_ID', 'P4_Model_ID', 'P4_EAN', 'P4_UPC','P4_Brand',
#         'P4_Category', 'P4_Product_Name','P4_Tag', 'P4_Sale_Price','P4_MRP','P4_Discount_Price','P4_Discount_Percentage','P4_Range_Price','P4_Price_Type',
#         'P4_Offers/Promotion','P4_UOM','P4_Quantity','P4_Dimensions','P4_Star Ratings','P4_Number of Reviews','P4_Number of Ratings','Bifurcation_Ratings','Bifurcation_Review','P4_Country','P4_Pin_Code','P4_Availability','P4_Availability_Messages','P4_In_Cart_Status',
#         'P4_Shipping_Detail','P4_Main_Image_URL','P4_MainImageAltTag','P4_All_Image_URL', 'P4_All_Image_Count','P4_360_Image','P4_Video_URL','P4_3D_Video_URL', 'P4_Description','P4_Additional_Information', 'P4_Key Features_Highlights',
#         'P4_Specification_1','P4_Specification_2','P4_Specification_3', 'P4_Aplus_Content','P4_Aplus_Data_Image','P4_Aplus_Image Count','P4_Condition','P4_Variant_URL','P4_Seller_Info','P4_Manufacturer_Info',
#         'P4_Ship_By','P4_Sold_By','P4_User_Manual','P4_Disclaimer','P4_Product_Includes', 'P4_Buying_Opt_Data','P4_Image_Review','P4_Image_Review_Count','P4_Video_Review','P4_Video_Review_Count','P4_Top_Reviews','P4_Customer_QA(count)','P4_Customer_Q&A',
#         'P4_TimeStamp','Product_URL','SKU_ID']


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
       "IMAGE ALT TAGS","TIMESTAMP", "Record No", "produrl","articalcode","channel","channelid" ]
for z in range(len(row)):
    #row[z] = str(row[z]).replace('\n', '').replace('\t', '')
    row[z] = str(row[z]) + '\t'
row.append('\n')


with open(r".\Amazon_P4_Output_ " + str(num) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
    fp.writelines(row)

# with opritelines(row)

prdlist = list()
file = r".\Amazon" + str(num) + ".xlsx"
raw_data = pd.read_excel(file)
raw_dataf = pd.DataFrame(raw_data)
urllist = raw_dataf['productURL'].tolist()
Articalcode = raw_dataf['Article Code'].tolist()
Channel=raw_dataf['Channel'].tolist()
Channelid=raw_dataf['productId'].tolist()
recdno1 = raw_dataf['Record No'].tolist()
# cat_url1 = raw_dataf['Cat_URL'].tolist()
# ip_brand1 = raw_dataf['Input_Brand'].tolist()
# ip_l01 = raw_dataf['Input_L0'].tolist()
# ip_l11 = raw_dataf['Input_L1'].tolist()


for j, produrl in enumerate(urllist):
    try:
        recdno = recdno1[j]
        articalcode = Articalcode[j]
        #articalcode = 'B004J18S46'
        #channel = 'Amazon'
        channel = Channel[j]
        channelid = Channelid[j]
        produrl = urllist[j]
        # cat_url = 'n/a' #cat_url1[j]
        # ip_brand = 'n/a' #ip_brand1[j]
        # ip_l0 = 'n/a' #ip_l01[j]
        # ip_l1 = 'n/a' #ip_l11[j]
        #channelid = 'B006NVDWGE'
        #produrl = 'https://www.amazon.in/Delonghi-EC850M-1450-Watt-Espresso-Coffee/dp/B004J18S46/ref=sr_1_4?qid=1666266870&refinements=p_89%3ADELONGHI&rnid=3837712031&s=kitchen&sr=1-4'
        pdp = productcrawl(produrl,articalcode,channel,channelid)
    except:
        print('Error')


print('Done')
# df = pd.read_csv(r'C:\Users\User\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Output\amazon_bluetooth_re_OP.csv')
# list = df.to_dict()
# df2 = pd.DataFrame(list)
# df2.to_excel(r"C:\Users\User\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Output\amazon_bluetooth_re_OP.xlsx", encoding='utf-8', index=False)
print('Crawl Complete')
