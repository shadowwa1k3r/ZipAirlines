# ZipAirlines

Installing dependencies:
    ```poetry install``` 

Running project:\
First activate virtual environment: ```poetry shell```

Then run: ```./manage.py runserver

Api available at url ```127.0.0.1:8000:/api/airplane```

Airplane create api - ```127.0.0.1:8000:/api/airplane/create/```

request body = ```{ "airplane_id": 5, "passenger_count": 100}```

Airplane list api - ```127.0.0.1:8000:/api/airplane/list/```

Airplane by id api - ```127.0.0.1:8000:/api/airplane/list/?airplane_id=<airplane_id>```

Running tests: 
```./manage.py test```

Coverage report: 
```coverage run --source='.' manage.py test```

```coverage report```
