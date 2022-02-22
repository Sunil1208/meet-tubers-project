# meet-tubers-project

## **NEW PROJECT STEPS**
>
> 1. Install virtualenv (pip install virtualenv)
> 2. Create a new virtual env in the root folder (python3 -m venv venv)
> 3. Activate the virtual environment (source venv/bin/activate)
> 4. Install Django (pip install Django)
> 5. Create a new app (django-admin createapp <app_name>)

## **Record the installed packages in requirements.txt file**
>
> pip freeze > requirements.txt

## **Run server**
>
> python3 manage.py runserver

## **Migration steps**
>
> - python3 manage.py makemigrations
> - python3 manage.py migrate
>
## **Create super user**
>
> python3 manage.py createsuperuser

## **Creat a new app**
>
> django-admin startapp <app_name>
> e.g. django-admin startapp api

## **Category**

> ### Steps to be taken
>
> - Create model
> - Register in admin
> - serializers.py file to serialize data in JSON
> - Views to get all category
> - Setup URL
