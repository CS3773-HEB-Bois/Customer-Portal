# CS3773 - Consumer Portal Project

## Setting up dev environment

1.  Install Docker for Windows / OSX / Linux

* Windows: https://docs.docker.com/docker-for-windows/install/
* OSX: https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac
* Linux: It's complicated. Look it up.

2.  You are all set! You are ready to start developing our project :)

## Development

### Starting the development server

The Docker containers that w setup include `jdk-8`, `play 2.6`, and `mysql 5.7`, so
you don't have to install anything else. Everything is ready to go.

To start the development environment/setup, first navigate to this directory in a command shell
(terminal in OSX, or cywgin/git-bash/WSL in Windows), and then execute the following command:

```
docker-compose up
```

After a long while of installation and setup, the server should be running on `http://localhost:9000`.
Navigate to that address on your favorite web browser and you should be greeted with the `Hello World`
page of `Play 2.6`.

### Deploying changes to the server.

Don't even trip, dawg! The server automatically syncs with the code you have in your machine!
Whatever changes you make to the source of this project will be automatically reflected in the
dev environment.

To see the code changes, reload the page in your web browser and you should be able to test your
new code!

Since the `Play` framework auto-compiles the sources after it detects a change in the source files,
we don't have to worry about all that tedious work ;)

### Stopping the development server

To stop the server, you can execute `ctrl-c` in the command shell that runs the development server.
That should take care of shutting down all processes.

### Database

No worries! The database has been configured already. Our initial project was configured
to use `mysql` and `jdbc` to handle connections within `Play`.

### That's it! We are ready to start working on the project.

Navigate to the [Play docs](https://www.playframework.com/documentation/2.6.x/Home) and start
learning about backend development using Java!

## F.A.Q

#### What IDE can I use for development?

* You can pretty much use whatever you want! Navigate to the [IDE page](https://www.playframework.com/documentation/2.6.x/IDE) in `Play` docs to find out how to setup your IDE.

#### How do I get rid of the Docker containers (free up space after we are done with the project)

* To remove the Docker containers, you can use `docker-compose down --rmi all`.
  Note that if you execute this command, you will need to execute `docker-compose up` again to rebuild
  the container and start the development server

#### Why do we have two Nicks, and a Wolverine in the project?

* IDK. I sat with the wrong people in my first semester at UTSA.

#### What language are the views (`app/views.index.scala.html`) using?

* Well, based on the name...they use Scala. It's not too bad. Here is the [documentation](https://www.playframework.com/documentation/2.6.x/JavaTemplates).
