# DjangoChan
An Anonymous Imageboard with Django, probably going to be a 4chan clone.

## Table of contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [To-do](#to-do)
5. [License](#license)
   

## Installation
Assuming that you already have git and python installed:  

1.**Clone the repository**

Go in whatever directory you want to download the repository and clone it with:
```bash
git clone https://github.com/giovanni-bandinelli/DjangoChan.git
```
**Note:** Some directories ( './static' at root level '.static/core' inside 'core' app) are specified in the `.gitignore` file and will not be included when you clone the repository

2.**Create and activate a python virtual enviroment**
Go inside the Djangochan directory then run:
##on Windows
```bash
python -m venv venv
venv\Scripts\activate
```
##on Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3.**Add requirements**
```bash
pip3 install -r requirements.txt
```

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

## To-do

A list of missing features etc from the moment I wrote this README

### Frontend wise
- [ ] Overhaul of the UI/UX
   - [ ] Implement markdown (greentext,hyperlinks,other?)
   - [ ] Implement draggable reply form
   - [ ] Polish the look and feel of the standard webapp, make it more responsive
   - [ ] Implement a mobile friendly version
   - [x] Deconstruct the spaghetti code that is the frontend side of the application, organize it better

### Backend wise
- [x] Merge Thread and Post model so that they share the same ID
- [ ] Add user model, both anonymous and logged (for admin and mods)

I'll add more stuff going on.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
  
  
  


