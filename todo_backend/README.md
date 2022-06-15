# TODO_BACKEND

### Start project
```
docker-compose up
```

### Run migrations 
```
> docker-compose exec web bash
> python manage.py migrtate
> python manage.py createsuperuser
```

### Run celery 
```
> docker-compose exec web bash
> celery -A todo worker -l INFO
```

### Don\'t forget to give users permission to CRUDE