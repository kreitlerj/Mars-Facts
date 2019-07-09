# Mars Facts Web Page
The purpose of this project is to demonstrate web scraping using Python and storing the scraped data in a non-relational database using MongoDB.

#### -- Project Status: [Completed]

### Technologies
* Python
* MongoDB
* Beautifal Soup, pandas, Pymongo
* Jupyter Notebook
* HTML
* Flask
* Chromedriver

## Descripton
Using a jupyter notebook, initial web scraping is performed using the Python library [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). All the code for web scraping is copied into a python file to create a function to perform all the scraping at once. Using Pymongo in the function, the data is stored in a MongoDB database.  This function is called into the app.py file.  The app.py file is a flask app that is a single page app that allows the user to view all the scraped data. Once the app is opened, the user can view a Mars fact from NASA's twitter page, the weather on Mars, the featured Mars image on NASA's website, and images of every one of Mars' Hemispheres.
