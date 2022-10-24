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

#------------------

## Country GDPs

- https://countryeconomy.com/countries/groups/european-union


#import
url_2 = "https://countryeconomy.com/countries/groups/european-union"

#request
html2 = requests.get(url_2)
html2

#show content
html2.content

#revise with Soup 
soup_1 = BeautifulSoup(html2.content, "html.parser")
soup_1

#Scrap data 
economic = '"https://countryeconomy.com/countries/groups/european-union"
my_table1 = pd.read_html(distance)[0]
my_table1

#remove symbol 
economic_info["Countries"] = economic_info["Countries"].str.extract(r"(\w{1,})")


#-----------------

## Distance from Ukraine 

- https://www.distancefromto.net/distance-from-ukraine-country


# scrape data
distance = 'https://www.distancefromto.net/distance-from-ukraine-country'
my_table2 = pd.read_html(distance)[0]
my_table2

#name change
distance_df = my_table2

#rename columns
distance_df.rename(columns = {'Distance':'Distance from Ukraine', 'Country':'Countries to sort'}, inplace = True)

#show unique column values
distance_df["Countries to sort"].unique()

# Merging EU Economic Data with Refugee Data
def merge_dataframe(df1,df2,column):
    
    return pd.merge(df1,df2,how='outer', on=column, left_index=False, right_index=False, sort=True)

new_data_frame = merge_dataframe(economic_info,refugee_df,"Countries")

#drop columns
new_data_frame.drop([13, 17, 21, 23, 27, 32, 33, 34], axis = 0, inplace = True)

# regrez to remove km from distance
distance_df["Distance from Ukraine in km"] = distance_df["Distance from Ukraine in km"].str.extract(r"(\d,\d{1,})")

#organise 
distance_df.sort_values(by='Distance from Ukraine in km',ascending=True)

#drop extra rows
distance_df.drop([0, 1, 2, 3, 4, 245, 246, 247, 248, 249], axis = 0, inplace = True)
distance_df.drop([5, 6, 7, 8, 9, 240, 242, 243, 244], axis = 0, inplace = True)
distance_df.drop([10, 12, 13, 14, 236, 237, 238, 239], axis = 0, inplace = True)
distance_df.drop([15, 17, 18, 232, 233, 235], axis = 0, inplace = True)

#change value name
distance_df['Countries to sort'].replace('Distance from Romania to Ukraine', 'Romania', inplace=True)
distance_df['Countries to sort'].replace('Distance from Sweden to Ukraine', 'Sweden', inplace=True)
distance_df['Countries to sort'].replace('Distance from Slovenia to Ukraine', 'Slovenia', inplace=True)


#add missing values 
distance_df.at[21,'Distance from Ukraine in km']= 767
distance_df.at[94,'Distance from Ukraine in km']= 881
distance_df.at[127,'Distance from Ukraine in km']= 905
distance_df.at[168,'Distance from Ukraine in km']= 941
distance_df.at[177,'Distance from Ukraine in km']= 541
distance_df.at[190,'Distance from Ukraine in km']= 844

#merge 3rd dataframe
def merge_dataframe_two(df1,df2,column):
    
    return pd.merge(df1,df2,how='outer', on=column, left_index=False, right_index=False, sort=True)

project_data = merge_dataframe_two(new_data_frame,distance_df,"Countries")

#final clean for project_date

#drop rows
project_data.drop([16], axis = 0, inplace = True)

#replace
project_data.replace({",":"."}, inplace=True, regex=True)

#column name change
col_list = ['Annual GDP (M.€.)', 'Annual GDP (M.$.)','GDP per capita (€)','GDP per capita.1 ($)','Distance from Ukraine in km']

for col in col_list:
    project_data[col] = project_data[col].str.replace(r'.', '', regex=True)
    
project_data

#convert data types
convert_dict = {'Annual GDP (M.€.)': float,
                'Annual GDP (M.$.)': float,
                'GDP per capita (€)': float,
                'GDP per capita.1 ($)': float,
                'Distance from Ukraine in km': float
                }

project_data = project_data.astype(convert_dict)
print(project_data.dtypes)
