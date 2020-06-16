# Educatech
## Sharing the passion for knowledge and technology

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0-brightgreen.svg)](https://djangoproject.com)

Our platform is aimed at topics and communities related to technology for example bases and foundations of programming, software, and hardware that allows the user in a more interactive way to have personalized advice, to communicate with a "teacher" through a chat or video call to facilitate contact, which is a plus in our product.
<p align="center"><img src="images/home.jpeg" width="700"></p>

##  Technology

<p align="center"><img src="images/Technology.png" width="700"></p>


First, clone the repository to your local machine:

```bash
git clone https://github.com/Juan-Bogota/Educatech.git
```
### Create virtual environment

Review this [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
) 
* Create a Virtual Environment

### Install the requirements:

```bash
pip3 install -r requirements.txt
```
#### Install pgAdmin4 (optional)

```
pip3 install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.17/pip/pgadmin4-4.17-py2.py3-none-any.whl
```
#### Configure and run pgAdmin 4 (optional)
After completing the installation steps,you have to open the folder of virtual enviroments, you have to create a configuration file to run this software. Create a new file named ```config_local.py``` in lib/python3.6/site-packages/pgadmin4/ folder using favorite editor.

```
emacs lib/python3.6/site-packages/pgadmin4/config_local.py
```
Add the following content in **config_local.py**.
```
import os
DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SERVER_MODE = False
```

Now, use the following command to run pgAdmin.
```
python3 lib/python3.6/site-packages/pgadmin4/pgAdmin4.py
```
review pgAdmin in this [link](https://linuxhint.com/install-pgadmin4-ubuntu/)

## Create the database:

#### open postgres

```
$ sudo -i -u postgres

postgres$ psql

postgres# CREATE DATABASE dbeducatech;

```

#### migrations
```
python3 manage.py makemigrations classroom
python3 manage.py makemigrations chat
```


```bash
python3 manage.py migrate
```

Finally, run the development server:

```bash
python3 manage.py runserver
```

The project will be available at **127.0.0.1:8000**.



## 2. Open & Test Redis:
- **Open other Terminal**
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
- **Close Redis** with `control` + `c` to quit
