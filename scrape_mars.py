# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import pandas as pd
import time


def scrape():
    #Creating a path to open a browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Connect to a url for NASA's Mars website
    url_nasa_mars = "https://mars.nasa.gov/news"
    browser.visit(url_nasa_mars)
    time.sleep(1)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Scrape Latest article title and teaser on NASA's Mars website
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Connect to a url to grab NASA's featured Mars image
    url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_jpl)
    time.sleep(1)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Navigate to the page to scrape the full size featured image
    browser.click_link_by_partial_text('Full')
    time.sleep(1)
    url_jpl2 = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button')['data-link']
    browser.visit(url_jpl2)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('figure', class_='lede').a['href']

    # Connect to url for Mars Weather Twitter page
    url_mars_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_mars_twitter)
    time.sleep(1)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Scrape the latest weather from Mars
    mars_weather = soup.find('p', class_='TweetTextSize').text

    # Connect to url for Mars facts page and use pandas to scrape the table of Mars facts
    url_mars_facts = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(url_mars_facts)

    # Turn the table into a Dataframe
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Description', 'Value']
    mars_facts_df.set_index('Description', inplace=True)
    
    # Store the table as html
    mars_facts_html = mars_facts_df.to_html(justify='left')

    # Connect to url for Mars hemisphere images (Using the archive website since the actual one is down)
    url_mars_hemisphere = "http://web.archive.org/web/20181114171728/https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_hemisphere)
    time.sleep(1)

    # Scrape the images of each hemisphere
    hemisphere_image_urls = []
    hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']

    # Loop through the four pages containing the information
    for hemisphere in hemispheres:
        browser.click_link_by_partial_text(hemisphere)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_='title').text
        img_url = 'https://web.archive.org/' + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({'title': title, 'img_url': img_url})
        browser.back()
        time.sleep(1)
    
    # Close the browser window
    browser.quit()

    # Store all the scrapped data in a dictionary
    mars_scrape_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts_html": mars_facts_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    
    # Return the scrapped data dictionary
    return mars_scrape_data