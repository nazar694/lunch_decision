# Lunch Decision — Daily menu selection system

## To use it, you need to download it from the repository using bash:
```angular2html
git clone https://github.com/nazar694/lunch_decision
cd lunch_decision
```

## After that, you need to build and run docker using bash:
```angular2html
docker-compose build
docker-compose up
```

## After starting the container, you need to run migrations to create the database using bash:
```angular2html
docker-compose exec web python manage.py migrate
```

## The application is accessible at: http://localhost:8000
