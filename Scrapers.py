import os
import time
from datetime import date

import bs4 as bs
import pandas as pd
import requests
from CleaningFunctions import OutputDateCleaner, TripAdivsorDatecleaner

DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
TODAY = date.today()

def TripAdvisorScraper(url : str, pages : int, name=None, add=pd.DataFrame()):
    
    """ 
    
    Variables
    
    """
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'Accept-Enconding' : 'grip, deflate', 'Accept' : '*/*', 'Connection' : 'keep-alive'}
    URL = url
    if name == None:
        name = URL.split("-")[4]
    HEAD = "-".join([x for x in URL.split("-")[:4]])
    TAIL = "-".join([x for x in URL.split("-")[5:]])
    CURRENT = 0
    NUM = 0
    REVIEWS = []
    SITE = []
    WEBSITE = []
    RATINGS = []
    TYPES = []
    DATES = []
    
    """
    
    Scraping the data
    
    """
    
    print(f"Starting to Webscrape {name} Reviews")
    
    while CURRENT <= pages:
        
        QUERY = "-or" + str(NUM) + "-"
        if NUM != 0:
            URL = HEAD + QUERY + TAIL
        PAGE = requests.get(URL, headers=HEADERS)
        HTML = PAGE.content
        SOUP = bs.BeautifulSoup(HTML, 'html.parser')
        
        for review_selector in SOUP.find_all('div', class_ = "fIrGe _T bgMZj"):
            REVIEW = review_selector.find('span', class_ ="yCeTE")
            if REVIEW != None:
                REVIEWS.append(REVIEW.text)
                SITE.append(name)
                WEBSITE.append('TripAdvisor')
        
        for review_selector in SOUP.find_all('div', class_ = '_c'):
            RATING = review_selector.find('svg', class_ ="UctUV d H0")
            if RATING != None:
                RATINGS.append(RATING['aria-label'])
            TYPE = review_selector.find('div', class_ ="RpeCd")
            if TYPE != None:
                TYPES.append(TYPE.text)
            else:
                TYPES.append("• Unknown")
            DATE = review_selector.find('div', class_ ="biGQs _P pZUbB ncFvv osNWb")
            if DATE != None:
                DATES.append(DATE.text)
                
        print(f'Page {CURRENT} complete')
        
        CURRENT += 1
        NUM += 10 
    
    print("Finished Scraping")
    time.sleep(2)
    print("Starting to clean data")
        
    """

    Cleaning the data

    """
    COLUMNS = ('Date of Review', 'Rating', 'Review', 'Website','Site', 'Type Of Visitor')
    TEMP = list(zip(DATES, RATINGS, REVIEWS, WEBSITE, SITE, TYPES))
    TEMP = pd.DataFrame(TEMP,columns=COLUMNS)
    TEMP['Type Of Visitor'] = TEMP['Type Of Visitor'].str.split('\u2022', expand=True)[1].str.strip()
    TEMP['Type Of Visitor'] = TEMP['Type Of Visitor'].replace('Unknown', None)
    TEMP['Rating'] = TEMP['Rating'].str[:1]
    TEMP['Rating'] = pd.to_numeric(TEMP['Rating'])
    
    TripAdivsorDatecleaner('Date of Review', TEMP)
    
    """

    Exporting the data

    """
    print(f'{name} is complete')
    if add.empty: 
        TEMP.to_csv(DESKTOP + f"/TripAdvisorReviews.csv", index=False)
    else: 
        OutputDateCleaner('Date of Review', add)
        OUTPUT = pd.concat([add, TEMP]).reset_index(drop=True)
        OUTPUT.drop_duplicates(subset=['Date of Review', 'Rating', 'Review', 'Website','Site'], keep="last", inplace=True)
        OUTPUT.to_csv(DESKTOP + f"/TripAdvisorReviews.csv", index=False)