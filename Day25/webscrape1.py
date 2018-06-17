import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonhow.com/example.html")
c= r.content

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all = soup.find_all("div",{"class":"cities"})
#to return just one element :-> all = soup.find("div",{"class":"cities"})


#print(all[0].find_all("h2")[0].text)
for i in range(3):
    x = all[i].find_all("h2")[0].text
    print(x)
