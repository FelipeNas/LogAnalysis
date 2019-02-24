# Log Analysis

This project is part of the [UDACITY Full-Stack ND](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) about SQL database.  
The project is about asnwering 3 questions about the fictional news website database called **news**:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Inside the database **news** we have 3 tables: `articles`, `authors` and `log`:

### Articles
 Column |           Type
--------|--------------------------
 author | integer
 title  | text
 slug   | text                     
 lead   | text
 body   | text
 time   | timestamp with time zone
 id     | integer
### Authors
 Column |  Type
--------|---------
 name   | text
 bio    | text
 id     | integer
### Log
 Column |           Type
--------|--------------------------
 path   | text
 ip     | inet
 method | text
 status | text
 time   | timestamp with time zone
 id     | integer

The articles and authors share a common column that is `articles.author` and `authors.id`.  
The articles and log dosn't have a common column but the columns `articles.slug` and `log.path` have
a patter-matching.


## Prerequisites

[Git Bash](https://git-scm.com/downloads) for windows  
[Virtual Box 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)  
[Vagrant](https://www.vagrantup.com/downloads.html)  
[Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Install Git Bash for Windows.  
Install Virtual Box 5.1.  
Install Vagrant.  
Unzip the database file, and put the content inside the **vagrant** directory.

Change to the *VM config* directory via terminal, inside there is a directory called **vagrant**, change to this directory.  
Inside the directory **vagrant**, type: `vagrant up`.  
Wait until `vagrant up` is finish running.  
Now type: `vagrant ssh` to log in the VM.

Logged into the VM cd into the vagrant directory: `cd /vagrant/`  
Type: `psql	-d news -f newsdata.sql`.  
Now the database **news** is loaded.

## How to use

Logged into the VM  
Inside the directory /vagrant/,  
Use `python Log.Analysis.py`
