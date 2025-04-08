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

## For testing you need to run test using bash:
```angular2html
docker-compose exec web pytest
```

## And for checking flake8 you need to use bash:
```angular2html
docker-compose exec web flake8
```

## The application is accessible at: http://localhost:8000

## Links for working with API:
- ### http://localhost:8000/api/user/registration - Creating employee
- ### http://localhost:8000/api/user/login - Authentication
- ### http://localhost:8000/api/restaurants - Creating restaurant
- ### http://localhost:8000/api/menus - Uploading menu for restaurant
- ### http://localhost:8000/api/menus/today - Getting current day menu
- ### http://localhost:8000/api/votes - Vote for menu
- ### http://localhost:8000/votes/today - Getting votes results for the current day
