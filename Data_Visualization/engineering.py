import bokeh.plotting
import bokeh.io
import pandas


df = pandas.read_csv('Data_Visualization/bachelors.csv')

x = df['Year']
y = df['Engineering']

bokeh.io.output_file('enginieering.html')

f = bokeh.plotting.figure(title="Female Engineering Bachelors USA")

f.xaxis.axis_label = 'Date'
f.yaxis.axis_label = 'Percentage'

f.line(x, y, color='#3484BB', legend='FEB USA')

bokeh.io.show(f)
