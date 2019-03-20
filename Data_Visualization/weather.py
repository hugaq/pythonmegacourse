import bokeh.plotting
import bokeh.io
import pandas


df = pandas.read_excel('Data_Visualization/verlegenhuken.xlsx')

x = df['Temperature']/10.0
y = df['Pressure']/10.0

bokeh.io.output_file('weather.html')

f = bokeh.plotting.figure(title="Temperature and Air Pressure")

f.xaxis.axis_label = 'Temperature (°C)'
f.yaxis.axis_label = 'Pressure (hPa)'

f.circle(x, y, color='#3484BB', size=0.5)

bokeh.io.show(f)
