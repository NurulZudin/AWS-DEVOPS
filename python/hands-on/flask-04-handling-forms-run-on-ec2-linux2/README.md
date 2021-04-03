# Hands-on Flask-04: Using Get-Post Methods

Purpose of the this hands-on training is to give the students introductory knowledge of how to handle forms.

![HTTP Methods in Flask](./http-methods-flask.png)

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- install Python and Flask framework on Amazon Linux 2 EC2 instance.

- build a web application with Python Flask framework.

- handle forms using the flask-wtf module.

- use git repo to manage the application versioning.

- run the web application on AWS EC2 instance using the GitHub repo as codebase.


## Outline

- Part 1 - Getting to know HTTP methods (GET & POST).

- Part 2 - Write a Sample Web Application with forms and push to GitHub Repo

- Part 3 - Run the Sample Web Application on EC2 Instance


## Part 1 - Getting to know HTTP methods (GET & POST)


HTTP (Hypertext Transfer Protocol) is a request-response protocol. A client on one side (web browser) asks or requests something from a server and the server on the other side sends a response to that client. 

When sending request, the client can send data with using different http methods like `GET, POST, PUT, HEAD, DELETE, PATCH, OPTIONS`, but the most common ones are `GET` and `POST`.

![Get and Post Requests](./get-post-request.jpg)

- HTTP `GET` method request;
    
    - used to request data from a specified resource.

    - can be cached.

    - remains in the browser history.

    - can be bookmarked

    - should never be used when dealing with sensitive data.

    - has length limitation.

    - only used to request data, not to modify it. 

    ![url-structure of GET method](./url-structure.png) 

- HTTP `POST` method request;
    
    - never cached.

    - does not remain in the browser history.

    - can not be bookmarked

    - can be used when dealing with sensitive data.

    - has no length limitation.

## Part 2 - Write a Sample Web Application with forms and push to GitHub Repo

- Create folder named `flask-04-handling-forms-run-on-ec2-linux2` within `clarusway-python-workshop` repo

- Write an application with form handling and save the complete code as `app-form-handling.py` under `hands-on/flask-04-handling-forms-run-on-ec2-linux2` folder.

```python
# Import Flask modules


# Create an object named app


# Create a function named `home` which uses template file named `index.html` given under `templates` folder, send your name as template variable, and assign it root path ('/')


# Write a function named `greet` which uses template file named `greet.html` given under `templates` folder. it takes parameters from query string on URL. If it doesn't have any parameter, warning massage is raised



# Write a function named `login` which uses `GET` and `POST` methods,
# and template files named `login.html` and `secure.html` given under `templates` folder
# and assign to the static route of ('login'). It controls If password is clarusway or not


# Add a statement to run the Flask application which can be reached from any host on port 80.

# app.run(host='0.0.0.0', port=80)
```

## Part 3 - Install Python and Flask framework on Amazon Linux 2 EC2 Instance 

- Launch an Amazon EC2 instance using the Amazon Linux 2 AMI with security group allowing SSH (Port 22) and HTTP (Port 80) connections.

- Connect to your instance with SSH.

- Update the installed packages and package cache on your instance.

- Install `Python 3` packages.

- Check the python3 version

- Install `Python 3 Flask` framework.

- Check the versions of Flask framework packages

- Pull the files from github repo

- Run the Flask application

