# **DJANGO API TEMPLATE**

This documentation provides an overview of the DJANGO api and highlights the steps required to get the application up and running on your machine. 

### Running the application
Install Docker on your machine and then run `docker-compose up -d` to start the database. The database will be available on port `5432`. The database name is `database` and the username is `user` and the password is `password`. 

Running the `docker-compose up -d` will also give you access to a pgadmin instance on port `8001`. You can use this to connect to the database and view the tables. Use `database` as the hostname when adding the database to pgadmin on this port. If you have pgadmin installed on your machine, you can also use that to connect to the database using `localhost` as your hostname.

The command `docker-compose up -d` will also start a Mailhog mail server on port `8025`. You can use this to view emails sent by the application. 

The command will also launch the application and listen for any changes on port 8000.

Please see the docker-compose.yml file for more details on the application setup.

### Application Entry Point
To get the full flow of the application and endpoints start by opening the `config.urls.py` file.

### Additional Improvements
The app can be improved further by adding the following:

- Unit tests
- Deployment pipeline
- App monitoring (i.e Cloudwatch logs and setting up alarms)

