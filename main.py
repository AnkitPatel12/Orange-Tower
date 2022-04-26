# importing modules
import requests
from bs4 import BeautifulSoup
import re
import datetime
import datefinder


# providing url
url = "https://tower.utexas.edu/lighting-updates/"

# opening the url for reading
# parse the html file
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")  

#sort through scrape data
#store the data found 
pattern = "^The*"
orange = doc.find_all(text= re.compile(pattern))

#get the first secntence of the most recent data
data_holder = orange[0].split('.',1)
# print(data_holder[0])


#finds the date of the most recent data holder
matches = datefinder.find_dates(data_holder[0])
for match in matches:
    date_of_lit = match

#get todays date
date_today = datetime.datetime.now()

# check if there is any upcoming tower lighting
if (date_of_lit >= date_today):
    print(data_holder[0])
else:
    print("There are no upcoming Tower lightings.")
 
    




# for count,x in enumerate(orange):
#     #   print(x.strip() +str(count))
#       x.strip()
#       data_holder = (str(x.split('.',1)) +str(count))
   
# print(data_holder)

#print(orange)
# getting all the paragraphs
# for para in htmlParse.find_all("The UT Tower"):
#     print(para.get_text())