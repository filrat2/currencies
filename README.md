# Currency Converter

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#downloading-the-source-code-and-setup)
* [Planned changes](#planned-changes)
* [About me](#about-me)

## General info
This project is the final project of Python Developer bootcamp at [Future Collars](https://futurecollars.com/).

The project allows you to download exchange rate data from the [NBP Web API](http://api.nbp.pl/en.html) and perform several operations on the downloaded data:
- currency conversion
- comparing exchange rates
- generation of time series charts
- preview [Middle exchange rates of foreign currencies - table A](https://www.nbp.pl/homen.aspx?f=/kursy/ratesa.html) from  [National Bank of Poland](https://www.nbp.pl/)  (Narodowy Bank Polski)
	
## Technologies
<h3 align="left">Languages and Tools:</h3>
<p align="left"><a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/></a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/></a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/></a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/></a></p>

Project is created with:
* [Python](https://www.python.org/) version: 3.9.x
* [Flask](https://flask.palletsprojects.com/en/2.2.x/) version: 2.2.2
* [SQLAlchemy](https://www.sqlalchemy.org/) version: 1.4.44
* [requests](https://requests.readthedocs.io/) version: 2.28.1
* [plotly](https://plotly.com/) version: 5.11.0

	
## Downloading the source code and setup

The recommended way to get the source code of this project is by cloning this remote repository. You can that on any computer with [Git](https://github.com/git-guides/install-git)  installed with the following command:
``` bash
$ git clone https://github.com/filrat2/currencies
```

To run this project, install all required Python modules in your virtual environment with the following command:
``` bash
(venv) $ pip3 install -r requirements.txt
```

Before starting the server for the first time, you must download the data from [National Bank of Poland](https://www.nbp.pl/)  (Narodowy Bank Polski) with the following command:
``` bash
(venv) $ python3 download_data.py start-date end-date
```
Dates (start-date and end-date) must be provided in the **YYYY-MM-DD** format  (ISO 8601 standard), for example:

``` bash
(venv) $ python3 download_data.py 2022-09-29 2022-12-31 #a period of 93 days
```

Historic data for currency exchange rates are available since **2 January 2002** and a **single enquiry cannot cover a period longer than 93 days**. This data comes from [Middle exchange rates of foreign currencies – table A](https://www.nbp.pl/homen.aspx?f=/kursy/ratesa.html). 

To start server on your local machine use following command: 
``` bash
(venv) $ python3 -m flask --app backend run
```

To start server with active debugger on your local machine use following command: 
``` bash
(venv) $ python3 -m flask --app backend --debug run
```
## Planned changes
* loop for downloading data from a period longer than 93 days
* more than one currency on [plotly](https://plotly.com/) chart
* use the [cron](https://crontab.guru/) command-line tool (job scheduler) for daily automatic data download 
* start hosting this project on free online service that gives a way to run Python programs inside a browser, like [PythonAnywhere](https://www.pythonanywhere.com/)
* improve the appearance of the website

## About me

Hi, my name is Filip Ratajszczak and I am a geoinformation student at the Adam Mickiewicz University, Poznan, Poland.
<h4 align="left">Connect with me:</h4>  
<p align="left">  
<a href="https://linkedin.com/in/filip-ratajszczak" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="filip-ratajszczak" height="30" width="40" /></a> <a href="https://discord.gg/f_ratajszczak#9731" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="f_ratajszczak#9731" height="30" width="40" /></a> <a href="https://instagram.com/ratajszcza.k" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="ratajszcza.k" height="30" width="40" /></a>  

</p>