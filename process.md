# Data acquisition, database setup, and database connection

## Data acquisition
That data are publicly available. Access must be requested, and the request is typically approved in a few hours. The source of the data is: https://data.crunchbase.com/docs/2013-snapshot. It is downloaded using a private key you are given once access is granted. The data are provided in a MySQL format and are licensed uncer Create Commons with Attribution. The downloaded file is a tar.gz file that contains one .sql file for each of the 11 tables in the database. The database was generated using mysqldump. Store these .sql files locally.

## Database setup
After all .sql files are downloaded, create a MySQL database locally following the database setup instructions below.

### Create p3 database
```
mysql -u root -p
mysql > create database p3;
```

### Load tables into database using command line
For each of the 11 .sql files run:
```
mysql -u root -p p3 < cb_acquisitions.sql
```

### Make sure tables are all loaded
```
mysql -u root -p
mysql > use p3;
mysql > SHOW TABLES;
```

## Database connection
We use MySQLdb to make database queries. This requires the installation of mysqlclient.
```
pip install mysqlclient
```



