import folium
import pandas


volcanoes = pandas.read_csv('Volcanoes.txt', sep=',')
volcanoes = volcanoes.astype({'LAT':'object', 'LON':'object'})
volcanoes['MAP'] = volcanoes['LAT'] + ', ' + volcanoes['LON']
print(volcanoes.dtypes)
map = folium.Map(tiles='Mapbox Bright')

map.save('Map1.html')
