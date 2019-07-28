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


* Fcluster method is used to extract the cluster label and return an numpy array.

        - from scipy.cluster.hierarchy import fcluster
        - label = fcluster(mergin, 15, criterion='distance')

### T-sne for 2-D maps
* It preserve nearness of samples
* it has only fit_transform method.
* All feature are different every time 

        from sklearn.manifold import TSME
        model = TSME(learning_rate=100)

* Code to label each point with its company name has been written for you using plt.annotate()


* PCA told how to shift data nearby to mean 0 and doesnt effect the value of the data.

   * PCA discards low variance PCA feature
    
         from sklearn.decomposition import PCA
        model = PCA()

  * Principal Component: Is direction of variance along which data varies
     * Available as components_ attribute of PCA Object.

* Intrinsic dimension = number of feature needed to approximate the dataset.
    * It is also number of PCA features with significant variance.

* NOTE: Scatter plot work only if 2 or 3 features
        So PCA identifies intrinsic dimension when sample have any number of features.


### Non-negative matrix factorization

* Dimension reduction technique
* Easy to implement.
* Only applicable where sample features must be non-negative(>=0)

        from sklearn.decomposition import NMF
        model = NMF(n_components=2)
        