# REST API for Car Park with Drivers

# Installation

To run on a PC, must be installed:
[Python 3.9](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

## Windows 10 and Linux
In the folder with your project сlone repository

```sh
$ git clone https://github.com/sanromeo/CarPark-Test-Task.git
```

### 1) Django setup

At the root of the project, create a virtual environment and activate it

```sh
$ cd CarPark-Test-Task
$ python -m venv “venv”
$ .\venv\Scripts\activate (for Linux: source ./venv/bin/activate)
```

#### All subsequent actions should be performed inside the virtual environment.

Install all required dependencies for Django to work

```sh
$ pip install -r requirements.txt
```

Install all required migrations, make sure db.sqlite3 file was generated

```sh
$ python manage.py migrate
```

Run the project

```sh
$ python manage.py runserver
```
Copy _http://127.0.0.1:8000/_ and paste it to your browser

Finally you can check some endpoint`s in README.md
