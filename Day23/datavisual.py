#importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show

#creating random data

x = [1,2,3,4,5]
y = [6,7,8,9,10]

#prepare output file
output_file("line.html")
#creating figure object instance
f = figure()
#create line plot
#f.line(x,y)
#f.scatter(x,y)
f.circle(x,y)
show(f)
print(dir(f))
