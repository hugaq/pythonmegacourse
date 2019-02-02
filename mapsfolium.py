import folium
import pandas


volcanoes = pandas.read_csv('Volcanoes.txt', sep=',')
volcanoes = volcanoes.astype({'LAT':'str', 'LON':'str'})
volcanoes['MAP'] = volcanoes['LAT'] + ', ' + volcanoes['LON']
print(volcanoes)
map = folium.Map(tiles='Mapbox Bright')
def func(location):
    inp = location.split(',')
    map.add_child(folium.Marker(location=[int(inp[0]), int(inp[1])]))
volcanoes['MAP'].apply(func)
map.save('Map1.html')
