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