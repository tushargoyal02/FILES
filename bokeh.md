#   Bokeh

*   Glyph
    *   Properties of Visual shape [rectangle,circle] are called glyphs
    *   Properties like shape , size, color, transparency
    *   Any time of sequenctial values can be passed inside.

            # to save image and show in browser
            from bokeh.io import output_file, show

            from bokeh.plotting import figure

            plot = figure(plot_width=400, tools='pan,box_zoom')

            # defining x and y cordinate        
            plot.circle([1,2,3,4], [8,6,4,2])

            output_file('file.html')

            show(plot)

*   Patches: Are used to draw polygonal shape.
    *   used highly if waana draw geographic location.
    *   Data is given in list of list
    *   Each sublist contain x and y cordinate for one patch

            # this is used to plot line
            p=figure(x_axis_label='Date', y_axis_label='US Dollars')
            p.line(x-data, y-data)


            # for patch 
            p.patches(x_data, y_data)

*   Column dataSource

            from bokeh.models import ColumnDataSource

            source= ColumnDataSource(data={'x'=[1,2,3]})

            # if wanna take data as df
            from bokeh.sampledata.iris import flowers as df

            source=`ColumnDataSource(df)


*   HoverTool:

            from bokeh.models import HoverTool

            hover=HoverTool(tooltips=None, mode='hline')
            