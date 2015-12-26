
# Installation

## text_classify

The project includes an inhouse written package. In order to install `text_classify`:

```python full_app/text_classify/setup.py install```


## Environment Variables

Default settings for the Flask's app database location
```
FLASK_DB_IN_MEMORY_FLAG=True
```

If you want to run this over a file database use these settings:
```
FLASK_DB_IN_MEMORY_FLAG=False
DATABASE_URL = "/path/to/db/db_file_name.db" 
```

