# TripAdvisor-Webscraper
Python code to scrape reviews from a TripAdvisor URL

The TripAdvisorScraper() takes 1 required variable, url (the url of the reviews). 

There are a further three optional variables, pages (the number of pages you want scraped, defaults to all), name (the name you want the reviewed site/restaurant to have, defaults to the name in the URL string) and add (if you want to load a pandas df to append the reviews to). 

The function then ouputs on your desktop a .csv file with the columns: 'Date of Review', 'Rating', 'Review', 'Website','Site', 'Type Of Visitor', 'Date of Visit'
