#importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas
#creating random data

df = pandas.read_csv("bob.csv")
x = df["x"]
y = df["y"]

#prepare output file
output_file("line_from_csv.html")
#creating figure object instance
f = figure()
f.circle(x,y)
show(f)
print(dir(f))
