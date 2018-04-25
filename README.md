# Personal Blog Application

## Adebayo Olamijin Isaac

## Description

This blog application enables a writer to make posts while other users can also sign in to view the blog posts and also make comments.

It allows users to:
* view the blog posts entered by the writer
* Comment on blog posts submitted by the writer.
* View the most recent posts.
* It allows a writer to submit posts by accessing the writers page on the navbar only if the have access to  the username and password.


The application allows the writer to:
* sign in to the blog.
* submit several blog posts
* Delete comments when necessary.
* perform CRUD operations through the gui.

### Prerequisites

The following are needed for the application to run on a local computer:
* python version 3.6
* Flask framework
* Bootstrap v.3
* text editor (atom, VS code or sublime text)
* Web browser
* Admin Login credentials. This allows the admin(writer) to post a blog, delete and edit blogs posted and/orcomments posted by users.

## Getting Started
* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* In the cloned project, inside the root directory, create a directory and name it virtual.
* From the terminal,create a virtual environment and name it venv
* Switch to the virtual environment by entering  ```source venv/bin/activate``` from the terminal.
* Run ```pip install -r requirements.txt``` to install all the extension required.
* To run the application using the flask cli,```export FLASK_APP=blog.py``` ,then type ```flask run``` to run the application
* Once inside the application, a user will only be able to view the blogs posted and comment on them.
* To access the writer page in the application you will be required to enter a username which is set to "olamijin" and a password which i have also set as "1234abcdola"

## License

MIT License

Copyright (c) 2018 Adebayo Olamijin
