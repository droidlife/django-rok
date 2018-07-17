# django-rok
> Public url for exposing your local web server

# Overview
Django-rok is an ssh tunnel tool that provide a public url for your local web server and help in testing webhook integreations.
The django-rok is inspired from <a href="https://ngrok.com/" traget="_blank">ngrock</a> and built using <a href="http://www.paramiko.org/" targat="_blank">paramiko</a>. 

# Installation

Install using `pip`...

    pip install django-rok
    

# Quick Start
1. Add <b>"django_rok"</b> to your INSTALLED_APPS setting like this::
   ```python
    INSTALLED_APPS = [
        ...
        'django_rok',
    ]
    ```
2. Add the following parameters to the settings.py::
    ```python
    ROK_REMOTE_HOST="192.168.1.1" # remote host ip
    ROK_REMOTE_PORT=9000 # remote host port to connect to
    ROK_USERNAME="root" # remote host username
    ROK_PASSWORD="root" # remote host password
    ```

3. Instead of djnago runsver run this command::
    ```python
    python manage.py runrok
    ```    
    This will run the rokserver as well as the django development server


4. Now go to the url ```http://192.168.1.1:9000``` to access your local development server publicaly.
