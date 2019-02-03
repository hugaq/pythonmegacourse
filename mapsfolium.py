import folium
import pandas


def height_indicator(height):
    if height < 1000:
        return 'green'
    elif height < 3000:
        return 'orange'
    else:
        return 'red'

def population_indicator(pop):
    if pop < 1000000:
        return {'fill_color':'green'}
    elif pop < 100000000:
        return {'fill_color':'orange'}
    else:
        return {'fill_color':'red'}

volcanoes = pandas.read_csv('Volcanoes.txt', sep=',')
volcanoes = volcanoes.astype({'ELEV': 'int'})
lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
elev = list(volcanoes['ELEV'])

map = folium.Map(tiles='Mapbox Bright')

fgv = folium.FeatureGroup(name='Vulcanoes')
for i, k, e in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[i, k], popup=str(e)+'m', radius=6, fill_color=height_indicator(e)))
map.add_child(fgv)

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda p: {'fill_color':'green' if p['properties']['POP2005'] < 1000000 else 'orange' if p['properties']['POP2005'] < 100000000 else 'red'}))

map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')
