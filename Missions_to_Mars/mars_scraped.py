# Importing dependencies 
import pandas as pd 
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from lxml import html


# Establishing chrome driver executable path 
def init_browser():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

#Visiting Nasa News / Scraping
Nasa_News_url = 'https://mars.nasa.gov/news/'
browser.visit(Nasa_News_url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

html= browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')
news_title = slide_elem.find("div", class_='content_title').get_text()
slide_elem.find("div", class_='article_teaser_body')
news_p = slide_elem.find("div", class_='article_teaser_body').get_text()

#Visiting JPL MARS SPACE IMAGES / Scraping
img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(img_url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

html= browser.html
img_soup = bs(html, 'html.parser')
featured_image_path = img_soup.find('a', class_='button fancybox').get('data-fancybox-href').strip()
featured_image_url = img_url + featured_image_path

#Visiting JPL MARS MARS FACTS / Scraping
Mars_facts_url= 'https://space-facts.com/mars/'
table = pd.read_html(Mars_facts_url)

#Selecting only the first dataframe
df = table[0]

# Displaying the html table string
html_table = df.to_html(header= False, index= False)

#Visiting MARS HEMISPHERES/ Scraping using forloop

USGS_url= 'https://astrogeology.usgs.gov'
Hemispheres_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(Hemispheres_url)
browser.is_element_present_by_css("h3", wait_time=1)

html= browser.html
facts_soup = bs(html, 'html.parser')

imgs= facts_soup.find_all('div', class_='item')
img_title_url=[]
for img in imgs:
    img_urls= img.find('a', class_= 'itemLink product-item')['href']
    titles= img.find_all('h3')
    #Accessing image urls to scrape ENHANCED JPG IMAGES
    browser.visit(USGS_url + img_urls)
    html_jpg= browser.html
    jpg_soup= bs( html_jpg,'html.parser')
    #Scraping url for ENHANCED JPG IMG
    jpg_url = USGS_url + jpg_soup.find('img', class_='wide-image')['src']
    #Appending dictionary with image url strings 
    img_title_url.append({'Title':titles, 'Img_url': jpg_url})


    #Constructing python dictionary for all of the scraped mars information
    USGS_Mars_scraped = {
        'News_title': news_title,
        'News_paragraph': news_p,
        'Featured_image_url': featured_image_url,
        'Mars_facts_table': html_table,
        'Images': img_title_url,
    }

    browser.quit()
    return mars_records