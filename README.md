# teach-portal

# prerequisites
* python3.8+

# install
```shell
python3 -m venv .venv
pip install --upgrade pip --no-cache-dir
pip install -r requirements.txt --no-cache-dir
source .venv/bin/activate
```

```shell
# don't forget add to .env file SECRET_KEY and DEBUG in the root directory of the project
SECRET_KEY=
DEBUG=
```

```shell
# migrate models to database
cd teachportal
python manage.py migrate
```

```shell
# fill the database
python fill_db.py
```

```shell
# create a superuser
python manage.py createsuperuser
```

```shell
# run server in the development mode
python manage.py runserver
```

# Pages
* [Teach portal](http://127.0.0.1:8000)
* [Admin page](http://127.0.0.1:8000/admin)