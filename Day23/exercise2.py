import pandas
from bokeh.plotting import figure
from bokeh.io import output_file,show

df = pandas.read_excel(open("weather.xlsx","rb"),sheet_name="Ark1")
#print(df)
x=df["Temperature"]
y=df["Pressure"]
output_file("exercise2.html")
f=figure()
f.scatter(x,y)
show(f)
