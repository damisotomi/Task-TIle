# Problem statememt

Pre-Interview Task

Django plays a big role in abstracting away the need to deal with database management. However, this means as developers we have to make good choices about what structures and data our models contain and how they are related to enable the ORM to work most efficiently.

In our research software we have task objects that a user has to complete, each task has a title, an order field, a description and a type (such as survey, discussion, diary). We group tasks together in a container which we call a tile. Each tile has a launch date and a status. The status can be either live, pending or archived. A tile can be made up of one or many tasks. A task can only belong to a single tile.

Therefore, this exercise is to create a Django 3.x project that contains task and tile models, configured as outlined above. We would also like you to create a simple API to allow interaction with these models with DRF (Django Rest Framework version 3.10), using the appropriate viewsets and serialisers provided by DRF. No frontend work is required for this task.

This Project implements a task and tile model as outlined above and also an API to allow interaction with this models

## Extra Features

-I Used ModelViewset class to expose the APIs
-I implemented Pagination, Filtering and Searching on the APIs
-I made the serializer to be as robust as possible. Each Tile also returns a list of the task under it
-I implemented DefaultRouter using DRF routers
-Loaded up the db using dummy data
-I set up the admin interface using the credentials below
Email: tasktile@gmail.com
username: tasktile
Password: tasktile

## To Run the Application

-Activate the virtual environment by navigating to venv/Scripts/Activate.ps1
-Install all dependencies using `pip install -r requirements.txt`
-Run `py manage.py runserver` to start the development server
-Click on any of the API links shown on screen to interact with the API using DRF browseable API
