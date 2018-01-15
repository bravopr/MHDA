# Maria Hurricane Disaster App
Backened System for Disaster Site Resources Locator

The data of the application is managed by a relational database system, and exposed to client applications through a REST API. The database engine is relational and our project is implemented in Python. The user will be able to browse categories for resoursece, search for specific items, specify who is supplying items, and who needs the items.

The application manages data from the following tables:

User- The person who either is the administrator of the database system, a person who needs resources or a person who supplies resources

Request- The requests made by a user for one or more resources.

Resources- Resources that are being requested and shows the availability of the requested resources

Request Details- has all the requests made by users with all the details of each request, including date requested, quantity and status.

Purchase- Shows the purchases made by each user, including purchase date, resources purchased or reserved, quantity and requests.

UserAddress- Address where the user is located at.

PaymentInfo- Holds the credit card of every user registered in the database.

The application is organized in three broad layers:

A) App- Main app module takes care to setup the routes for the Rest API and calling the proper handler objects to process the request.

B) Handlers- Handlers takes care of implementing the logic of each REST call. Each handler rely upon the Data Access Objects to extract data from the database, based on the type pf request for a data. They provide the appropriate HTTP response code.

C) DAOs- Data Access Objects (DAOs) take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropiate types. For phase 1, all the DAOs are hardwired.

Requirements:

*The following software is required to run this application*

Pyscopg2 - library to connect to PostgreSQL form Python

Flask - web bases framework to implement the REST API.

PostgreSQL - database engine

PgAdmin3 - app to manage the databases

To run the application, run the app.py file.


