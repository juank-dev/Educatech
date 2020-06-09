# Django School

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

This is an example project to illustrate an implementation of multiple user types. In this Django app, teachers can create quizzes and students can sign up and take quizzes related to their interests.

![Django School Screenshot](https://simpleisbetterthancomplex.com/media/2018/01/teacher-quiz.png)

Read the blog post [How to Implement Multiple User Types with Django](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html).

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/Juan-Bogota/Django-Chat-Educatech.git
```

### Install the requirements:

```bash
pip3 install -r requirements.txt
```
Install pgAdmin4

```
pip install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.17/pip/pgadmin4-4.17-py2.py3-none-any.whl
```
#### Configure and run pgAdmin 4

emacs lib/python3.6/site-packages/pgadmin4/config_local.py

```
import os
DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SERVER_MODE = False
```



Create the database:

```
python3 manage.py makemigrations classroom
python3 manage.py makemigrations chat
```


```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.



2. Open & Test Redis:
    - open other Terminal


    - **Run redis-server**
        ```
        $ redis-server
        86750:C 08 Nov 08:17:21.431 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
        86750:M 08 Nov 08:17:21.433 * Increased maximum number of open files to 10032 (it was originally set to 256).
                        _._                                                  
                   _.-``__ ''-._                                             
              _.-``    `.  `_.  ''-._           Redis 3.2.5 (00000000/0) 64 bit
          .-`` .-```.  ```\/    _.,_ ''-._                                   
         (    '      ,       .-`  | `,    )     Running in standalone mode
         |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
         |    `-._   `._    /     _.-'    |     PID: 86750
          `-._    `-._  `-./  _.-'    _.-'                                   
         |`-._`-._    `-.__.-'    _.-'_.-'|                                  
         |    `-._`-._        _.-'_.-'    |           http://redis.io        
          `-._    `-._`-.__.-'_.-'    _.-'                                   
         |`-._`-._    `-.__.-'    _.-'_.-'|                                  
         |    `-._`-._        _.-'_.-'    |                                  
          `-._    `-._`-.__.-'_.-'    _.-'                                   
              `-._    `-.__.-'    _.-'                                       
                  `-._        _.-'                                           
                      `-.__.-'                                               

        86750:M 08 Nov 08:17:21.434 # Server started, Redis version 3.2.5
        86750:M 08 Nov 08:17:21.434 * The server is now ready to accept connections on port 6379

        ```
        
    - **redis-cli ping**
        ```
        $ redis-cli ping
        PONG
        ```
        **Close Redis** with `control` + `c` to quit