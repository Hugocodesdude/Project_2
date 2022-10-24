# Project_2

# Title: The EU and Ukrainian refugees.

A comparative review of EU member states economic metrics and Ukrainian refugee numbers. 
---------
## Table of contents
1. Project Focus
2. Questions & Hypothesis 
3. Tools & Method
4. Code breakdown 
5. Visualisation 

## 1. Project Focus
To invesitgate whether there is a relationship between EU memberstate's economic strength (understood in terms of GDP) and the amount of Ukrainian refugees hosted by these countries. 


----------
## 2. Questions & Hypothesis 
- Do countries with a higher GDP accept larger quantites of refugees? 
- Is there a correlation between refugee numbers and distance to Ukraine? 
- Can larger EU economies accept more refugees? 

Hypothesis: Countries with a closer proximity to Ukraine have a higher intake of refugees. However that have displayed an 'open boarder' policy in recent to refugees would also accept higher numbers. I believe there to be a moral case for EU member states with a high GDP rate to accept more refugees.
 

--------
## Tools & Method 


For this particular project we had to demonstrate usage of APIs, webscraping or both. I scraped three websites for the data used for this project. 

1. EU member state economic infomation: https://countryeconomy.com/countries/groups/european-union
2. Refugee numbers: https://www.statista.com/statistics/1312361/europe-temporary-protection-for-persons-fleeing-ukraine/
3. Distance from Ukraine: https://www.distancefromto.net/distance-from-ukraine-country

I imported the following tools to run the code: 

```python
import matplotlib.pyplot as plt
from matplotlib import rcParams
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams



