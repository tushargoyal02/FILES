#       Unsupervised Learning 
*   Basically it mean finding some sought of similar pattern in the dataset. Without having label column


##      K-Mean Clustering
*   Finding clusters of samples
*   Specify number of cluster

        from sklearn.cluster import KMeans
        model = KMeans(n_clusters=3)

* Lower the value of interia better is the model.
* Cross tab: Down below make a cross table between two column for maintaing the accuracy.

        pd.crosstab(df['labels], df['species'])

* In Kmean feature variance=feature influence,

* STANDARDSCALER: Transforms each feature  to have mean 0 and variacnce 1

      - from sklearn.preprocessing import StandardScaler
      - scaler = StandardScaler()
      - scaler.fit(samples)

### Difference between Kmean and STANDARDSCALER

* STANDARDSCALER use fit / transform   method.
* KMean uses fit and predict with KMean

* Make the STANDARDSCALER and KMean together.

        from sklearn.pipeline import  make_pipeline
        pipe = make_pipeline(scalerObj, KmeanObj)


### Hierarchical clustering with Scipy
* Use to show data visualization with the help of dendogram
* linkage() function to obtain a hierarchical clustering of the grain samples, and use dendrogram() to visualize the result. 

      - from scipy.cluster.hierachy import linkage, dendogram
      - merging = linkage(samples, method='complete')
      - dendogram( merging
       labels=country_name,
       leaf_rotation=90,
       leaf_font_size=6 )

* In dendogram : height on dendogram represnt distance between merging clusters.

