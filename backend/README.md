# Setup

## Flask Backend w. Poetry
The project's backend is built using Poetry package manager. The ```poetry.lock``` file contains all project dependencies.  To install them, make sure python-poetry is installed beforehand. Then in a terminal, cd to the project's root folder, and enter:
```
poetry install
```

This will set the project up with all its dependencies, within a Poetry virtual env. To find its path for use in your IDE's interpreter settings, enter:
```
poetry env info --path
``` 


To add new packages to the project:
```
poetry add some-python-package
```
You'll want to create a ```app_key.json``` file in the project's root folder. It contains the app's secret key, and is gitignored. Formatted like: 
```
{
  "app_key": "some-secret-key"
}
```

also create a ```db_credentials.json``` file in the root, it is gitignored as well. Format  like so:
```
{
  "driver": "mysql",
  "user": "admin",
  "password": "supersecretpassword",
  "host": "localhost",
  "port": 3306,
  "db": "database_name"
}
```

To run the server enter: 
```
flask run
```

##### NOTE: if the ```migrations``` folder is present, then skip this step)
if not, you can initialize migrations with Flask-Migrate already installed. 
```
flask db init
```

After the migrations folder is created with the above command, you can run them with 
```
flask db migrate -m"sample comment for the migration"
```

You then apply the migrations afterwards with:
```
flask db upgrade
```

