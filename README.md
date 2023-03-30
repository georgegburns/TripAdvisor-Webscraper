# TripAdvisor-Webscraper
Python code to scrape reviews from a TripAdvisor URL

The TripAdvisorScraper() takes 2 required variables, url (the url of the reviews) and pages (the number of pages you want scraped). 

There are a further two optional variables, name (the name you want the reviewed site/restaurant to have) and add (if you want to load a pandas df to append the reviews to). 

The function then ouputs on your desktop a .csv file with the columns: 'Date of Review', 'Rating', 'Review', 'Website','Site', 'Type Of Visitor'
