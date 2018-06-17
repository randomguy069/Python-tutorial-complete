import folium,pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"]) #getting latitude from the Text file
lon = list(data["LON"]) #getting longitude from the Text file
elev = list(data["ELEV"]) #getting elevation from the Text file
map = folium.Map(location=[12.991,77.649], zoom_start =6)  #creation of map object
#bengaluru co-ordinates -> 12.979766,77.5925815
fgv= folium.FeatureGroup(name="Volcanoes") #to add multiple features
#fg.add_child(folium.Marker(location=[12.9913,77.6521], popup = "Hello, I am god!",icon = folium.Icon(color='red'))) #to add children. This adds a marker

#creating a function for different colors for different elevations

def color_producer(elevation):
    if elevation < 1000 :
        return "green"
    elif 1000 < elevation < 3000 :
        return "orange"
    else :
        return "red"




#adding multiple markers
#for coordinates in [[12.97,77.64],[12.9431,77.6922]]:
    #fg.add_child(folium.Marker(location=coordinates, popup="Hello World!", icon=folium.Icon(color='red')))
#     fg.add_child(folium.Marker(location=[lt,ln], popup = str(el) +" m", icon=folium.Icon(color= color_producer(el)))) will produce marker
#     folium.CircleMarker(location=[lt,ln],  radius = 6, popup = str(el) +" m",fill_color= color_producer(el), color = 'grey', fill_opacity = 0.7, fill = True ) will produce circle


for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],  radius = 6, popup = str(el) +" m",fill_color= color_producer(el), color = 'grey', fill_opacity = 0.7, fill = True ))

#What is GeoJson?

#GeoJson enables different polygons for different countries

fgp = folium.FeatureGroup(name="Population")
file = "world.json"
fgp.add_child(folium.GeoJson(data = open(file, 'r', encoding = 'utf-8-sig').read(),
                                            style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' } ))  #adding GeoJson to the map. style_function changes the color of the polygon
#p opup = folium.popup(str(el),parse_html=True))

#the if x['properties']['POP2005'] is used to check for population density in a particular country and color code it accordingly



map.add_child(fgv)
map.add_child(fgp)

#adding layer control
map.add_child(folium.LayerControl()) #can toggle between layers
map.save("TestMap.html") #saving it to see output
