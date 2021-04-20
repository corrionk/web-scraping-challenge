#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as soup
from splinter import Browser
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[5]:


# Parse Results HTML with BeautifulSoup
# Find Everything Inside:
#   <ul class="item_list">
#     <li class="slide">

html = browser.html
news_soup = soup(html, "html.parser")
slide_element = news_soup.select_one("ul.item_list li.slide")


# In[6]:


slide_element.find("div", class_="content_title")


# In[7]:



# Scrape the Latest News Title
# Use Parent Element to Find First <a> Tag and Save it as news_title
news_title = slide_element.find("div", class_="content_title").get_text()
print(news_title)


# In[8]:


# Scrape the Latest Paragraph Text
news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
print(news_paragraph)


# In[9]:


# Visit the NASA JPL (Jet Propulsion Laboratory) Site
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[10]:


# Ask Splinter to Go to Site and Click Button with Class Name full_image
# <button class="full_image">Full Image</button>
url_image = "https://www.jpl.nasa.gov/images/"
browser.visit(url_image)
img_html = browser.html
img_soup = soup(img_html, 'html.parser')


# In[11]:


header=img_soup.find("h2", class_="mb-3 text-h5").text


# In[12]:


endpoint=header.replace(' ', '-').lower()
endpoint


# In[13]:


url_featured=url_image = "https://www.jpl.nasa.gov/images/" + endpoint
url_featured


# In[14]:


browser.visit(url_featured)
featured_html = browser.html
featured_soup = soup(featured_html, 'html.parser')


# In[15]:


featured_image=featured_soup.find('img', class_='BaseImage object-scale-down')['data-src']
featured_image


# In[17]:


table_url= "https://space-facts.com/mars/"
tables=pd.read_html(table_url)
tables


# In[19]:


df=tables[1]
mars_df=df[["Mars - Earth Comparison","Mars"]]
mars_df.columns=['Description','Value']
mars_df.set_index('Description', inplace=True)
mars_df


# In[20]:


html_table=mars_df.to_html()
html_table


# In[28]:


hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)


# In[29]:


hemisphere_image_urls = []
links = browser.find_by_css("a.product-item h3")
for i in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)
    browser.back()
    


# In[30]:


hemisphere_image_urls


# In[ ]:




