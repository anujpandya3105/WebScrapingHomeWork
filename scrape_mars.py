import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    #executable_path = {"executable_path": "C:\Users\anuj\webScrapingHW"}
    #return Browser("chrome", **executable_path, headless=False)
	return Browser("chrome",headless=False)
	
def scrape():
	browser = init_browser()
	mars_hemispheres_images = {}
	result = {}
	title_list = []
	url_list = []
	mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
	browser.visit(mars_hemisphere_url)
	html=browser.html
	soup = BeautifulSoup(html, 'html.parser')
	descriptions = soup.find_all('div', class_='description')
	print(descriptions)
	for description in descriptions:
		title = description.find('h3').text
		img_url = description.a['href']
		img_url = "/Mars/Viking/cerberus_enhanced"
		img_url_final = "https://astropedia.astrogeology.usgs.gov/download" + img_url + ".tif/full.jpg"
		print(title)
		print(img_url_final)
		title_list.append(title)
		url_list.append(img_url_final)
		
	result = zip(title_list, url_list)
	mars_hemispheres_images = dict(result)
	#title = ['hardcodedtit1', 'hardcodedtit2', 'hardcodedtit3', 'hardcodedtit4']
	#img_url_final = ['HCimg_url1', 'HCimg_url2', 'HCimg_url3', 'HCimg_url4']
	#result = zip(title, img_url_final)
	#mars_hemispheres_images = dict(result)
	
	#for i in range(0,4):
	#	mars_hemispheres_images = [
	#		{'title': title_list[0], 'img_url': url_list[0]},
	#		{'title': title_list[1], 'img_url': url_list[1]},
	#		{'title': title_list[2], 'img_url': url_list[2]},
	#		{'title': title_list[3], 'img_url': url_list[3]}
	#	]
	#mars_hemispheres_images = [
	#		{'title': "tit1", 'img_url': "img1"},
	#		{'title': "tit2", 'img_url': "img2"},
	#		{'title': "tit3", 'img_url': "img3"},
	#		{'title': "tit4", 'img_url': "img4"}
	#	]
	#mars_hemispheres_images = {'title': "titanuj", 'img_url': "imgAnuj"}
		
    
    
	return(mars_hemispheres_images)