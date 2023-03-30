# Django Postgres clery Redis sample application

This is a sample application that has limited functionality like
- create users form (stores in postgres DB)
- show list of users (django)
- search list of users (uses redis cache)

# objective
Main objective is to dockerize this application and there by deploy to any kubernetes cluster

#method
run 
#django_app1> docker compose run app sh -c "django-admin startpap core"

#django_app1> docker compose run app sh -c "django-admin startapp core"

#django_app1> docker compose up --build