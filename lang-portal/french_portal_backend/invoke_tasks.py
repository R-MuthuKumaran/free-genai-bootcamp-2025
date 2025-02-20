from invoke import task

@task
def init_db(c):
    c.run("python manage.py makemigrations")
    c.run("python manage.py migrate")
    c.run("python manage.py loaddata initial_data.json")  # Assuming you have an initial_data.json fixture

@task
def runserver(c):
    c.run("python manage.py runserver")