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

    *   If we waana map all different species with different color

                from bokeh.models import CategoricalColorMapper

                mapper= CategoricalColorMapper( factors=['sentosa','virginica','versicolor'],
                palette=['red','blue','green'])

                # give
                p.circle(color={'field':'species', 
                'transformer': mapper})


### Row of plots
*   Plot 3 graph on horizontal row

        from bokeh.layouts import row
        
        #same works with column 
        layout = row(p1,p2,p3)

        #row and column can be nested too
        layout = row(column(p1,p2),p3)

* Also support Gridplot

      from bokeh.layouts import gridplot

      layout=gridplot([[None, p1],
      [p2,p3],
      toolbar_location=None])

   * list of list give list of rows for layout.



* To create tabs and panel like windows tabs for graph

      from bokeh.models.widgets import Tabs, Panel

      first = Panel(child=row(p1,p2), title='first')

      second = Panel(child=row(p3), title='second')

      tabs = Tabs(tabs=[first, second])




* For adding legend to graph
    
      # provide this addition argument
      plot.circle(legend='colName')

        # location of legend
      plot.legend.location= 'top_left'


* To show all the information of each point

      hover = HoverTools(tooltips=[
              ('speciesName', '@colname')

      ])

      plot= figure(tools=[hover, 'pan' , 
      'wheel_zoom'])



### App outline for Bokeh Server
* Bokeh server is to synchronize python objects with web applications in a browser

        # curdoc here is current document
        from bokeh.io  import curdoc

        #create plot and widgets


        #add callbacks [trigger at any event]



        # arrange plot and widget in layout

        curdoc().add_root(layout)


* To run bokeh file as server

        bokeh serve --show myapp.py


#### Uploading an drop down menu

* Same as import curdoc, column , figure and ColumnDataSource, Select from bokeh.models

        from bokeh.models import ColumnDataSource, Select

        menu = Select(options=['uniform', 'normal', 'lognormal',
        value='uniform', title='Distribution'])


  * And in the callback value we select the menu.value to get the actual value being putted by the user or is been selected from the menu.


* Button: Whenver a button is click an event is occur.

        from bokeh.models import Button

        button = Button(label='press me')

        # button callback
        def update():

                button.on_click(update)