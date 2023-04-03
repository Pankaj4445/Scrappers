import datetime
import random
import time
from lxml import html
import pandas as pd
from time import timezone
from pytz import timezone, utc
from datetime import date
from datetime import datetime
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import requests

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

    ]
    return random.choice(user_agent)

def productcrawl(produrl):

    useragent = useragentselector()

    prodname = ''
    sellingprice = ''
    mrp = ''
    discountpercentage = ''
    couponapplicable = ''
    review = ''
    rating = ''
    imageurl = ''
    breadcrumb = ''
    canonicalurl = ''
    variantsname = ''
    variantsize = ''
    storagecondition = ''
    prescription = ''
    composition = ''
    producthighlight = ''
    briefdescription = ''
    vendor = ''
    manufacturername = ''
    pstDateTime = ''
    # s = Service(r"C:\Users\User\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\chromedriver.exe", )
    # browser = webdriver.Chrome(service=s)
    # browser.get(produrl)
    # time.sleep(1)
    # resp = (browser.page_source)
    # browser.quit()
    headers = {
        'authority': 'www.1mg.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec - ch - ua': '" Not A;Brand";v = "99", "Chromium";v = "99", "Google Chrome";v = "99"',
        #'cookie': 'VISITOR-ID=81ca0bc9-b44d-4fae-cfe7-03aaa27c6f06_acce55_1648704434; city=New Delhi; abVisitorId=671131; abExperimentShow=true; amoSessionId=d3cb66c5-288b-4ee2-a088-338dd9f0762e; _csrf=ax0W210gawSdi_21qvN_sG-P; rl_group_id=RudderEncrypt:U2FsdGVkX1+1d6lqX3QjqTzn8CmqC6KMcDs/3iL0IL0=; rl_group_trait=RudderEncrypt:U2FsdGVkX1+7/ZcElsfSJvOXkYywItFOYvg+NP1kkRY=; rl_anonymous_id=RudderEncrypt:U2FsdGVkX19Q86ATxZTrCee+VdMBjuf4SWce2iA3WoQbVNpyP6By5TJpnkbnW1f7wz7cMdLp+3UKZwFPwpdowg==; rl_page_init_referrer=RudderEncrypt:U2FsdGVkX1+0t8SAo4M7TOQcvldxYSWT52/adQJiVRI=; rl_page_init_referring_domain=RudderEncrypt:U2FsdGVkX19G+gonpgS4vNYFOWpZzfx8rQiOiRmYef0=; rl_user_id=RudderEncrypt:U2FsdGVkX19YWoAdUHNUIibG4onNHVijXGPZ8Ak0GO9oXBN8i3dW2CAGuaydy4fohb9+2xKNUCwrAIXj3TjtwSeN64T5xXi/KtQVMI0Htaw=; rl_trait=RudderEncrypt:U2FsdGVkX19JzAXRSET1xwm0lUmvcMs31dTj+TAXwFbw8NreId09YUxh9g45gsC58KHJMbjX/RJqI5AdZO5CFg==; geolocation=false; session=iOERd9dcDvI5PdTLiEldEA.mejXIAWHroZ5o4rcXBz7gF_CzhIINPAvMUQ_cWho4WSLx0u92bSe2pIgONQODA6Xgni7uyX0jnIwnh-9DDLo-zS9iBguPxFvqk60QxbdX0SJaaWP_kEDAu1efsj7zwHpk2R0Ec-9S5dD_fruRerrvg.1648704441919.2592000000.BgOuwkrjLoZDYMO4jf7x5pI9xUbJUdMkmu8MoOKAues; _fbp=fb.1.1648704462320.1127770498; _gcl_au=1.1.1977661775.1648704462; _uetsid=4a0122d0b0b311ec86cfd5c1fe027e4e; _uetvid=4a017720b0b311ecbeb7d76807f0313a; _nv_uid=173339004.1648704460.2c52feee-20f2-40d6-b51f-b8aee778d5c4.1648704460.1648704460.1.0; _nv_utm=173339004.1648704460.1.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=; _nv_sess=173339004.1648704460.iO2Xjl8TiFWKhhAPV9sDpI4MJULj2wzLZnLbQGjuXlpuSpDkVJ; _nv_did=173339004.1648704460.4323018779de73p; AMP_TOKEN=$NOT_FOUND; _ga=GA1.2.761463193.1648704463; _gid=GA1.2.231826169.1648704463; singular_device_id=5c5dbb0d-8b34-4584-a2a9-4b81da1ea77d; __adroll_fpc=55e7bc17a240406328127cabbf367af8-1648704465356; __ar_v4=|U4ZFS2QH4VB65A54O43AEQ:20220330:1|6PFMKMAZXFGFLMSXPCJHFF:20220330:1|KJTLL7NSNRFA5J3GVYGJVJ:20220330:1; __gads=ID=487956030c5a6548:T=1648704464:S=ALNI_Mbw9RarDO9ZtBmDL1ag4iJRcSDfBA; shw_13453=1; _nv_banner_x=13453; _nv_hit=173339004.1648704460.cHZpZXc9MXxidmlldz1bIjEzNDUzIl0=; _nv_push_neg=1',
        #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'user-Agent': useragent,
    }
    for i in range(2):
        try:
            #sleeptime = random.randint(4, 6)
            time.sleep(2)
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
            try:
                prodname = prodtree.xpath('//div[@id="drug_header"]/div/div/div[2]/div/div/h1/text()')[0].strip()
            except:
                try:
                    prodname = prodtree.xpath('//div[@id="drug_header"]/div/div/div[1]/div/div/h1/text()')[0].strip()
                except:
                    try:
                        prodname = prodtree.xpath('//div[@class="otc-container"]/div/div/div[1]/div/h1/text()')[0].strip()
                    except:
                        prodname = 'n/a'
        except:
            prodname = 'n/a'

        try:
            try:
                Sale_Price = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div[2]/div[2]/text()')[1].strip()
                Sale_Price = str(Sale_Price).replace("₹", "")
            except:
                try:
                    Sale_Price = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/div[2]/text()')[1].strip()
                    Sale_Price = str(Sale_Price).replace("₹", "")
                except:
                    try:
                        Sale_Price = prodtree.xpath('//div[@class="OtcPriceBox__atc-box___30PES"]/div[2]/div/div/div[2]/span[1]/text()')[1].strip()
                        Sale_Price = str(Sale_Price).replace("₹", "")
                    except:
                        try:
                            Sale_Price = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/div[2]/span[1]/text()')[1].strip()
                            Sale_Price = str(Sale_Price).replace("₹", "")
                        except:
                            try:
                                Sale_Price = prodtree.xpath('//div[@class="OtcPriceBox__price-box___p13HY"]/div/div/div[2]/span/text()')[1].strip()
                                Sale_Price = str(Sale_Price).replace("₹", "")
                            except:
                                try:
                                    Sale_Price = prodtree.xpath('//div[@class="DrugATCContent__substitute-section___3FXXe"]/div/div/div/div/div/div/div/div/div/div/a/div[6]/div/text()')[1].strip()
                                    Sale_Price = str(Sale_Price).replace("₹", "")
                                except:
                                    try:
                                        Sale_Price = prodtree.xpath('//div[@class="OtcPriceBox__price-box___p13HY"]/div[2]/div/text()')[1].strip()
                                        Sale_Price = str(Sale_Price).replace("₹", "")
                                    except:
                                        try:
                                            Sale_Price = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/div/text()')[1].strip()
                                            Sale_Price = str(Sale_Price).replace("₹", "")
                                        except:
                                            Sale_Price = 'n/a'
        except:
            Sale_Price = 'n/a'

        try:
            try:
                MRP = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/span[2]/text()')[1].strip()
            except:
                try:
                    MRP = prodtree.xpath('//div[@class="OtcPriceBox__atc-box___30PES"]/div[2]/div/div/div[2]/span[2]/text()')[1].strip()
                except:
                    try:
                        MRP = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/div[2]/span[2]/text()')[1].strip()
                    except:
                        try:
                            MRP = prodtree.xpath('//div[@class="OtcPriceBox__price-box___p13HY"]/div[1]/div/span[2]//text()')[1].strip()
                        except:
                            MRP = 'n/a'
        except:
            MRP = 'n/a'

        try:
            try:
                Discount_Percentage = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/span[3]/text()')[0].strip()
                Discount_Percentage = str(Discount_Percentage).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
            except:
                try:
                    Discount_Percentage = prodtree.xpath('//div[@class="OtcPriceBox__atc-box___30PES"]/div[2]/div/div/div[2]/span[3]/text()')[0].strip()
                    Discount_Percentage = str(Discount_Percentage).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
                except:
                    try:
                        Discount_Percentage = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div/div[2]/span[3]/text()')[0].strip()
                        Discount_Percentage = str(Discount_Percentage).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
                    except:
                        try:
                            Discount_Percentage = prodtree.xpath('//div[@class="OtcPriceBox__price-box___p13HY"]/div[1]/div/span[3]//text()')[0].strip()
                            Discount_Percentage = str(Discount_Percentage).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
                        except:
                            try:
                                Discount_Percentage = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div[2]/span[3]//text()')[0].strip()
                                Discount_Percentage = str(Discount_Percentage).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
                            except:
                                Discount_Percentage = 'n/a'
        except:
            Discount_Percentage = 'n/a'

        try:
            couponapplicable = prodtree.xpath('//div[@class="DrugPriceBox__container___1ya7B"]/div[2]/div/div[3]/div[2]/text()')[0].strip()
        except:
            couponapplicable = 'n/a'

        try:
            Reviews = prodtree.xpath('//div[@class="ProductTitle__ratings___4MWF_"]/span/text()')[0].strip()
        except:
            Reviews = 'n/a'

        try:
            Ratings = prodtree.xpath('//div[@class="ProductTitle__ratings___4MWF_"]/div/span/text()')[0].strip()
        except:
            Ratings = 'n/a'

        try:
            All_Image_URL = prodtree.xpath('//div[@class="ProductImage__thumbnail-array___15c5x"]/div/div/img/@src')
            All_Image_URL = str(All_Image_URL).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
        except:
            All_Image_URL = ''
        if All_Image_URL == '[]':
            try:
                All_Image_URL = prodtree.xpath('//div[@class="style__container___3DB0z"]/div/img/@src')
                All_Image_URL = str(All_Image_URL).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")
            except:
                All_Image_URL = 'n/a'
        else:
            pass

        try:
            breadcrumb = prodtree.xpath('//div[@class="OtcPage__breadcrumb-container___ib1Xx"]/div/span//text()')
            breadcrumb = str(breadcrumb).replace("[\'", "").replace("\']", "").replace("\', \'", " > ")
        except:
            breadcrumb = ''
        if breadcrumb == '[]':
            try:
                breadcrumb = prodtree.xpath('//div[@class="DrugHeader__wrapper___ZqUzE"]/div/div/span//text()')
                breadcrumb = str(breadcrumb).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "")
            except:
                breadcrumb = 'n/a'
        else:
            pass

        try:
            Weight_RAM_Height = prodtree.xpath('//div[@class="DrugPriceBox__qty-wrapper___1RBzv"]/div/text()')
            Weight_RAM_Height = str(Weight_RAM_Height).replace("[\'", "").replace("\']", "").replace("\', \'", "")
        except:
            Weight_RAM_Height = ''
        if Weight_RAM_Height == '[]':
            try:
                Weight_RAM_Height = prodtree.xpath('//div[@class="OtcPriceBox__price-box___p13HY"]/div/div/span/text()')
                Weight_RAM_Height = str(Weight_RAM_Height).replace("[\'", "").replace("\']", "").replace("\'", "").replace(",", "").replace("of", "")
            except:
                Weight_RAM_Height = 'n/a'
        else:
            pass

        try:
            Availability = prodtree.xpath('//div[@class="AvailableStatus__container___1R2Nk"]/div/div//text()')
            Availability = str(Availability).replace("[\'", "").replace("\']", "")
            if Availability == "SOLD OUT":
                Availability = "Out Of Stock"
            elif Availability == '[]':
                Availability = "In Stock"
            else:
                Availability = "In Stock"
        except:
            Availability = 'n/a'

        try:
            Availability_Messages = prodtree.xpath('//div[@class="AvailableStatus__container___1R2Nk"]/div/div//text()')
            Availability_Messages = str(Availability_Messages).replace("[\'", "").replace("\']", "")
        except:
            Availability_Messages = 'n/a'

        try:
            Warning_Message = prodtree.xpath('//div[@class="DrugPriceBox__banned-container___3ngUi"]/div[1]//text()')[0].strip()
        except:
            Warning_Message = 'n/a'

        try:
            variantsname = prodtree.xpath('//div[@class="OtcVariants__variant-div___2l321"][1]/div/div/text()')[0].strip()
        except:
            variantsname = 'n/a'

        variantsname = str(variantsname).replace("[\'", "").replace("\']", "").replace("\', \'", " || ")

        try:
            variantsize1 = prodtree.xpath('//div[@class="OtcVariants__container___2Y3D2"][2]/div/div/a/div[1]//text()')[0].strip()
        except:
            variantsize1 = 'n/a'

        try:
            variantsize2 = prodtree.xpath('//div[@class="OtcVariants__container___2Y3D2"][2]/div/div/div/div[1]//text()')[0].strip()
        except:
            variantsize2 = 'n/a'

        variantsize = str(variantsize1) + str(variantsize2) .replace("[\'", "").replace("\']", "").replace("\', \'", " || ")[0].strip()

        try:
            Condition = prodtree.xpath('//div[@class="DrugHeader__left___19WY-"]/div/div[3]/div[2]/text()')[0].strip()
        except:
            Condition = 'n/a'

        try:
            Prescription = prodtree.xpath('//div[@class="DrugHeader__left___19WY-"]/div/span/text()')[0].strip()
        except:
            Prescription = 'n/a'

        try:
            composition = prodtree.xpath('//div[@class="DrugHeader__left___19WY-"]/div/div[2]/div[2]/a/text()')[0].strip()
        except:
            composition = 'n/a'

        try:
            Description = prodtree.xpath('//div[@class="ProductDescription__description-content___A_qCZ"]//text()')
            Description = str(Description).replace("[", "").replace("]", "").replace("\'", "").replace(".,", ". || ").replace(",  , ", "")
        except:
            Description = ''
        if Description == '':
            try:
                Description = prodtree.xpath('//div[@class="DrugOverview__container___CqA8x"]//text()')
                Description = str(Description).replace("[", "").replace("]", "").replace("\'", "").replace(".,", ". || ").replace(",  , ", "")
            except:
                Description = 'n/a'
        else:
            pass

        try:
            try:
                Seller_Info = prodtree.xpath('//div[@class="VendorInfo__container___-iV1S"]/div//text()')[1] + \
                         prodtree.xpath('//div[@class="VendorInfo__container___-iV1S"]/div//text()')[2]
                Seller_Info = str(Seller_Info).replace("[\'", "").replace("\']", "").replace(",", "")
            except:
                try:
                    Seller_Info = prodtree.xpath('//div[@class="DrugPage__vendors___R1Bnk"]/div//text()')[1] + \
                             prodtree.xpath('//div[@class="DrugPage__vendors___R1Bnk"]/div//text()')[2]
                    Seller_Info = str(Seller_Info).replace("[\'", "").replace("\']", "").replace(",", "")
                except:
                    Seller_Info = 'n/a'
        except:
            Seller_Info = 'n/a'

        try:
            try:
                Manufacturer_Info = prodtree.xpath('//div[@class="DrugHeader__left___19WY-"]/div/div[1]/div[2]/a/text()')[0].strip()
            except:
                try:
                    Manufacturer_Info = prodtree.xpath('//div[@class="row OtcPage__top-container___2JKJ-"]/div[3]/div/div[2]/a/text()')[0].strip()
                except:
                    Manufacturer_Info = 'n/a'
        except:
            Manufacturer_Info = 'n/a'

        try:
            Canonical_URL = prodtree.xpath('//link[@rel="canonical"]/@href')[0].strip()
        except:
            Canonical_URL = 'n/a'

        try:
            Meta_Title = prodtree.xpath('//title//text()')[0].strip()
        except:
            Meta_Title = 'n/a'

        try:
            Meta_Description = prodtree.xpath('//meta[@name="description"]/@content')[0].strip()
        except:
            Meta_Description = 'n/a'

        try:
            Brand = prodtree.xpath('//*[@id="container"]/div/div/div[2]/div[3]/div[1]/div[2]/a/text()')[0]

        except:
            try:
                Brand = prodname.split(' ')[0]
            except:
                Brand = 'n/a'

        try:
            Discount_Price = int(MRP) - int(Sale_Price)
        except:
            Discount_Price = 'n/a'

        try:
            Offers_Promotion = prodtree.xpath('//*[@id="container"]/div/div/div[2]/div[4]/div[3]/div/div/div[2]//text()')
            Offers_Promotion = str(Offers_Promotion).replace('[','').replace(']','').replace(',',' || ').replace('\'','')
        except:
            Offers_Promotion = 'n/a'

        try:
            Quantity = prodtree.xpath('//*[@id="dropdown-377968"]/text()')[0]
        except:
            Quantity = 'n/a'

        try:
            Main_Image_URL = prodtree.xpath('//*[@id="container"]/div/div/div[2]/div[2]/div/div[2]/div/img/@src')[0]
        except:
            Main_Image_URL = 'n/a'

        try:
            Features_Highlights = prodtree.xpath('//*[@id="container"]/div/div/div[2]/div[3]/div[2]/div[2]//text()')
            Features_Highlights = Features_Highlights.replace('[','').replace(']','').replace(',', ' || ')
        except:
            Features_Highlights = 'n/a'

        Variant_URL = ""
        try:
            Variant_URL1 = prodtree.xpath('//*[@id="similar-skus-section"]/div[2]/div/div[2]/div/div//a/@href')
            for i in Variant_URL1:
                Variant_URL = Variant_URL + 'https://www.1mg.com' + i + ' || '
        except:
            Variant_URL = 'n/a'

        try:
            Country = prodtree.xpath('//div[@class="VendorInfo__container___-iV1S"]/div//text()')[0].split(':')[1]
        except:
            Country = 'n/a'

        try:
            Top_Reviews = prodtree.xpath('//div[@class="ReviewCards__review-description___WoLdZ"]/text()')
            Top_Reviews = str(Top_Reviews).replace('[','').replace(']','').replace(',',' || ').replace('\'','')
        except:
            Top_Reviews = 'n/a'

        try:
            Expiry_Date = prodtree.xpath('//*[@id="container"]/div/div/div[3]/div[1]/div[9]/div/text()')[1]
        except:
            Expiry_Date = 'n/a'


        Meta_Data = 'n/a'
        Item_ID = 'n/a'
        Model_ID = 'n/a'
        EAN = 'n/a'
        UPC = 'n/a'
        Category = 'n/a'
        Tag = 'n/a'
        Range_Price = 'n/a'
        Price_Type = 'n/a'
        UOM = 'n/a'
        Dimensions = 'n/a'
        Pin_Code = 'n/a'
        In_Cart_Status = 'n/a'
        Shipping_Detail = 'n/a'
        Video_URL = 'n/a'
        Additional_Information = 'n/a'
        Specification_1 = 'n/a'
        Specification_2 = 'n/a'
        Specification_3 = 'n/a'
        Aplus_Content = 'n/a'
        Color = 'n/a'
        Size = 'n/a'
        Ship_By = 'n/a'
        Sold_By = Manufacturer_Info
        User_Manual = 'n/a'
        Discalimer = 'n/a'
        Product_Includes = 'n/a'
        Image_Review = 'n/a'
        Customer_QA_Count = 'n/a'
        Customer_QA = 'n/a'
        Composition = 'n/a'
        Ingredients = 'n/a'

        print(produrl)
        print(prodname)
        print(Sale_Price)
        print(MRP)
        print("URL Crawled")

        date_format = '%Y-%m-%d %I:%M:%S:%Z'
        date = datetime.now(tz=utc)
        date = date.astimezone(timezone('US/Central'))
        TimeStamp = date.strftime(date_format)

        record = [Record_No, Canonical_URL, produrl, breadcrumb, Meta_Title, Meta_Description, Meta_Data, Product_ID, Item_ID, Model_ID, EAN, UPC, Brand, Category,
                  prodname, Tag, Sale_Price, MRP, Discount_Price, Discount_Percentage, Range_Price, Price_Type, Offers_Promotion, UOM, Quantity, Dimensions,
                  Ratings, Reviews, Country, Pin_Code, Availability, Availability_Messages, In_Cart_Status, Shipping_Detail, Main_Image_URL, All_Image_URL, Video_URL, Description, Additional_Information, Features_Highlights, Specification_1, Specification_2, Specification_3, Aplus_Content,
                  Warning_Message, Condition, Color, Size, Weight_RAM_Height, Variant_URL, Seller_Info, Manufacturer_Info, Ship_By, Sold_By, User_Manual, Discalimer,
                  Product_Includes, Image_Review, Top_Reviews, Customer_QA_Count, Customer_QA, Expiry_Date, Prescription, Composition, Ingredients, TimeStamp ]
        for z in range(len(record)):
            record[z] = str(record[z]) + '\t'
        record.append('\n')

        with open(r'D:\OneDrive - CONTEXIO LLP\PythonProject\Script\1mg\1mg_P4_Output ' + str(crawled_date) +'.txt', 'a', newline='', encoding="utf-8") as fp:
            fp.writelines(record)
            fp.close()

    except Exception as e:
        print(str(e))

###################################################################################################
############################## 1mg_P4_v2's Script Caller ###############################################
###################################################################################################
crawled_date = date.today()
row = ['Record_No',	'Canonical_URL', 'Product_URL',	'Breadcrumb', 'Meta_Title',	'Meta_Description',	'Meta_Data', 'Product_ID', 'Item_ID', 'Model_ID', 'EAN', 'UPC',
       'Brand', 'Category', 'Product_Name', 'Tag', 'Sale_Price', 'MRP', 'Discount_Price', 'Discount_Percentage', 'Range_Price', 'Price_Type',
       'Offers/Promotion', 'UOM', 'Quantity', 'Dimensions', 'Ratings',	'Reviews', 'Country', 'Pin_Code', 'Availability', 'Availability_Messages',
       'In_Cart_Status', 'Shipping_Detail', 'Main_Image_URL', 'All_Image_URL', 'Video_URL', 'Description', 'Additional_Information', 'Features/Highlights',
       'Specification_1', 'Specification_2', 'Specification_3', 'A+_Content', 'Warning_Message', 'Condition', 'Color', 'Size', 'Weight/RAM/Height', 'Variant_URL', 'Seller_Info',
       'Manufacturer_Info', 'Ship_By', 'Sold_By', 'User_Manual', 'Discalimer', 'Product_Includes', 'Image_Review', 'Top_Reviews', 'Customer_QA(count)', 'Customer_Q&A',
       'Expiry_Date', 'Prescription',	'Composition', 'Ingredients', 'TimeStamp']
prdlist = list()
for z in range(len(row)):
    row[z] = str(row[z]) + '\t'
row.append('\n')
with open(r'D:\OneDrive - CONTEXIO LLP\PythonProject\Script\1mg\1mg_P4_Output ' + str(crawled_date) +'.txt', 'a', newline='', encoding="utf-8") as fp:
    fp.writelines(row)
    fp.close()
file = (r"D:\OneDrive - CONTEXIO LLP\PythonProject\Script\1mg\P4_1mg_Inputre.xlsx")
raw_data = pd.read_excel(file)
raw_dataf = pd.DataFrame(raw_data)
urllist = raw_dataf['URL'].tolist()
sku1 = raw_dataf['SKU ID'].tolist()
cat1 = raw_dataf['Category'].tolist()
disname1 = raw_dataf['Display Name'].tolist()
mkt1 = raw_dataf['MKT Company Name'].tolist()
Ratio = raw_dataf['Ratio'].tolist()
recno1 = raw_dataf['Record No'].tolist()
for j, produrl in enumerate(urllist):
    try:
        Product_ID = sku1[j]
        Record_No = recno1[j]
        cat = cat1[j]
        disname = disname1[j]
        mkt = mkt1[j]
        #produrl = 'https://www.1mg.com/otc/a-to-z-immune-tablet-otc678388'
        pdp = productcrawl(produrl)
    except:
        print('Error')
print('Done')

