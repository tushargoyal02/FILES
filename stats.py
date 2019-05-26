EDA - Exploratory Data Analysis


1 Swarm or BEE Swarm plot
	sns.swarmplot(x='colname', y='colname', data=df)
	set x and y label and show both


2 ECDF Empirical cumulative distribution functions

	x axis have value which we are calculating
	y axis have fraction of value smaller than x value
	
	import numpy as np
	x = np.sort(column)
	y = np.arange(1, len(x)+1 / len(x) )
	plt.plot(x,y , marker='.', linestyle='none') 	#none to plot value not 
	plt.margins(0.02)  	#keeps data off plot edges(gives 0.02 buffee)

3 Mean is the average statistics of data
	import numpy as np
	np.mean(col_name)

	[Mean is higly affected by outliers as it increases or decreases the mean value for the actual mean value ]

4 Median is the middle value of data set
	np.median(colname)

5 Percentile are used for summary statistics
	like at what 25 percentage how people voted

	np.percentile(df['colNamw'], [25,50,75])	#the amount of percentile like 25,50,75 percent


6 IQR - is inter quantile range which is height of the summary statist like 25,50,75

7 Boxplot has good when we need to look for the percentile and drawing is same as swarmplot
	
	sns.boxplot(x='colname', y='colname', data=df)


8 Variance is the average squared distance of the data from their mean

	np.var(colname)					#it doesnt have the same quantites as we have measured

So for that we calculate square root of variance which is STANDARD DEVIATION [SD]

	np.std(colname)	#same as 
		 np.sqrt(np.var(colname))

