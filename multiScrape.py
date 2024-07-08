from datetime import datetime, date
from urllib.parse import urljoin, urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas
from pytz import timezone, utc
import json
from scrapy_splash import SplashRequest
from icecream import ic
import os
import re
import scrapy
from pathlib import Path
import sys
sys.path.append(r'W:\Python Crawling\StealthCrawlingScrapy')


# today = date.today()
# folder = 'CrawlerOutput\\Kohls\\'+str(today)+"\\p4\\output"
# Path(folder).mkdir(parents=True, exist_ok=True)
# now = datetime.now()
# fileaddres = folder+"\\kohls"+str(now).replace(':', '.')+".csv"
# print(fileaddres)
# kolhsettings = get_project_settings()
# kolhsettings['FEED_FORMAT'] = 'csv'
# kolhsettings['FEED_URI'] = fileaddres
# kohlsprocess = CrawlerProcess(kolhsettings)
# kohlsprocess.crawl(
#     'KohlsP4Excel', input=r"C:\Users\Divya\Desktop\InputData\12-8-2021 Demo\KohlsInput.csv")
# kohlsprocess.start()

# wayFairSettings = get_project_settings()
# wayFairProcess = CrawlerProcess(wayFairSettings)
# wayFairProcess.crawl(
#     'WayFairPageDump', input=r"C:\Users\Divya\Desktop\InputData\wayfairRem1.csv")
# wayFairProcess.start()

# cartersSetting = get_project_settings()
# castersProcess = CrawlerProcess(cartersSetting)
# castersProcess.crawl(
#    'cartersPageDump', input=r"M:\OneDrive - CONTEXIO LLP\Crawling\Inputs\JCP\Input 13-01-2022\Daily\Carters.csv")
# castersProcess.start()

today = date.today()
folder = 'CrawlerOutput\\Macys\\'+str(today)+"\\p4\\output"
Path(folder).mkdir(parents=True, exist_ok=True)
now = datetime.now()
fileaddres = folder+"\\Macys"+str(now).replace(':', '.')+".csv"
print(fileaddres)
macysSetting = get_project_settings()
macysSetting['FEED_FORMAT'] = 'csv'
macysSetting['FEED_URI'] = fileaddres
macysProcess = CrawlerProcess(macysSetting)
macysProcess.crawl(
    'MacysP4Excel', input=r"W:\OneDrive - CONTEXIO LLP\Crawling\Inputs\JCP\Input 22-04-2022\Daily\Macys.csv")
macysProcess.start()