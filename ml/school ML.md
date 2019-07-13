*   Higher log loss   = High confidence[p value] and target value is wrong[target=0]

*   Compute the log loss value:
    *   log loss metric handles the trade-off between accuracy and confidence

            compute_log_loss(predicted_values, actual_values)

#   key steps for any challenge related to machine learning
*   Start with basic model.
*   Try to train model with the numeric data only
*   Multi-class logistic regression
    *   Train classifier on each label seprately and use to predict whether their is any label for particular row.

*   Compute log loss score

#   ---------
*   If you have multiple target variables use

        multilabel_train_test_split()

*   Importing OneVsRestClassifier

        from sklearn.multiclass import OneVsRestClassifier

        OneVsRestClassifier(LogisticRegression())

    *   OneVsRestClassifier
        *   Treats each column of y independently
        *   Fits a classifier for each of the columns
    

*   To get only the numeric column in dataframe

        df[NUMERIC_COLUMNS]


*   To make the prediction column in csv file 

        predict_df = pd.DataFrame(columns-pd.get_dummies(df[LABELS], prefix_sep='__').columns,
        index=df.index, data=predictions)


    *   data above contains value of array in `predictions`, as it is the value of arrays


*   Predict_prob method: Is to predict probability of each model

        clf.fit(X_train, y_train)
        clf.predict_prob(df)


*   To check the score submission for the submission file 

        score = score_submission(pred_path='filename')


# NLP
*   Tokenization: It mean splitting the string into segments.

*   Scikit-learn tools for bag-of-words

    *   CountVectorizer() : Do 3 things
        *   Tokeinzes all the string
        *   Build a vocubulary
        *   Count the occurances of each token in vocabulary
*   
    
    -   from sklearn.feature_extraction.text import CountVectorizer
    -   TOKEN_BASIC = '\\S+(?=\\s+)'  [regular expression]
    -   df.column.fillna('', inplace=True)

    -   obj = CountVectorizer(token_pattern=TOKEN_BASIC)

* To take n gram in CountVectorizer type inside as:

      CountVectorizer(token_pattern=TOKEN_BASIC, ngram_range=(1,2))

#   Function Transformer:

* Pipeline cant take Imputer as well as CountVectorizer problem at same time.

* Use Function Transformer:
   * Turn an python function to object with understanding of pipeline
   * Need to write two functions:
        * Take entire df and retun numeric columns
        * Take df and return text data.
   * Create two different lambda functions one for text and other for numeric value

   * Can then preprocess numeric and text data in seprate pipelines.

         from sklearn.preprocessing import FunctionTransformer

         from sklearn.pipeline import FeatureUnion

* Make object for text and numerical data in df.
 
      obj1 = FunctionTransformer(lambda X: X['text], validate=False)

## Feature Union
* Feature Union of sklearn combines the two array of text features with numeric features into 1 array
* This 1 array is now passed to classifier
          
      union = FeatureUnion([('numeric, obj2),('text',obj1)])

* Make two pipeline seprate for text and 1 for numeric data. Then combine both in the last pipeline




## Statistical Tool used

* sklearn provide way to add interaction terms

        - from sklearn.preprocessing import Poly  nomialFeatures
        - interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

        - interaction.fit_transform(x)

* Interaction_only : Above tell we dont need to multiply the column by itself

        - SparseInteractions(degree=2).fit_transform(x).toarray()


## Hashing Vectorizer

* Adding new feature lead to increase in array size.
* Hashing is way of increasing memory efficiency

 
      - from sklearn.feature_extraction.text import HashingVectorizer
      - vec= HashingVectorizer(norm=None, non_negative=True, token_pattern=Token, ngram_range=(1,2))
