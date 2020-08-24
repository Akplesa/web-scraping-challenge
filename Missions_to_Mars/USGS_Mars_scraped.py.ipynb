{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing dependencies \n",
    "import pandas as pd \n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist\n",
    "from lxml import html\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Establishing chrome driver executable path\n",
    "def init_browser():\n",
    "    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initializing Nasa Mars News Site communication with webpage\n",
    "def scrape_info():\n",
    "\n",
    "    browser=init_browser()\n",
    "#Visiting Nasa News url\n",
    "Nasa_News_url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(Nasa_News_url)\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scraping Nasa Mars News titles and paragraphs\n",
    "html= browser.html\n",
    "news_soup = bs(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')\n",
    "slide_elem.find(\"div\", class_='content_title')\n",
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "slide_elem.find(\"div\", class_='article_teaser_body')\n",
    "news_p = slide_elem.find(\"div\", class_='article_teaser_body').get_text()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initializing Nasa Mars Image Site communication with webpage\n",
    "img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(img_url)\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scraping Nasa Mars Images\n",
    "html= browser.html\n",
    "img_soup = bs(html, 'html.parser')\n",
    "featured_image_path = img_soup.find('a', class_='button fancybox').get('data-fancybox-href').strip()\n",
    "featured_image_url = img_url + featured_image_path\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initializing Nasa Mars Facts Site communication with webpage\n",
    "Mars_facts_url= 'https://space-facts.com/mars/'\n",
    "table = pd.read_html(Mars_facts_url)\n",
    "table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Selecting only the first dataframe\n",
    "df = table[0]\n",
    "# Displaying the html table string\n",
    "html_table = df.to_html(header= False, index= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initializing Nasa Mars hemispheres Site communication with webpage\n",
    "USGS_url= 'https://astrogeology.usgs.gov'\n",
    "Hemispheres_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(Hemispheres_url)\n",
    "browser.is_element_present_by_css(\"h3\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scraping Titles/Images using forloop\n",
    "html= browser.html\n",
    "facts_soup = bs(html, 'html.parser')\n",
    "imgs= facts_soup.find_all('div', class_='item')\n",
    "img_title_url=[]\n",
    "for img in imgs:\n",
    "    img_urls= img.find('a', class_= 'itemLink product-item')['href']\n",
    "    titles= img.find_all('h3')\n",
    "    #Accessing image urls to scrape ENHANCED JPG IMAGES\n",
    "    browser.visit(USGS_url + img_urls)\n",
    "    html_jpg= browser.html\n",
    "    jpg_soup= bs( html_jpg,'html.parser')\n",
    "    #Scraping url for ENHANCED JPG IMG\n",
    "    jpg_url = USGS_url + jpg_soup.find('img', class_='wide-image')['src']\n",
    "    #Appending dictionary with image url strings \n",
    "    img_title_url.append({'Title':titles, 'Img_url': jpg_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Constructing Python Dictionary\n",
    "\n",
    "scraped_MTM = {\n",
    "        'News title': news_title,\n",
    "        'News paragraph': news_p,\n",
    "        'Featured image url': featured_image_url,\n",
    "        'Mars facts table': html_table,\n",
    "        'Enhanced jpg Images': img_title_url, \n",
    "}\n",
    "\n",
    "browser.quit()\n",
    "\n",
    "return mars_items"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
