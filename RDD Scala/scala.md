# How to create a project in scala

### Website : scala-lang.org

*   www.github.com/databricks/scala-style-guide

*   Make a directory at any place
    *   Make a `build.sbt` file inside the folder

            scalaVersion := "2.11.7"
            name := "name of project"
            libraryDependencies += "org.apache.spark" % "spark-mllib_2.11" % "1.5.1"

            1 is group id who created the project
            2 is name of the project to pull and scala version
            3 is the version of the project itself

            cmd: type `activator` to import project.
    
    * Type after the activator the `compile` command to compile all the project file

            > compile
    * Type `run` to run any classs present.

            > run

    * To move your project to IDE
        
            - Press CTRL+D
            - cd project
            - vim plugins.sbt 
        

        *   See pluginsSBT file

            *   Go back to `cd ..`

                    Type-  activator
                           > eclipse

* Let say apply a map function
    *   Create number `[1 to 100 ]`
        
            var.map(number => number+1)
    *   Group By operation

            var.groupBy(number => number %3 )

### To make  SparkContext object

*   Type this

        val conf = new SparkConf().setAppName("projectName").setMaster("local[*]")

        val sc = new SparkContext(conf)

* To make SQL Context

        val sqlContext =  new SQLContext(sc)

* To create dataframe

        val df = sqlContext.createDataFrame(Seq(
            (0, Array("hi","I","Bye")),
            (1, Array("bye", "world"))
        )).toDF("label","words")


* To get data

        df.take(3).map(line => line.getAs[Stream[String]]("ngrams").toList).foreach(println)

    *   We are taking 3 data converting it by explicitly giving to String and providing it to list and printing for each line.


## Syntax in scala

*   Define a class and by default a constructor is called at making class.
        
        class hello
    Creating an instance of a class

        new hello()
        res0 variable got defined by default

    Calling a method on instance
        
        res0.toString

*   Field: Is a value encapsulated within instance of a class. It is accessible to outside world, unless specified otherwise

*   Field vs Parameter:

    *   Parameter are passed to class  and are only visible inside the class.
    *   Field exist in body of class and accessible to outsiders.

*   Immutable field are those whose value can't be changed.
    * They are threadsafe & is done by default.
        
    
            val message: String = "hey"

    Mutuable are those whose value can be changed
            
        var messgae: String = "hey"

*   Method : Describes the behaviiour within a class. Specify their return type.

        def echo(message: String):
            String  = message

*   Field's VS Method
    *   Method is evaluated every time they are called.
    *   Field are evaluated at time class is constructed.


*   Overloading:    Allow to have multiple defination of same method but taking different arguments.
