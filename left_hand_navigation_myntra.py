import csv
import requests
from lxml import html
import time
import datetime
from datetime import date
from datetime import datetime
import pandas as pd
import json
from pytz import timezone, utc
import random

def proxyselector():
    proxy_list = [
       
    ]
    return random.choice(proxy_list)

def productcrawl(produrl):
    proxies = proxyselector()
    print(proxies)
    headers = {
        'authority': 'www.myntra.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        #'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        #'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTlRnNFlqTTRaVEl0TVRKbU9TMHhNV1ZrTFRsalpqY3ROVFkzT0dSaU1HVmlORE15SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTnpVd05qRTNOallzSW1semN5STZJa2xFUlVFaWZRLkh1SU5uVUpYaE9CNWNjSksyandLYkpsZUFRU0NkMm9jb0h0V3FmdTRhUnc=; bc=true; _d_id=3d7a3e11-3025-4fb4-b8a7-eccc7caa5457; mynt-eupv=1; mynt-ulc-api=pincode:400071; _gcl_aw=GCL.1659509768.CjwKCAjwlqOXBhBqEiwA-hhitOtj-m3YW6nOIssCG5OSCVO7rWqor5s736pJJc81lZ13MehnTtTxlhoC0RIQAvD_BwE; _gcl_au=1.1.12057716.1659509768; OMG-349836=SSKey=&UUserID={b846a7ee-f2a0-4c59-a390-cd1ef07cca12}&fpc=true&attributionMode=fpc&AttributionPartnerRef=CjwKCAjwlqOXBhBqEiwA-hhitOtj-m3YW6nOIssCG5OSCVO7rWqor5s736pJJc81lZ13MehnTtTxlhoC0RIQAvD_BwE&channel=perf_google_search_brand; _fbp=fb.1.1659509771390.1763325435; _ga=GA1.2.153316640.1659509772; _gid=GA1.2.395022711.1659509772; _gac_UA-1752831-18=1.1659509772.CjwKCAjwlqOXBhBqEiwA-hhitOtj-m3YW6nOIssCG5OSCVO7rWqor5s736pJJc81lZ13MehnTtTxlhoC0RIQAvD_BwE; tvc_VID=1; _cc_id=2e0a9b8b13e4c03d3ddec04243dd705b; panoramaId_expiry=1660118903928; panoramaId=6d13aa7d54be85a5715f0d9b0b874945a7025078e0b4b8b69dd1a2f819245769; _abck=C896AE0571AC9ED2A7B2A8CF033361AD~0~YAAQL13SF+SG+luCAQAA35w8YwjpxSkn0lOBID9WNOpbK/9hiC+zj8XWdLGPQvXVDlOI2AraFhplA+nH2DYTFs7mNRDNNR1fX9xExzsOLdpr9Qw2aaQgq9nYqv+0N9gBXH82+thypXalF0N47HGr0eNY+hfm6njGP4BywZEARYF7P7EMKvc6QpltiawI7LCO00k7KapmsQMqqeAkqMAsZKwhZ7m0TqERBHP/u3h3pPd6Tu4ZiUqYleGqzs6g2XcySaMDnURIskpYMFAmH1CIk/TPm2dVKdg0JAMsTWq7Dui7AqN6CPwjniUZmZUCXCcgbkWO0rOAryeGeTnvipWjBenNoJyK4EHq5+O+GqKZ1i1JmYlEXHp61n5b8SQLKwn7CW6TCbpY5zyFxi6VBPn+/9zYop0xiMZu~-1~-1~1659525828; _ma_session={"id":"0fbf6a3c-cba2-4bfa-8cae-4645e5811e87-3d7a3e11-3025-4fb4-b8a7-eccc7caa5457","referrer_url":"","utm_medium":"","utm_source":"","utm_channel":"direct"}; _mxab_=checkout.selective=enabled;config.bucket=regular;checkout.couponUpsell=enabled;checkout.attachedProducts=enabled;pdp.expiry.date=enabled; _pv=default; dp=d; microsessid=35; utm_track_v1={"utm_source":"direct","utm_medium":"direct","trackstart":1659522293,"trackend":1659522353}; lt_timeout=1; lt_session=1; _xsrf=zJpkm1EUurCvNuJuEzdUKOmWjQGzmKDb; user_session=VdC3VQI0tTnLqkPGyRJwJw.AtIy8htfsqC0vGKdAgkX88zfBoasVC1yOKelekeCwdxAVRKOZUS1Mv0H1Plk4CLJ7rcDPuiftXCXZEOTLUOwMyqjnl0UlpQKkpFohQ4trfUXBgA5WQsHN6S_JTqsPQrxcqwAPxEIx3ZO3XxK6CSfZg.1659522293027.86400000.mEfWdJXo8t7tKZcqCMRWuLMKiCzjqVjuc41EQWd7E08; ak_bmsc=5B2D5120A7CCC0315C452FBB356E44E2~000000000000000000000000000000~YAAQL13SF/WG+luCAQAAep08YxBREszki0SbW4lEMM/Z4syVuNeHzIEVU1Cbyri+wFSuAOhHY2BfIMRmykErlutSlhQe6Oo8JDmmnA6tq3MJxAXpeCcvN+oBow/VZeIu7Tnk6JChvI4PnkfrLiTCi7kEaJbq3sTtrdTQ07FeIIv8eM8Z0STuUXKcLBGeJWjUfktpkoo/gZ54nC1x8Ek78yPBq3EyN1RQa0Tjr5JVLX596PLsJvsMjqs124GwK6PnJZ3epolICF8+gqHiNbdRpJT7Ba6mT72vwEwomJM3pjsuqmSTPrYJQj8AfEwdBCTWQB+wzTNkTzFVWisj8lhKUR+mHT2NYKt1qbR9AUTEIrqf7TKGrrNpt85jWEKKLn0+7GYu1pJZSZg6MFLe; bm_sz=02DC15401318919816B068793C43E5FE~YAAQL13SF/aG+luCAQAAep08YxAcDRdhe6eVa5wXaa/7yIkWSjp8uUgDjBsc04OdsPWXgzlCuo8CwrZAaN10yjeg9Hhh90c6WOP4mMrIt4pMvQQ/MZAAQDOatOjToNQslPdtcCYD4oe6sRDBFV9fVaZ0Pe5tFJStTMt8SsQk541qLcIdMRvpAp+7YqNvs75CnEJTshlKbPIQozDuJzTdc21cvjvlmLZk5UmYdZC5KNqBmMGUFS9vXFBJ5/oB9gU+ET6IplwVGb11jHK8LX/EPFfcIrsJ/7HTBzWuy1WS9jSodnMAb8MlB24IM7XBlQz95So0keYHJgC5/OE=~4600642~4339513; mynt-loc-src=expiry:1659523733260|source:IP; AMP_TOKEN=$NOT_FOUND; _gat=1; cto_bundle=1ZFd1l9ZZ0xON0tpRXBwbGl4RlpqWEJhVkhPZ1VWM3RnQVdYY0dtQ21ZdDlsY2ZtN1VMa2RVbHpRMWozSkh3NzRDY0hDNndUdTFYczNQUmM3Vnl1MWtGZzNyWVR2VHUwd1hCcm4lMkZGZWJ5OGdodmxzR2h1THlVdjdEcEU0R3JBUUN2NkhMTHBwaHN2YzlhSkJQYWhKYk1yaDZDQSUzRCUzRA; bm_mi=646966F09F782F1FECC302141049FE74~YAAQL13SF6aI+luCAQAAt7M8YxDkesteVDJ8RcTTpLJcFeLB3hjgw2RFPMha2+seZmNXGetgtamnrZnvUgs5n8MWCLeCQ03CjYB7AKvlQOB/eBW3iJoEbsGKtLyFTy99BBnEIYXUMVQ9GDX03tMnuzoTgsGdItCAA6kc65p7GhWI1xFFF5RzKCqSdl7DF9DXI2DnpJZmTP+XSc/k10Z0yl3JUPKe8wJGR2jfOynn4UBp+4TBjJljlriLHCyGH2VGznjksl6nlZtAwwJCOiNWqliORm1usDACauZVk3f6f4jY4occwGX23Yq/g77lMKNyDjwv0yMseWvp~1; utrid=ZkF8VwhfHFIIRwRISEVAMCMzMzcyNjI3MzI4JDI=.e34d0e4585d8d70c532d1dfbbb4f2314; bm_sv=56BC5B63DAAE0FAE9C399BF9B2B4A534~YAAQL13SF9yI+luCAQAAD7Y8YxDLYHmUiRPNE6Gn+4OILmqadOglyteZcyUVq6f0P+luk6Jr3HB+p1EqcyX/yI52YctsrML9GNoQ8TbRipgCUIasSprw+Iyk0DU3y6rAOiAmrUDQQFoQrjM7qiY9q3/S/iLbHMNwD59MCXquQ2QCxKfScZEzO+ELhVnvZ6QyQwirn9A5puM0DCl5xgmPty3yGs47XHtjviiYxEf8olwknUDIJKdE9tIR8HmHeY/f~1; ak_RT="z=1&dm=myntra.com&si=a6945f2a-036c-4625-ad19-4f3b680f62f0&ss=l6dgq3io&sl=1&tt=4bl&rl=1&ld=4br&ul=91z"',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }

    for i in range(2):
        try:
            time.sleep(1)
            resp = requests.get(produrl, headers=headers, timeout=30)
            if resp.status_code == 200:
                break
        except Exception as e:
            print(str(e))
            if i > 0:
                return produrl + ' ^^ ' + str(e), 'Error'

    try:
        prodtree = html.fromstring(resp.text)
        JSON = prodtree.xpath('//body//script//text()')[2].replace("window.__myx = ","")
        jsondata = str(JSON).replace("\\u002F","/").replace("\\u003","/").strip()
        jsondata1 = json.loads(jsondata)
        date_format = '%Y-%m-%d %I:%M:%S:%Z'
        date = datetime.now(tz=utc)
        date = date.astimezone(timezone('Asia/Kolkata'))
        pstDateTime = date.strftime(date_format)
        pstDateTime = "'" + str(pstDateTime) + "'"

        attribute_header = jsondata1['searchData']['results']['filters']['primaryFilters']
        totalalphabets = len(attribute_header)
        for a in range(totalalphabets):

            try:
                attrname = jsondata1['searchData']['results']['filters']['primaryFilters'][a]['id']
                attr1name = str(attrname).replace("_facet","")
                # Category_name = str(produrl).replace("https://www.myntra.com/","").split("?")

                filter_by = jsondata1['searchData']['results']['filters']['primaryFilters'][a]['filterValues']
                len_subcategory =len(filter_by)
                for i in range(len_subcategory):
                    try:
                        Filter_id = jsondata1['searchData']['results']['filters']['primaryFilters'][a]['filterValues'][i]['id']
                        if str(Filter_id).isdigit():
                            try:
                                Filter_id = "'" + str(Filter_id) + "'"
                            except:
                                Filter_id = Filter_id
                    except:
                        Filter_id = 'n/a'

                    try:
                        Filter_count =jsondata1['searchData']['results']['filters']['primaryFilters'][a]['filterValues'][i]['count']
                    except:
                        Filter_count = 'n/a'
                    try:
                        Filter_url = str(produrl)+'?f='+str(attr1name)+'%3A'+str(Filter_id)
                    except:
                        Filter_url = 'n/a'
                    print(recno)
                    print(attr1name)
                    record = [recno, cat_name, attr1name, Filter_id, Filter_count, Filter_url, pstDateTime, produrl]
                    for z in range(len(record)):
                        record[z] = str(record[z]).replace('\n', '').replace('\t', '')
                        record[z] = str(record[z]) + '\t'
                    record.append('\n')
                    with open(
                            r'D:\OneDrive\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Script\Myntra\myntraLHN_Output ' + str(
                                crawled_date) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
                        fp.writelines(record)
            except:
                attr1name = 'n/a'

            attribute_header = jsondata1['searchData']['results']['filters']['rangeFilters']
            totalalphabets = len(attribute_header)
            for a in range(totalalphabets):

                try:
                    attrname = jsondata1['searchData']['results']['filters']['rangeFilters'][a]['id']
                    attr1name = str(attrname).replace("_facet", "")
                    if attr1name == 'Brand':
                        attr1name = 'Brands'
                    if str(attr1name).isdigit():
                        attr1name = "'" + str(attr1name) + "'"
                    # Category_name = str(produrl).replace("https://www.myntra.com/","").split("?")

                    filter_by = jsondata1['searchData']['results']['filters']['rangeFilters'][a]['filterValues']
                    len_subcategory = len(filter_by)
                    for i in range(len_subcategory):
                        try:
                            Filter_id = \
                            jsondata1['searchData']['results']['filters']['rangeFilters'][a]['filterValues'][i]['id']
                            Filter_id = str(Filter_id).replace('.0 TO 100.0', '% and above')
                        except:
                            Filter_id = 'n/a'

                        try:
                            Filter_count = \
                            jsondata1['searchData']['results']['filters']['rangeFilters'][a]['filterValues'][i][
                                'count']
                        except:
                            Filter_count = 'n/a'
                        try:
                            Filter_url = str(produrl) + '?f=' + str(attr1name) + '%3A' + str(Filter_id)
                        except:
                            Filter_url = 'n/a'
                        print(recno)
                        print(attr1name)
                        record = [recno, cat_name, attr1name, Filter_id, Filter_count, Filter_url, pstDateTime, produrl]
                        for z in range(len(record)):
                            record[z] = str(record[z]).replace('\n', '').replace('\t', '')
                            record[z] = str(record[z]) + '\t'
                        record.append('\n')
                        with open(
                                r'D:\OneDrive\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Script\Myntra\myntraLHN_Output ' + str(
                                        crawled_date) + '.txt', 'a+', newline='', encoding="utf-8") as fp:
                            fp.writelines(record)
                except:
                    attr1name = 'n/a'


    except Exception as e:
        print(str(e))

###################################################################################################
############################## left Hand Navigation ###############################################
###################################################################################################
crawled_date = date.today()
row = ['Sr. No.', 'Category_name','Attribute_Header', 'Filter_id',  'Filter_count', 'Filter_url' , 'TimeStamp', 'INPUT URL']
for z in range(len(row)):
    #record[z] = str(record[z]).replace('\n', '').replace('\t', '')
    row[z] = str(row[z]) + '\t'
row.append('\n')
with open(r'D:\OneDrive\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Script\Myntra\myntraLHN_Output ' + str(crawled_date) +'.txt', 'a+', newline='', encoding="utf-8") as fp:
    fp.writelines(row)
prdlist=list()
raw_data = pd.read_excel(r"D:\OneDrive\OneDrive - CONTEXIO LLP\Desktop\Crawling\Python Project\Script\Myntra\myntra1.xlsx")
raw_dataf = pd.DataFrame(raw_data)
urllist = raw_dataf['URL'].tolist()
recno1 = raw_dataf['Record No'].tolist()
cat_name1 =raw_dataf['Category_name'].tolist()
for j, produrl in enumerate(urllist):
    try:
        recno = recno1[j]
        cat_name =cat_name1[j]
        #cat_name = "Women's Clothing"
        #produrl = 'https://www.myntra.com/women%27s-clothing?f=Brand%3AVero%20Moda'
        pdp = productcrawl(produrl)
        print('URL crawled')
    except:
        print('Error')
print('Done')