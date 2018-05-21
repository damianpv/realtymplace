# RealtyMPlace | Realty Market Place #

Website .....

## Overview ##

### Prerequisites ###

* Debian/Ubuntu
* Python 2.7+
* PIP
* virtualenv/virtualenvwrapper


## Installation ##

### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

#### Activate ####
```
workon {{ project_name }}-env
```


### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Install requirements ###

```bash
cd {{ project_name }}
pip install -r requirements.txt
```
    

### Sync database ###

```bash
python manage.py syncdb
```
    
    
## Running ##
    
```bash
python manage.py runserver --settings=bienes.settings.dev
or
python manage.py runserver --settings=bienes.settings.prod
or
python manage.py runserver --settings=bienes.settings.staging
or
python manage.py runserver --settings=bienes.settings.test
```
    

Open browser to http://127.0.0.1:8000 or http://localhost:8000


### Resize image ###

```bash
pip install -I Pillow

sudo apt-get install libjpeg-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libjpeg
sudo apt-get install libpng
sudo apt-get install libpng-dev
sudo apt-get install libpng12-dev
sudo apt-get install libjpeg62
sudo apt-get install libjpeg62-dev
```

```bash
- I updated sorl-thumbnail to 12.2

- Added this 2 lines to settings.py:
    THUMBNAIL_COLORSPACE = None
    THUMBNAIL_PRESERVE_FORMAT = True 

- python manage.py thumbnail clear_delete_all
```