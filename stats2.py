
1 Residuals - It is the vertical distance from the vertical line
  Intercept is the point where vertical line crosses the y-axis

  Least squares - Process of finding the parameters for which sum of squares of residuals is minimal
prog-	slope, intercept = np.polyfit(x_data, y_data, 1)	#perform least square with the polynominal function and 1 is degreee of polynominal

2 To do bootstrapping - rearranging the array values for summary statistics
prog-	np.random.choice([1,2,3,4,5], size=5)				#output [5,1,3,2,4]

  Bootstrap replicate -- A single value of a statistic computed from a bootstrap sample.
	

To get specific confidence interval	
	To get the 2.5th and 97.5th percentiles of x, the statement would be 
	
prg->	np.percentile(x, [2.5, 97.5]). This gives the 95% confidence interval of x. Do the same for bs_replicates.

	To any function to pass (data , function , size of data)

	Data should be in 2D array and the function is like np.mean or np.median and size is the 


3 Permutation -- Is the scrambling the arrangement of data in any order
	make two data concatinate each other

prog		data3 = np.concatenate	(data1 , data2)
		permuted = np.random.permutation(data3)
		
		data1_NEW =  permuted[:len(data1)]		#assigning the same amount of data1 to data1_new



4 Hypotheis testing is also called Null Hypothesis significance testing [NHST]

	p - values = the probability of observing a test statistic equally or more extreme than the one you observed, given that the null hypothesis                       is true.



5 To check correlation between two entites
	- Use null hypothesis - two variables are completely correlated
	- Simulate data assuming that null hypothesis is true 
	- Use pearson coffeicient as a test statistic
	- complete p-value

