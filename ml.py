
2 REINFORCEMENT LEARNING - Software agents interact with an environment
	- learn how to optimize their behaviout 
	- APPLICATION 
		Economies
		Genetics
		Game playing
Classification - When target variable are consist of categories
  Eg -	Using labeled financial data to predict whether the value of a stock will go up or go down next week.

Regression - When target variable is continuous


3 KNN ALGORITHM -- In this all unlabeled point get trained by its  nearby labeled points

  Increasing number of k will make ypur model work smooth so making more high value of k is also a disadvantage
	
	from sklearn.neighbors import KNeighborsClassifier
	# setting its neighbour
	knn = KNeighborsClassifier(n_neighbors=6)
	# fitting the labeled data using and the data should not have any null values
	
	knn.fit(df['col1'], df['TARGET COLUMN'] )

	#predicting the unlabeled data is done with PREDICATE() method
	prediction = knn.predict(X_new)			#X_new is the unlabeled data


4 Train and split data
	from sklearn.model_selection import train_test_split
	
	# X will be the feature column and Y will be the target column
		#random_state=21 set seed 21 for split data, stratify=y indicate the same label over all 4 array
	
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2,  random_state=42, stratify=y)

	# Create a k-NN classifier with 7 neighbors: knn
	knn = KNeighborsClassifier(n_neighbors=7)

	# Fit the classifier to the training data
	knn.fit(X_train, y_train)

	# to check the accuracy of the model
	knn.score(X-test, y_test)	


	
