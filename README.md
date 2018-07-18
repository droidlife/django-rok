# django-rok
> Public url for exposing your local web server

# Overview
Django-rok is an ssh tunnel tool that provide a public url for your local web server and help in testing webhook integrations.
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

3. Instead of django runsver run this command::
    ```python
    python manage.py runrok
    ```    
    This will run the rokserver as well as the django development server.


4. Now go to the url ```http://192.168.1.1:9000``` to access your local development server publicaly.

## Debugging

1. It's possible that your remote host by default doesn't allow port forwarding. To enable this open ```/etc/ssh/sshd_config``` 
    ```
    $ sudo vim /etc/ssh/sshd_config
    ```
    Add the following line somewhere in that config file. Make sure you add it only once!
    ```
    GatewayPorts yes
    ```
    Now restart the service
    ```
    $ sudo service ssh restart
    ```

2. Make sure that the remote port specified is open on the server.

## Additional Configuration
1. Private key can be used to connect to the remote server. To do so add the following parameter to settings.py
     ```python
    ROK_KEY="/path/to/private/key" # private key for remote host connection
    ROK_PASSWORD=None # remote host password is not required since we are using private key
    ```

 2. Rokserver can be started standalone without invoking the django development server. Thing can be achieved by setting env variable
     ```python
    ROK_ENV="PRODUCTION"
    ```
3. Local port for rokserver can be changed by passing the ```-lp``` parameter
    ```
    python manage.py runrok -lp 8080
    ```

## Command Line Usage
  You can also pass the parameters through command line.

  <b>Example:</b>
  ```
  python manage.py runrok -r 192.168.1.1 -rp 9000 -u 'root' -p 'root'
  ```

  To check the command line parameters run ```python manage.py runrok --help```

  ```
  usage: manage.py runrok [-h] [--version] [-v {0,1,2,3}] [--settings SETTINGS]
                        [--pythonpath PYTHONPATH] [--traceback] [--no-color]
                        [-lp LOCAL_PORT] [-rp REMOTE_PORT] [-r REMOTE_HOST]
                        [-u USER_NAME] [-p PASSWORD] [-key PKEY] [-env ENV]

Command to run runrok server along with django development server

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  -lp LOCAL_PORT        The local port to forward the request.
  -rp REMOTE_PORT       The remote port for ssh connection.
  -r REMOTE_HOST        The remote host for ssh connection
  -u USER_NAME          The username for remote host
  -p PASSWORD           The password for remote host(If there)
  -key PKEY             The private key for remote host(If there)
  -env ENV              Which env the server is running on
```

## Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

## Bug / Feature Request

If you find a bug kindly open an issue [here](https://github.com/droidlife/django-rok/issues/new) by including the error thrown.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/droidlife/django-rok/issues/new).
