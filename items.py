# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from re import S
import scrapy


USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    Producttitle = scrapy.Field()
    Selling_price=scrapy.Field()
    Regular_price=scrapy.Field()
    Discount=scrapy.Field()
    Image=scrapy.Field()
    Reviews=scrapy.Field()
    Rating=scrapy.Field()
    Breadcrum=scrapy.Field()
    #Seller=scrapy.Field()
    Shippin_Import_Fees=scrapy.Field()
    Canonical_url=scrapy.Field()
    ShipBy=scrapy.Field()
    SoldBy=scrapy.Field()
    Marketplace_Seller=scrapy.Field()
    Availability=scrapy.Field()
    Shipping_Status=scrapy.Field()
    Url=scrapy.Field()
    Crawl_Date=scrapy.Field()
    technical_details=scrapy.Field()
    #Additional_Information=scrapy.Field()
    model=scrapy.Field()
    Brand=scrapy.Field()
    Special_Offer=scrapy.Field()
    UPC=scrapy.Field()
    ShippingPrice=scrapy.Field()
    Product_Information=scrapy.Field()
    featureHighlights=scrapy.Field()
    ProdcutDetails=scrapy.Field()
    SKU=scrapy.Field()
    Frequency=scrapy.Field()
    Sublot=scrapy.Field()
    Retailer=scrapy.Field()

    pass

class WalmartItem(scrapy.Item):
    # define the fields for your item here like:
    Producttitle=scrapy.Field()
    Title = scrapy.Field()
    RegularPrice=scrapy.Field()
    Image=scrapy.Field()
    Reviews=scrapy.Field()
    Rating=scrapy.Field()
    Breadcrum=scrapy.Field()
    Retailer_Name=scrapy.Field()
    Canonical_url=scrapy.Field()
    Availability=scrapy.Field()
    UPC=scrapy.Field()
    Brand=scrapy.Field()
    walmartItemNumber=scrapy.Field()
    Url=scrapy.Field()
    Price=scrapy.Field()
    StartRangeprice=scrapy.Field()
    EndRangeprice=scrapy.Field()
    Crawl_Date=scrapy.Field()
    manufacturer=scrapy.Field()
    model=scrapy.Field()
    sellerName=scrapy.Field()
    offers=scrapy.Field()
    specification=scrapy.Field()
    criteria=scrapy.Field()
    SKU=scrapy.Field()
    Frequency=scrapy.Field()
    Sublot=scrapy.Field()
    Retailer=scrapy.Field()  
    listPrice=scrapy.Field()  

    pass


class HomeDepotItem(scrapy.Item):
    Producttitle=scrapy.Field()
    Title = scrapy.Field()
    RegularPrice=scrapy.Field()
    Image=scrapy.Field()
    Reviews=scrapy.Field()
    Rating=scrapy.Field()
    Breadcrum=scrapy.Field()
    Retailer_Name=scrapy.Field()
    Canonical_url=scrapy.Field()
    Availability=scrapy.Field()
    Shipping_Status=scrapy.Field()
    UPC=scrapy.Field()
    Brand=scrapy.Field()
    Url=scrapy.Field()
    Price=scrapy.Field()
    StartRangeprice=scrapy.Field()
    EndRangeprice=scrapy.Field()
    Crawl_Date=scrapy.Field()
    manufacturer=scrapy.Field()
    model=scrapy.Field()
    sellerName=scrapy.Field()

    pass


class KohlsItem(scrapy.Item):
    Producttitle=scrapy.Field()
    Title = scrapy.Field()
    RegularPrice=scrapy.Field()
    Image=scrapy.Field()
    Reviews=scrapy.Field()
    Rating=scrapy.Field()
    Breadcrum=scrapy.Field()
    Retailer_Name=scrapy.Field()
    Canonical_url=scrapy.Field()
    Availability=scrapy.Field()
    UPC=scrapy.Field()
    UPC2=scrapy.Field()
    Brand=scrapy.Field()
    URL=scrapy.Field()
    Price=scrapy.Field()
    minPrice=scrapy.Field()
    maxPrice=scrapy.Field()
    Crawl_Date=scrapy.Field()
    manufacturer=scrapy.Field()
    model=scrapy.Field()
    priceType=scrapy.Field()
    Sale_Price=scrapy.Field()
    specialoffer=scrapy.Field()
    specialoffer1=scrapy.Field()
    specialoffer2=scrapy.Field()
    offer3=scrapy.Field()
    SKU=scrapy.Field()
    Daily_Biweekly_Flag=scrapy.Field()
    Brand_Type=scrapy.Field()
    Sublot=scrapy.Field()
    Retailer=scrapy.Field()
    Frequency=scrapy.Field()
    priceType2=scrapy.Field()
    offerExclusion=scrapy.Field()
    size=scrapy.Field()
    color=scrapy.Field()
    SKUprice=scrapy.Field()
    SKUregularprice=scrapy.Field()
    SKUavaibality=scrapy.Field()
    SKUminprice=scrapy.Field()

    pass


class WalmartCasearchItem(scrapy.Item):
    # define the fields for your item here like:

    CrawlDate=scrapy.Field()
    c2_productId=scrapy.Field()
    URL=scrapy.Field()
    Rank=scrapy.Field()
    p4_Product_url=scrapy.Field()
    xml_productid=scrapy.Field()
    p4_Title=scrapy.Field()


    pass

class MacysItem(scrapy.Item):
    Producttitle=scrapy.Field()
    RegularPrice=scrapy.Field()
    Brand=scrapy.Field()
    URL=scrapy.Field()
    Image=scrapy.Field()
    Reviews=scrapy.Field()
    Rating=scrapy.Field()
    Breadcrum=scrapy.Field()
    Canonical_url=scrapy.Field()
    Availability=scrapy.Field()
    Price=scrapy.Field()
    Offer2=scrapy.Field()
    ALLUPC=scrapy.Field()
    offer1=scrapy.Field()
    Crawl_Date=scrapy.Field()
    SKU=scrapy.Field()
    Sublot=scrapy.Field()
    Frequency=scrapy.Field()
    Retailer=scrapy.Field()
    tieredRegularPrice=scrapy.Field()
    tieredSalePrice=scrapy.Field()
    FinalPrice=scrapy.Field()
    ID=scrapy.Field()
    


    pass    

