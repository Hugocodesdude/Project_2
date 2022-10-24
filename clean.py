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

#target data line
a = soup.select("tr")[1].getText()
a

# clean using function 
def extract(something):
    str_ = ''
    nums_ = ''
    
    for i in something.getText():
        if i.isdigit() == False:
            str_ = str_ + i
        else:
            nums_ = nums_ + i
    return str_.replace(".", "").replace(",", ""), nums_


#turn into list
new_list = list(map(extract, b))
new_list

#refine data
country_list = str(b).split(",")
country_list

#
country, pop = soup.select("tr")[1].getText().split(',')

#transform into DataFrame
refugee_df = pd.DataFrame(new_list)
refugee_df

#Remove first row
refugee_df = refugee_df.iloc[1:, :]
refugee_df

# Arrange column ascending 
refugee_df = refugee_df.sort_values(by = ["Country"], axis = 0, ascending=True)

# Rename column
refugee_df.rename(columns = {'Country' :' Countries'}, inplace = True)










