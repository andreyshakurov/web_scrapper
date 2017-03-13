# Web-scrapper

Web-scrapper is used to crawl [website]  and extract structured data from pages. The output is CSV file with profile data.

# Before installing
Make sure that the [website] is running in the background and sample user "Bob" with a password "Bob" is registrated. 

# Instalation 
First of all you have to install virtualenv via pip:
  ```sh
$ pip install virtualenv 
```
Create a virtual environment for a project:
  ```sh
$ mkdir scrapper_folder 
$ cd scrapper_folder
$ virtualenv venv
```
And then activate your virtual environment.
  ```sh
$ source venv/bin/activate
```
Copy web_scrapper_master folder into scrapper_folder and install the requirements:
  ```sh
$ cd  web_scrapper-master/
$ pip install -r requirements.txt
```
Now you can run your scrapper:
  ```sh
$ python spider.py
```
As a result there will be a CSV file with profile data of all registrated users.


[website]: <https://github.com/andreyshakurov/web_app>
