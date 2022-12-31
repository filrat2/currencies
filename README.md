## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#downloading-the-source-code-and-setup)

## General info
This project is ...
	
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

To run this project, install all required modules in your virtual environment with the following command:
``` bash
$ pip3 install -r requirements.txt
```

Before starting the server for the first time, you must download the data from [National Bank of Poland](https://www.nbp.pl/)  (Narodowy Bank Polski) with the following command:
``` bash
$ python3 download_data.py start-date end-date
```
Dates (start-date and end-date) must be provided in the **YYYY-MM-DD** format  (ISO 8601 standard), for example:

``` bash
$ python3 download_data.py 2022-09-29 2022-12-31 #a period of 93 days
```

Historic data for currency exchange rates are available since **2 January 2002** and a **single enquiry cannot cover a period longer than 93 days**. This data comes from [Middle exchange rates of foreign currencies – table A](https://www.nbp.pl/homen.aspx?f=/kursy/ratesa.html).
