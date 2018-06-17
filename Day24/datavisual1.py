#importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df = pandas.read_csv("adbe.csv",parse_dates=["Date"])

p = figure(width=500,height=500,x_axis_type="datetime",responsive=True)
p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)
output_file("output.html")
show(p)
