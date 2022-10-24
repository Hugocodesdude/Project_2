import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

#---------------

## Web-scraping Statisa for Refugee Info: 

- Refugees from Ukraine registered for Temporary Protection or similar national protection schemes in Europe from February 24 to October 4, 2022, by selected country(in 1,000s

- https://www.statista.com/statistics/1312361/europe-temporary-protection-for-persons-fleeing-ukraine/

#import
url = "https://www.statista.com/statistics/1312361/europe-temporary-protection-for-persons-fleeing-ukraine/"

#request
html = requests.get(url)
html

#show content
html.content

#revise with Soup 
soup = BeautifulSoup(html.content, "html.parser")
soup



