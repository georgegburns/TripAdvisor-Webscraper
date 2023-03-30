import os

import pandas as pd
from Scrapers import TripAdvisorScraper

DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

PAGES = 1

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g1902845-d3597529-Reviews-WWT_Slimbridge_Wetland_Centre-Slimbridge_Cotswolds_England.html"
NAME = "Slimbridge"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g186338-d187534-Reviews-WWT_London_Wetland_Centre-London_England.html"
NAME = "London"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g644362-d261551-Reviews-WWT_Martin_Mere_Wetland_Centre-Burscough_Ormskirk_Lancashire_England.html"
NAME = "Martin Mere"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g186405-d297089-Reviews-WWT_Arundel_Wetland_Centre-Arundel_Arun_District_West_Sussex_England.html"
NAME = "Arundel"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g776264-d219276-Reviews-Llanelli_Wetland_Centre-Llanelli_Carmarthenshire_Wales.html"
NAME = "Llanelli"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g504187-d591659-Reviews-WWT_Washington_Wetland_Centre-Washington_Tyne_and_Wear_England.html"
NAME = "Washington"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g551732-d318705-Reviews-WWT_Castle_Espie_Wetland_Centre-Comber_County_Down_Northern_Ireland.html"
NAME = "Castle Espie"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g7176430-d1837805-Reviews-WWT_Welney_Wetland_Centre-Welney_Norfolk_East_Anglia_England.html"
NAME = "Welney"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g186513-d2038192-Reviews-WWT_Caerlaverock_Wetland_Centre-Dumfries_Dumfries_and_Galloway_Scotland.html"
NAME = "Caerlaverock"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

REVIEWS = pd.read_csv(DESKTOP + "/TripAdvisorReviews.csv")

URL = "https://www.tripadvisor.co.uk/Attraction_Review-g504115-d10091988-Reviews-WWT_Steart_Marshes-Bridgwater_Somerset_England.html"
NAME = "Steart"
TripAdvisorScraper(URL, PAGES, name=NAME, add=REVIEWS)

print("All Sites Complete")