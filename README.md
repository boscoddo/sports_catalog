# Project 2: Item Catalog
## Description
I have developed a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users has the ability to post, edit, and delete their items.
The homepage displays all current categories with the latest added items.
Selecting a specific category shows you all the items available for that category.
Selecting a specific item shows you specific information about that item.
After logging in, a user has the ability to add, update, or delete item information. Users should be able to modify only those items that they themselves have created.

## How to run
* 1. To excute this code you'll need to setup a Linux virtual machine.  Installing Virtual Box and Vagrant is recommended.
* 2. You will need to bring the virtual machine online with vagrant up, Then log into it with vagrant ssh.
* 3. Within the Linux virtual machine, please install Python, PostgreSQL. Launch the Vagrant VM (by typing vagrant up in the directory fullstack/vagrant from the terminal). 
* 4. Copy All Project files to /vagrant/catalog folder. 
* 5. Setup the database by running, python database_setup.py  Then populate the database by runing, python database_data.py
* 6. Run the application within the VM by typing python /vagrant/catalog/application.py into the Terminal.
* 7. Opening Chrome Browser with Localhost:8000 to view the app

## Link to VM
You can find the link to the fullstack-nanodegree-vm [here.](http://github.com/udacity/fullstack-nanodegree-vm)

## Design
The app uses Flask and includes Google and Facebook authentication/authorization to allow users to login before making changes. PostgreSQL was used implement a databaseto store and organize item information. HTML was used to create the structure of the pages and Bootstrap CSS to the style the pages.

## PEP8 Errors
application.py:68:80: E501 line too long (141 > 79 characters)
This is due to Facebook URL too long. Not recommended to be broken up
application.py:77:80: E501 line too long (91 > 79 characters)
This is due to Facebook URL too long. Not recommended to be broken up
application.py:92:80: E501 line too long (110 > 79 characters)
This is due to Facebook URL too long. Not recommended to be broken up
application.py:270:5: E722 do not use bare 'except'
This line is the same as the example from Udacity oauth project.
