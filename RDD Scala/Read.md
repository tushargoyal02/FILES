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

* Steps:
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

*   Start   sbt shell and exit
    To compile the changes 

        >compile
* Type `help` for more commandsh