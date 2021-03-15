# Hands-on Flask-01 : Creating First Flask Application - Hello World and basic usage of Jinja Templates

Purpose of the this hands-on training is to give the students quick introductory knowledge of how to create a Flask web application on local.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- understand client-server software architecture.

- get familiar with Python Flask framework.

- install Python and Flask framework on local

- build a simple web application with Python Flask framework.

- use git repo to manage the application versioning.

- run the web application on AWS EC2 instance using the GitHub repo as codebase (will be shown by instructor).

## Outline

- Part 1 - Getting to know the Python Flask framework

- Part 2 - Write a Simple Hello World Web Application on GitHub Repo

- Part 3 - Run the Hello World App on local

- Part 4 - Write a Simple Hello World Web Application with Jinja template on GitHub Repo

## Part 1 - Getting to know the Python Flask framework

![Flask](./flask.png)

Flask is a web application development framework written in Python. It is a micro-framework that provides only the essential components which makes it easier to begin with when compared to full-stack frameworks like Django which has boilerplate code and dependencies.
And yet, Flask provides libraries, tools, and modules to develop web applications with additional features like authentication, database ORM, etc.

Followings are some of features of Flask Framework;

- It provides a development server and a debugger.

- It uses Jinja2 as templating engine.

- It is compliant with WSGI 1.0.

- It provides integrated support for unit testing.

- Many extensions are available to enhance its functionalities.


## Part 2 - Write a Simple Hello World Web Application on GitHub Repo

- Create folder named `flask-01-hello-world-app` within `clarusway-python-workshop` repo

- Create python file named `hello-world-app.py`

- Import Flask module.

- Create an object named `app` from imported Flask module.

- Create a function `hello` which returns a string `Hello World`.

- Assign a URL route the `hello` function with decorator `@app.route('/')`.

- run the application in debug mode

- Save the complete code as `hello-world-app.py` file under `hands-on/flask-01-hello-world-app` folder.

- Add and commit all changes on local repo

- Push `hello-world-app.py` to remote repo `clarusway-python-workshop` on GitHub.

- Run the web application in debug mode.


- Connect the Hello World application from the web browser


- Connect the Hello World application from the terminal with `curl` command.

## Part 4 - Write a Simple Hello World Web Application with Jinja template on GitHub Repo

- Create folder named `flask-02-Jinja_Template` within `clarusway-python-workshop` repo

- Create python file named `jinja.py`

- Import Flask module.

- Create an object named `app` from imported Flask module.

- Create an `index.html` file under templates folder.

- Create a function named `head` which sents number `number1` and `number2` variables to the `index.html`. Use these variables into the `index.html` file. Assign a URL route the `head` function with decorator `@app.route('/')`.

- Create an `body.html` file under templates folder.

- Create a function named `number` which sents number `num1` and `num2` and sum of them to the `index.html`. Use these variables into the `body.html` file. Assign a URL route the `number` function with decorator `@app.route('/sum')`.

- run the application in debug mode

- Save the complete code as `jinja.py` file under `hands-on/flask-02-Jinja_Template` folder.

- Add and commit all changes on local repo

- Push `jinja.py` to remote repo `clarusway-python-workshop` on GitHub.