import string

import pandas as pd
from ReviewDictionaries import MONTHS, UNICODE


def TripAdivsorDatecleaner(column_name : str, df=pd.DataFrame()):
    CHANGE = MONTHS
    CLEAN_DATES = []
    for row in df[column_name]:
        if row != None:
            year = row.split()[3]
            month = row.split()[2]
            day = row.split()[1]
            for word, replacement in CHANGE.items():
                if month == word:
                    month = month.replace(word,str(replacement))
                    date_fixed = "-".join([year,month,day])
                    CLEAN_DATES.append(date_fixed)
                    break
                continue
        else:
            CLEAN_DATES.append(None)
    df[column_name] = CLEAN_DATES
    df[column_name] =pd.to_datetime(df[column_name], format="%Y-%m-%d")

def OutputDateCleaner(column_name : str, df=pd.DataFrame()):
    CLEAN_DATES = []
    for row in df[column_name]:
        print(row)
        if row != None:
            try:
                row = row[:10].strip()
                year = row.split("/")[2]
                month = row.split("/")[1]
                day = row.split("/")[0]
            except:
                year = row.split("-")[2]
                month = row.split("-")[1]
                day = row.split("-")[0]
            CLEAN_DATES.append("/".join([year,month,day]))
    df[column_name] = CLEAN_DATES
    df[column_name] =pd.to_datetime(df[column_name], format="%Y/%m/%d")
    
def ReviewPunctuationCleaner(column_name : str, df=pd.DataFrame()):
    CLEAN_REVIEWS = []
    for i in df[column_name]:
        encoded_review = i.encode(encoding="UTF-8")
        encoded_review = encoded_review.decode(encoding='UTF-8', errors='strict')
        CLEAN_REVIEWS.append(encoded_review)
    df[column_name] = CLEAN_REVIEWS
