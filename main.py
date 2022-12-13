from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

SEARCH_QUERIES = ["Iwtglobal", "TCT Computer Solutions", "real Time Health Pte", "PCe Solutions", "denver it services", "nssit", "iceberg managed solutions"]

def search(query):
    link = f"https://www.google.com/search?q={query}+linkedin"
    parse(link)

# check if description or url contains company name or abbreviation
# Iwtglobal = iwt-global, e.t.
# nssit = north-star-strategic-it
def check():
    pass

def parse(link):
    driver.get(link)
    page_source = driver.page_source
    selector = Selector(text=page_source)
    links = selector.xpath("//div[contains(@class, 'yuRUbf')]/a/@href").extract()
    firstlink = str(links[0])
    seclink = str(links[1])
    # check if first link is the same as second
    # https://www.linkedin.com/company/iwt-global = https://ph.linkedin.com/company/iwt-global
    if firstlink.rsplit("/")[4] == seclink.rsplit("/")[4] or check():
        print(firstlink)
    else:
        print("None")
    # name = selector.xpath("//h3[contains(@class, 'LC20lb MBeuO DKV0Md')]/text()").extract_first()

def main():
    for query in SEARCH_QUERIES:
        search(query)

main()
