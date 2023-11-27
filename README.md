# DjangoChan
An Anonymous Imageboard with Django, probably going to be a 4chan clone.

## Table of contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)
   

## Installation
Assuming that you already have git and python installed:  

1.**Clone the repository**

Go in whatever directory you want to download the repository and clone it with:
```bash
git clone https://github.com/giovanni-bandinelli/DjangoChan.git
```
**Note:** Some directories ( './static' at root level '.static/core' inside 'core' app) are specified in the `.gitignore` file and will not be included when you clone the repository

2.**Create and activate a python virtual enviroment**
I called mine 'vEnv', remember to change the .gitignore accordingly 
'''bash
python -m venv vEnv
'''

3.**Add requirements**
```bash
pip3 install -r requirements.txt
```
**important**
I'm using postgres as my DBMS so you should either install it (if it's not already present on your machine) and create a database matching the infos inside the 'DATABASE = {}' section
in settings.py or tweak them to fit your needs, even changing DBMS should go fairly smooth i'm pretty sure.

4.**Run migrations**
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
## Usage
After completing the installation,open a terminal inside of the project's directory and run:
```bash
python manage.py runserver
```
et voilà
**reminder**
This repository is still in development stage, Work on deployment mode hasn't started yet 
## Contributing 
At the moment I want this to be a solo project and no contributions will be accepted

 
