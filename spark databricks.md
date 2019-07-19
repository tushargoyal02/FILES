#   DataBricks
*   Workspace is an environment for accessing all of your Databricks assets. A Workspace organizes notebooks, libraries, dashboards, and experiments into folders and provides access to data objects and computational resources.


*   Notebook:
    *   A notebook is a web-based interface to a document that contains runnable code, visualizations, and narrative text. Notebooks are one interface for interacting with Databricks.


    *   REPL - Read Evaluate print loop interactive toplevel environment.

    *   A cluster has a maximum number of execution contexts (145). Once the number of execution contexts has reached this threshold, you cannot attach a notebook to the cluster or create a new execution context.

    
            spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion")
 


*   Commands in Notebook : :
    *   %sh : Allows you to execute shell code in your notebook
    *   %fs : Allows you to use dbutils filesystem commands.
    *   %md :     Allows you to include various types of documentation, including text, images, and mathematical formulas and equations.




*   Creating a global Table
    
        dataFrame.write.saveAsTable("<table-name>")

    *   Create local table

            dataFrame.createOrReplaceTempView("<table-name>")

*   Sql with Python
    
        diamonds = spark.sql("select * from diamonds")display(diamonds.select("*"))


*   Creating partition table

        dataframe.write.mode(SaveMode.Overwrite).partitionBy("id").saveAsTable("<example-table>")
    


#   SPARK
*   wide range data processing engine.

*   RDD : is a distributed collection of elements across cluster nodes. Also performs parallel operations. Moreover, Spark RDDs are immutable in nature.

