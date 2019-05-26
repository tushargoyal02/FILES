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

9 Covariance - is a measure of how two quantities vary together

	Pearson correlation coefficient is 	P = covariance
						   --------------
						 (std of x) (std of y)

NOTE
      [
	Look at the spread in the x-direction in the plots: The plot with the largest spread is the one that has the highest variance.
    	High covariance means that when x is high, y is also high, and when x is low, y is also low.
    	Negative covariance means that when x is high, y is low, and when x is low, y is high.
	]

10 Covariance is calculated by 
	np.cov(x,y)



11 Probablity is allow to give uncertanity
	 Probabilistic language is in fact very precise. It precisely describes uncertainty.


12 	simulating 4 coins
	np.random.seed(42)
	random_number = np.random.random(size=4)


13 Probility -- Bernaouli distribution to find probability for values either be true or False

	Discreate uniform PMF - example is throwing a dice and probability for a number is 1/6 everytime
		[PMF -- Probability Mass Function]
	
	PMF - defined as set of probabilits of discreate outcomes

	Binominal Distribution -- Number of r of success in n Burnouli trials with probability p of success is Binomially distributed
		np,random.binimial(4,0.5)		#4 is the number of trials and 0.5 is the probability



14 Poisson Process - timming of next event is completely independent of when previous event happened
	ex -  hits on a website

   Poisson distributed - number of r arrivals of Poisson process in a given time interval with average rate of lamla arrival per interval
	
	It is limit of Binominal Distribution for low probability of success and large number of trials

	 NOTE [When we have rare events (low p, high n), the Binomial distribution is Poisson. ]
		np.random.poisson(6 , size=1000)         #6 is average or mean of the event
		
PDF - Probability density function	[used for continuous variable ]
	- continuous analog to PMF[mass function]
	- Observing value of continuous variable

CDF - Cummalative distribution function
	- Gives probability of light wil be less than value on x-axis [example]
		to draw     x , y = ecdf(colName)
			    plt.plot(x,y)


	Area under the curve given probability

15 Normal Distribution [or GAUSSIAN distribution]- describes continuous variable whose PDF has a single symmetric peak

	Mean and Standard deviation are the parameter not the actual calculated values from the data

		take mean and std into two variables
	
		samples = np.random.normal(mean, std, size=10000)
		
		x, y = ecdf(colName)
		x_theo , y_theo = ecdf(samples)				# this is of the normal distribution


16 Exponential Distribution - waiting time between arrivals of Poisson process is this [single parameter]
	np.random.exponential(mean , size=1000)			#pass only the mean value

