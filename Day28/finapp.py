from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN
#open link for more files -> https://pandas-datareader.readthedocs.io/en/latest/
yf.pdr_override()
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,1,10)

df=data.get_data_yahoo(tickers="ORCL",start=start, end=end) #tickers is name of the stock
date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]
def inc_dec(c,o):
    if c > o :
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c,o) for c, o in zip (df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type = "datetime", width = 1000 , height = 300, responsive = True)
p.title.text= "Candlestick chart"
p.grid.grid_line_alpha = 0.3 #level of transparency

hours_12 = 12* 60 * 60 * 1000
p.segment(df.index, df.High, df.index, df.Low, color = "Black")

p.rect(df.index[df.Status == "Increase"] , df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color="#FF0000", color="black")
p.rect(df.index[df.Status == "Decrease"] , df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color="#6A5ACD", color="black")
script1, div1 = components(p)
cdn_js = CDN.js_files
cdn_css =CDN.css_files

print(script1)
print(div1)



#output_file("CS.html")
#show(p)
