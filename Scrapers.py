import os
import time
from datetime import date

import bs4 as bs
import pandas as pd
import requests
from CleaningFunctions import ReviewPunctuationCleaner, TripAdivsorDatecleaner

DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
TODAY = date.today()

def TripAdvisorScraper(url : str, pages=None, name=None, add=pd.DataFrame()):
    
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
    WORKING = True
    NUM = 0
    PAGES = pages
    ALLREVIEWS = []
    ALLSITES = []
    ALLWEBSITES = []
    ALLRATINGS = []
    ALLTYPES = []
    ALLDATES = []
    ALLTITLES = []
    
    """
    
    Scraping the data
    
    """
    
    print(f"Starting to Webscrape {name} Reviews")
    
    while WORKING:
        
        QUERY = "-or" + str(NUM) + "-"
        if NUM != 0:
            URL = HEAD + QUERY + TAIL
        PAGE = requests.get(URL, headers=HEADERS)
        HTML = PAGE.content
        SOUP = bs.BeautifulSoup(HTML, 'html.parser')
        
        REVIEWS = [review_selector.find('span', class_ ="yCeTE").text for review_selector in SOUP.find_all('div', class_="fIrGe _T bgMZj") if review_selector.find('span', class_ ="yCeTE") != None]
        SITE = [name for i in range(len(REVIEWS))]
        TITLES = [review_selector.find('span', class_="yCeTE").text for review_selector in SOUP.find_all('div', class_ = '_c') if review_selector.find('span', class_="yCeTE") != None]
        WEBSITE = ['TripAdvisor' for i in range(len(REVIEWS))]
        RATINGS = [review_selector.find('svg', class_="UctUV d H0")['aria-label']for review_selector in SOUP.find_all('div', class_ = '_c') if review_selector.find('svg', class_ ="UctUV d H0") != None]
        TYPES = [review_selector.find('div', class_ ="RpeCd").text if review_selector.find('div', class_ ="RpeCd") != None else "• Unknown" for review_selector in SOUP.find_all('div', class_ = '_c')]
        DATES = [review_selector.find('div', class_ ="biGQs _P pZUbB ncFvv osNWb").text for review_selector in SOUP.find_all('div', class_ = '_c') if review_selector.find('div', class_ ="biGQs _P pZUbB ncFvv osNWb") != None]
        
        if len(TYPES) > len(REVIEWS):
            TYPES = TYPES[1:len(REVIEWS)+1]
            
        print(f'Page {CURRENT} complete')
        
        if NUM != 0:
            if not REVIEWS:
                WORKING = False
            elif PAGES and CURRENT >= PAGES:
                WORKING = False
        
        for i in range(len(REVIEWS)): 
                ALLREVIEWS.append(REVIEWS[i])
                ALLSITES.append(SITE[i])
                ALLWEBSITES.append(WEBSITE[i])
                ALLRATINGS.append(RATINGS[i])
                ALLTYPES.append(TYPES[i])
                ALLDATES.append(DATES[i])
                ALLTITLES.append(TITLES[i])
        CURRENT += 1
        NUM += 10 
    
    print("Finished Scraping")
    time.sleep(2)
    print("Starting to clean data")
        
    """

    Cleaning the data

    """
    COLUMNS = ('Date of Review', 'Rating', 'Title', 'Review', 'Website','Site', 'Type Of Visitor')
    TEMP = list(zip(ALLDATES, ALLRATINGS, ALLTITLES, ALLREVIEWS, ALLWEBSITES, ALLSITES, ALLTYPES))
    TEMP = pd.DataFrame(TEMP,columns=COLUMNS)
    TEMP['Date of Visit'] = TEMP['Type Of Visitor'].str.split('\u2022', expand=True)[0].str.strip()
    TEMP['Type Of Visitor'] = TEMP['Type Of Visitor'].str.split('\u2022', expand=True)[1].str.strip()
    TEMP['Type Of Visitor'] = TEMP['Type Of Visitor'].str.replace("Unknown", " ")
    TEMP['Rating'] = TEMP['Rating'].str[:1]
    TEMP['Rating'] = pd.to_numeric(TEMP['Rating'])
    ReviewPunctuationCleaner('Review', TEMP)
    TripAdivsorDatecleaner('Date of Review', TEMP)
        
    """

    Exporting the data

    """
    print(f'{name} is complete')
    if add.empty: 
        TEMP.to_csv(DESKTOP + f"/TripAdvisorReviews.csv", index=False, encoding="utf-8")
    else: 
        OUTPUT = pd.concat([add, TEMP]).reset_index(drop=True)
        OUTPUT['Date of Review'] = pd.to_datetime(OUTPUT['Date of Review'], format="%Y-%m-%d")
        OUTPUT.drop_duplicates(subset=['Date of Review', 'Rating', 'Review', 'Website','Site'], keep="last", inplace=True)
        OUTPUT.to_csv(DESKTOP + "/TripAdvisorReviews.csv", index=False, encoding="utf-8")