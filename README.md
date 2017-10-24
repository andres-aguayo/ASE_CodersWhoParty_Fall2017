# scheduLIT
### A collaborative trip planning web application designed and built by CodersWhoParty.

This repository contains all assignments, submissions, and code related to our semester project for Advanced Software Engineering (COMSW4156) taught by Gail Kaiser in the Fall of 2017 at Columbia University. TA mentor is Tuhin Chakrabarty.

## Group members:
#### Dominique Gordon, dlg2156
#### Matias Lirman, ml37007
#### Julian Silerio, jjs2245
#### Andres Aguayo, aa3642

## Overview:

From experience, planning a trip with multiple people becomes a burden very quickly as
differences in flights, hotels, schedules, and interests causes different itineraries and a
nightmare in planning and scheduling. We are proposing a way to consolidate all this
information into an easy to use, simple, and efficient calendar app. Our application will allow
users to add information about their specific trip, including events, hotel and flight information,
scheduled events, and tentative activities. This user specific itinerary can then be shared with
and easily viewed by other members of the trip. This would make planning a trip with multiple
users very manageable and allow for easy access to everyone's tentative schedule.

Whether it is an extende family reunion, a jam-packed business trip, or even a fraternity
spring break to a beach, scheduLIT makes group planning and coordination a breeze.


# Flask Skeleton

### PULLED FROM [flask-skeleton](https://github.com/realpython/flask-skeleton/)
#### Modified by Julian and Andres

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Basics

1. Create and activate a virtualenv
1. Install the requirements
  - $ pip install -r requirements.txt

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
