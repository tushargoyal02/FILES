# 1. RDD SCALA
*   RDD is like immutable sequential or parallel scala collections
    * flatmap
    * map
    * filter
    * fold
    * aggregate

### 2. Creation of RDD
*   Transforming existing RDD   [Like map on RDD]
*   From SparkContext or SparkSession 

    *   [SparkContext can be thought as how you handle Spark Cluster. Represent connection between Spark Cluster & application]
        *   Parallelize - 
            *   Convert local scala collection to RDD
        *   textFile    - 
            *   Read data fron textfile like hadoop and return an string.



#### 3. Operations on RDD

*   Transformation:
*   Return an RDD as results
       
*   They are `lazy`as RDD is not computed immediately

*   Action
    *   Compute the result based on RDD
    *   They are `eager` , as their resilt is immediately computed


NOTE -- When a transformation is done nothing actually happens at cluster until any action is performed.


### 4. Comman Transformation:
*   map: apply function on rdd and return rdd
    *   map[B](f: a=>b): RDD[B]

*   flatmap: apply function to each element of rdd and return rdd of contents.
    *   flatmap[B](f: A=> TraversableOnce[B]): RDD[B]

* filter: Apply function to RDD and return RDD of Elements that passes function

    *   filter(pred: A=> Boolean): RDD[A]
* distinct: return rdd with duplicated removed
    *   distinct() : RDD[B]


### 5. Common Actions:
*   collect: return all element in RDD
*   count: return number of elements
*   take : return only specific data
*   reduce: combine the elements in RDD together using any function and return result.

    *       reduce(func: (A,A) => A)  : A     
          
*   foreach -  apply function to each element in RDD


### 6. Transformation on TWO RDD's
*   union: Return an RDD containing element from both RDD
*   intersection: return element found in both RDD
*   subtract:  return an RDD with the content of other RDD removes
*   cartesian: cartesian product with other RDD.


### 7. RDD Actions
*   takeSample: return an array with a random sample of num element of datasets
    
        takeSample(withRepl: Boolean, num:Int): Array[T]
*   takeOrdered - return the first n numbers of rdd

        takeOrdered(num: Int)(implicit ord: Ordering[T]) : Array[T]

*   saveAsTextFile: write elements of datasets as a text file

        saveAsTextFile(path: String ): Unit

*   saveAsSequenceFile:  write elements of datasets as Hadoop sequence file in the local filesysten
        saveAsSequenceFile(path: String): Unit

        
* RDD are computed every time an action is performed.

* Cache the data in memory to stop data.

        - persist() : make data save in cache memory      
        cmd -> data.filter(_.contains("ERROR")).persist()




* cache() : shorthand for using the default storage level which is memory only as java objects
* persist() : Pass the storage level you'd like as a parameter to persist.
