1 ModeGl is train for X_train and Y_train
  Predict is done on X_test as how much it is accurate as y_test
  Score is check between X_test and y_test
  Mean square error is done between y_test and y_pred




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

5 Linear regression
	from sklearn.linear_model import LinearRegression
	reg_all = linear_model.LinearRegression()
	

6 K-N fold cross validation -  In this we divide our data first in part and hold 1 fold for test and 9 for train and same goes on.

	from sklearn.model_selection import cross_val_score
	reg = linear_model.LinearRegression()
	
	cv_results = cross_val_score(reg, X, y, cv=5)				#providing regression data and number of fold



7 Regularization: Lineaer regression uses loss function & uses coefficient for each coefficient for each feature
	Large objects lead to overfitting by penalizing the large coefficient (regularization)


  1st type of regualarization is ridge regression:
	SEE IMAGES
	from sklearn.linear_model import Ridge 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

	# normalize mean all variable are in same state	
	ridge = Ridge(alpha=0.1 , normalize=True)
	ridge .fit(X_train, y_train)

	ridge_pred = ridge.perdict(X_test)

  2nd type is LASSO function 
	loss function 	= OLS loss function  + alpha * sum |absolute values|		#see IMAGES
	
	Can be used to select important feature of dataset
	Shrinks the coefficient of less importance to zero

# Classification reports and confusion matrices are great methods to quantitatively evaluate model performance,


8 LOGISTIC REGRESSION FOR BINARY CLASSIFICATION
	probabilty is greater than 0.5 [data labeled as 1]
	probabilty is less than 0.5 [data labeled as 0.5]
	
ROC CURVE - [Receiver opearting curve] - is got by chnaging the threshold value[p]
	
	# ROC curves provide a way to visually evaluate models.
	from sklearn.metrics import roc_curve

	#.predict_proba() method which returns the probability of a given sample being in a particular class. 
	y_pred = logreg.predict_prob( X_test )[:,1]




MORE area under the curve(AUC) of ruc curve more good is the model

	from sklearn.metrics import roc_auc_score
	pass predicted probabilty to roc_auc_curve

	#fpr is false positive right , true 
	fpr, tpr, threshold = roc_curve( y_test,  y_pred) 		#roc_curve is function



9 Hyperparamter tuning
	-- Are the parameter which are not trained while fitting the data [Done by cross validation]
	
  -> GRID SEARCH CROSS_VALIDATION -  
	
	from sklearn.model_selection import GridSearchCV
	param_grid = {'parameter Name here' : np.arrange(1,50)}			#range of choosing value as neighbours in np.arrange()
	knn = KNeighborsClassifier()

	knn_cv = GridSearchCV (knn, param_grid,cv=5) 	

	knn_cv.fit()

	# best_params_ to check the best parameter out there
	knn_cv.best_params_

	#best_score_ to check the best score out of all
	knn_cv.best_score_



 -> RandomizedSearchCV -
		In which not all hyperparameter values are tried out. Instead, a fixed number of hyperparameter settings is sampled from 				specified probability distributions
	Works same as grid search but grid search is computationally expensive	



10 PreProcess data converting categorical data into values
	- scikit learn [OneHotEncoder()]
	- pandas [get_dummies()]

	import pandas , read files
	df_origin = pd.get_dummies(df)



11 Replace not null value like 0 with nan values in data set

	df.col.replace(0, np.nan, inplace=True)					# to get nan value in place of 0 to show in df.info()[null value]

   Filling up nan values as like getting mean of nan or something else
	
	from sklearn.preprocessing import Imputer
	imp=Imputer(missing_values='NaN', strategy='mean', axis=0)
	#fitting the data
	imp.fit(X)  

	# transforming the data
	X = imp.transform(X)



12 PIPELINING IN SCIKIT LEARN
	from sklearn.pipeline import Pipeline	
	from sklearn.preprocessing import Imputer
	imp=Imputer(missing_values='NaN', strategy='mean', axis=0)
	logreg=LogisticRegression()
	
	# providing all steps as in tuple for doing work
	steps = [('imputation', imp), ('logistic_regression', logreg)]
	
	pipeline= Pipeline(steps)
	
	divide data, fit with pipeline and predict with pipeline.predict
