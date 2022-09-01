# Data Viz with Python and JavaScript

Back in 2020 I was without a job and having not learned much in the previous gig (only Bash and C) a friend kindly borrowed me a book that linked Python and JavaScript. I decided to follow every page and run all the sample code, to finnaly build a web app to display the Nobel Winners of all the categories with data scraped from Wikipedia.

Book: Data-visualization with Python and JavaScript by Kyran Dale (2013 print).

This repository is to learn:<br> 
Back-End: Python (using Scrapy, MongoDB and Eve)<br>
Front-End: JavaScript (using D3.js v4).<br>

## caveats
The book uses a deprecated version of Scrapy, and D3.v3. It complicates the scrapping process, the outcome is not as shown on the book or [page](https://www.kyrandale.com/visualizing-the-nobel-prize-winners/). Data is updated up to 2014. This repo scrapes data upto 2020, and does not make use of a database, like mongo. I think with the data stored in a JSON file and search app the web app could run. It does NOT. 

## Running Environment
- OS: MacOS 15.5
- Python: v3.8
	- Scrapy v2.3.0
	- Eve 1.1.3
	- matplotLib 3.3.1
- D3: v4
