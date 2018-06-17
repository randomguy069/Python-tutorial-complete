import bs4, requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c= r.content
soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify())
#cached version URL -> http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=10.html
all = soup.find_all("div", {"class": "propertyRow"})
x = all[0].find("h4", {"class" , "propPrice"}).text.replace("\n","")
page_nr = soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr)
l =[]
for page in range(0,int(page_nr) * 10 ,10):
    base_url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
    print(base_url)
    r = requests.get(base_url+str(page)+".html?v=0")
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})


    for item in all:
        d={}
        d["Address"] = item.find_all("span",{"class", "propAddressCollapse"})[0].text
        d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","") #oterates thru all the prices
        d["Locality"]=item.find_all("span",{"class", "propAddressCollapse"})[1].text
        try:
            d["Beds"] = item.find("span",{"class","infoBed"}).find("b").text #to get number of beds
        except:
            d["Beds"] = None

        try:
            d["Area"]= item.find("span",{"class","infoSqFt"}).find("b").text #to get square feet
        except:
            d["Area"] = None

        try:
            d["Full Baths"]= item.find("span",{"class","infoValueFullBath"}).find("b").text #to get number of baths
        except:
            d["Full Baths"] = None

            try:
                d["Half Baths"] = item.find("span",{"class","infoValueHalfBath"}).find("b").text #to get number of baths
            except:
                d ["Half Baths"] = None

        for column_group in item.find_all("div", {"class" , "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class" : "featureGroup"}), column_group.find_all("span",{"class": "featureName"})):
                if "Lot Size" in feature_group.text :
                    print(feature_name.text)
        l.append(d)


import pandas
df = pandas.DataFrame(l)
print(df)
df.to_csv("output.csv")
