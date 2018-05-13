# WebScrapingHomeWork
</br>
* For Part I of the Home Work , I have used Jupyter notebook to scrape the NASA Website to get infornation about planet Mars.
</br>
*** Please make sure that chromeexplorer.exe is in your folder ***
</br>
File name : mission_to_mars.ipynb
</br>
* Please run the cells in order and the output will be rendered
</br>
* The NASA web site apparently needs splinter to visit their website. Using the regular request / response renders an obsolete
web page.
</br>
* The critical part of Part I is generating a list of the title and image_url for the pictures rendered from
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/
</br>
* This dictionary will be used in the Python file mars_scrape.py to render a Web Page using Flask.
</br>
* In mars_scrape.py there is a method called "scrape" that uses Beautiful Soup to scrape the URL and return a list of dictionaries to app.py, that renders a Web page when you type localhost:5000/scrape.
</br>
* Multiple things happen here 
</br>
* The app.py program write to the mongo database. This can be verified by using the "mongo" prompt and running the command 
db.mars_images.find(). Please mote the DB is app(the name of the app in app.py, mars_images is the collection name. 
</br>
On running this command we see that the dictionary generated from mars_scrape.scrape is saved in the Mongo databse.
</br>

