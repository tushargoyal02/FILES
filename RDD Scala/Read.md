# Apache Spark with Scala
*   Making eclipse project file to be open in Eclipse on terminal
    *   Move to the workspace

            sbt new scala/hello-world.g8

    *   After running above command type project name as hello-world

    *   We need to tell sbt that we would like to use the `sbteclipse` plugin.
    
    Type this in the project directory as is(hello-world)

            $ echo 'addSbtPlugin("com.typesafe.sbteclipse" % "sbteclipse-plugin" % "5.1.0")' > project/plugins.sbt

    
    *   This will add a file called "plugins.sbt" to the project directory which tells sbt that you want to use the sbteclipse plugin

* Finally run

        $ sbt > eclipse




# Setting up SBT [Support for Compiling Scala code]

## Install sbt on ubuntu

*  Steps:
    *  echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/
    sources.list.d/sbt.list
    *   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
    *   sudo apt-get update
    *   sudo apt-get install sbt



*   To create simple hello world build

        $ sbt new sbt/scala-seed.g8
    
    *   Provide name on the next go like `hello`

* Move inside dir `cd hello` and run `sbt`
        
        $ sbt
        > run

### Create a minimum sbt build 

        $ mkdir foo-build
        $ cd foo-build
        $ touch build.sbt

* Start   sbt shell and exit
    To compile the changes 

        >compile
* Type `help` for more command


## SEQUENCES
* Ordered collections of Data.
* Duplicates are permitted
* Array , list and vector


*  Creating an array

        Array(1,2,3,4)
*  creating a list
        
        List(1,2,4)

* List are the implementation like LINKED LIST.
  * Consist of a value and pointer to next element.

  * To remove or hide duplicate elements
    
        var.distinct


* VECTORS: Are linked list of 32 element arrays

* SET: Is bag of data. where no duplicates are permitted
  * Contains only unique values
  * Hashset, LinkedSet 

        Set(1,2,3,4)

* Option("Jamie")
  * To give any string 
* var.getOrElse("Jase")
  * This will not work as `Jamie ` is already been given (works only with NULL value)

        
* Tuple are the container can contain 22 elements
   
        (1,"a")
* Map consist of key -> value pair


## Higher Order Functions
        - var.map(lang => lang + "#")
        output = (SCALA#)
        
        - var.flatmap(lang => lang + "#")
        output = (s,c,a,l,a,#)

* Filter: In this filtering out those value which consist of `s` in it
        
        var.filter(lang => lang.contains("s"))

* foreach: This help to apply function but not return a value

        var.foreach(println)

* forall: check the conditions and return boolean values

        var.forall(lang => lang.contains("a"))

* reduce: Is a function used for transformation of data.

        scala> 1 to 5

        scala> var.reduce((acc,cur) => acc=cur)

        `or`

        scala> var.reduce(_+_)
* foldleft(): 

        var.foldLeft(0){case (acc,cur) => acc+ cur}

* product: This is like getting factorial or multiplication of all numbers

        var.product

* exists: This allow to check particular conditions as true or false

        var.exists(num => num==3)
* groupby: group the data into categories.

        var.groupBy(num => num%2)

        return value with remainder 1 group and with 0 group.


* takeWhile: take data to the conditions specified.

        var.takeWhile(num => num < 3)

* dropWhile: drop the value which doesnt satisfies the given condition.

#### For Conditions example

for{
        i <-  mynum if i%2==1
        j <-  1 to i 
} yield i*j 

NOTE - yield keyword return a result after completing of loop iterations.


### Exception Handling

*       import scala.util.{Try,Success,Failure}
