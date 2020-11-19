# Web Scraping Overview

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

# Process 
## Scraping:
Initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.


## NASA Mars News:
I scraped the NASA Mars News Site: "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest" and collected the latest News Title and Paragraph Texts.

## JPL Mars Space Images - Featured Image:
Used splinter to navigate the mars site: "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url

## Mars Facts:
Used the mars facts webpage: " https://space-facts.com/mars/" to scrape the table containing facts about the planet including Diameter, Mass, etc and used Pandas to convert the data to a HTML table string.

## Mars Hemispheres:
Visited the USGS Astrogeology site: "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" to obtain high resolution images for each of Mar's hemispheres.

## MongoDB and Flask Application:
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.





