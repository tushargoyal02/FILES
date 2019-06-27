#   SuperVised ML
*   Model is train for X_train and Y_train
*   Predict is done on X_test as how much it is accurate as y_test

*  Score is check between X_test and y_test
  Mean square error is done between y_test and y_pred

*   REINFORCEMENT LEARNING - Software agents interact with an environment.
	- Learn how to optimize their behaviour 
	- APPLICATION 
	    *   Economies
		*   Genetics
		*   Game playing
*   Classification - When target variable are consist of categories
    *   Eg -Using labeled financial data to predict whether the value of a stock will go up or go down next week.

*   Regression - When target variable is continuous

#### KNN ALGORITHM -- In this all unlabeled point get trained by its nearby labeled points.

*   Increasing number of k will make ypur model work smooth so making more high value of k is also a disadvantage.

        from sklearn.neighbors import KNeighborsClassifier

    *   setting its neighbour

            knn = KNeighborsClassifier(n_neighbors=6)

	*   fitting the labeled data using and the data should not have any null values

            knn.fit(df['col1'], df['TARGET COLUMN'] )
    *   predicting the unlabeled data is done with PREDICATE() method

            prediction = knn.predict(X_new)





## Fill null values like [0,?,Nan ]

    from sklearn.preprocessing import Imputer
    imp = Imputer(missing_values='Nan', strategy='mean', axis=0)             [providing all desired info]
    imp.fit(X)          [fitting the data]
    X = imp.transform(X)

## Pipeline work [multiple task at once]
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import Imputer
    imp = Imputer(missing_values='Nan', strategy='mean', axis=0)             

*   Now importing all model & all steps in tuple

        logreg = LogisticRegression()
        steps=[('imputation, imp), (logistic_regression, logreg)]

        # passing this data to pipeline
        pipeline = Pipeline(steps)

        # divide data as same & fit,predict using pipeline
        pipeline.fit(data_x, data_y)

## Scaling and 
*   Need is one all value varies very large hence model will not work properly
### Standardization : Subtract the mean and divide by variance  
* All features get centered around zero and have  variance one.
    
        from sklearn.preprocessing import scale
        X_scaled = scale(X)

    *   Can also be used with pipelining
            
            from sklearn.preprocessing import   StandardScaler
            steps = [('scaler', StandardScalar()), ('knn', KNeighbour]
        

        

