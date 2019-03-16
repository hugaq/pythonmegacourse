from bokeh.plotting import figure
from bokeh.io import output_file, show
#basic bokeh line graph

x = [1,2,3,4,5]
y = [1,2,2,4,7]

output_file("Line.html")

#create figure object
f = figure()

#create line plot
f.line(x, y)

show(f)



x = [3,7.5,10]
y = [3,6,9]


for i in ['triangle', 'circle']:
    exec(''.join(['output_file("', i, '.html")']))
    f = figure()
    exec(''.join(['f.', i, '(x, y)']))
    show(f)