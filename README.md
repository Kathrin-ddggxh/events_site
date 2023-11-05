# events_site
Site for artists to upload upcoming events and list past events. Django app.


## Virtual environment

### Setup

Run ``python -m venv .venv`` in terminal.

The python .gitignore file includes ``venv`` and ``.venv`` by default. It's advised to stick with this naming convention when creating a virtual environment.

If standard python .gitignore file was not used when creating repository, the name of the virtual environment has to be created manually to the custom .gitignore file.

### Activate environment

Run ``.venv/Scripts/activate`` in terminal.

If environment was named differently, adjust command accordingly (``<env-name>/Scripts/activate``)

Ensure to have virtual environment activate when running the application or installing any packages.


## Installed Dependencies

### Django

To install latest version of Django: ``pip install django``

#### Start Django Project

To start project: ``django-admin startproject <project-name> .``

The space and full-stop ensure the project file is installed in the current directory (the root directory conventionally).

#### Run Django App

To run app: ``python manage.py runserver``

To stop runserver: Ctrl + C

#### Start Django App

To start new app: ``python manage.py startapp <app-name>``


## Setting up environment variables

This is important to avoid exposing sensitive information such as secret keys or API keys in the Github repository.

This information will instead be stored in an environment file ``env.py`` which will not be push to Github (**add to .gitignore file before pushing to Github!**).

The information can be accessed by other files from the env.py file:

In settings.py at the top, include ``import os`` and replace the original value of the ``SECRET_KEY`` value with ``SECRET_KEY = os.environ.get("SECRET_KEY")``.

In the root directory, create an ``env.py`` file and add ``import os``. 
The ``SECRET_KEY`` variable is created inside the environment by including ``os.environ["SECRET_KEY"] = '<secret-key-value>'`` Then give it a new value (use secret key generator).

To get access to the environment file in settings.py, include 
```python:
if os.path.exists('env.py'):
    import env
```

## Configuring Debug in settings.py

The ``DEBUG`` variable in settings.py should be set to ``True`` locally, but be ``False`` in production (deployed version).

To not have to constantly change it, set the variable in settings.py to 
```python:
DEBUG = "DEVELOPMENT" in os.environ  # checks if DEVELOPMENT variable exists in environment. if it does, DEBUG is true, if not, DEBUG is false
```
Then in env.py add:
```python:
os.environ["DEVELOPMENT"] = "AnyValueWillEquateToTrue"
```

## Technologies used

- Bootstrap 5 [CDNs](https://cdnjs.com/libraries/bootstrap/5.3.2) and [Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

**Compressing/Resizing Images:** [ILoveImg](https://www.iloveimg.com/)


## Credits

### Media

#### Images / Icons

*star-logo* (placeholder only): https://ih1.redbubble.net/image.423993253.0830/flat,750x1000,075,f.jpg

#### Fonts

*Roboto* and *Karantina*: [Google Fonts](https://fonts.google.com/)