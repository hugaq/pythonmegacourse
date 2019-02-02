import folium
import pandas


volcanoes = pandas.read_csv('Volcanoes.txt', sep=',')
volcanoes = volcanoes.astype({'LAT':'str', 'LON':'str'})
volcanoes['MAP'] = volcanoes['LAT'] + ', ' + volcanoes['LON']
print(volcanoes)
map = folium.Map(tiles='Mapbox Bright')
volcanoes['MAP'].apply(map.add_child(folium.Marker))
map.save('Map1.html')
