# Car Trade

### About this app

This app is used for cleaning the existing data of cars that was scraped from the web. The data is to be used in a data warehouse that will be used by data analysts.

### Data cleaning and normalization

The data was cleaned using Pandas. After data was cleaned it was copied into a table on a new database created in PostgreSQL. 

After data was uploaded to a database, it was then normalized to the second normal form (2NF).


### Data users

While database and data upload is left to the database admin, data can be used by a data analyst user, who has been granted the permissions to work on created and normalized data.