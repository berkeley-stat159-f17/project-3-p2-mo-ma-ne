# Can we predict a start-up's success?

## Objective
Our question is: what are the biggest predictors of a start-up's success? We therefore first must define success. We could, for example, consider total investment amount, time to IPO, or time to acquisition. We will explore all of these metrics and more when considering success. While success is difficult to define, we will be sure to define key metrics to benchmark success.

We will look at characteristics of the startup such as the industry, the founder's profile, and the location. Does the location of the startup or the founder's age have a significant effect on time to acquisition or IPO? As we consider each metric, we will examine the correlation among the various metrics. For example, does biotech tend to be concentrated in certain areas more so than other industries?

Aside from characteristics of the company itself, we will look at the investors. Are there certain VC firms that are major predictors of success? How related are the investment decisions of various VC firms? For example, are there some VC firms that almost always invest together? Is it a good idea to raise money earlier or later? Does it depend on the industry?

We can think of our response variable of being set up in two classes - success and failure - so it seems like the best way to go about our analysis would be do use several classification methods. The scikit-learn package has built in methods for to perform classification methods like KNN, logistic regression, or Discriminant Analysis (LDA or QDA), which members of our group are familiar with, but we may also attempt to try different classification methods, or try tree-based methods if possible.

One issue with classification in statistical learning is that often methods will be able to predict well without providing inference. During our analysis we will do some sort of best-subset selection to find the best set of predictors for each statistical learning methods, but it may be hard to extrapolate meaning from those models. One idea we had in order to find which predictors had the most influence is once we are pick our best subset of predictors for a certain methods, we can use a dimensionality reduction method, like PCA, and then see if any of the predictors are particularly correlated to either of the first several principal components. This process will evolve as our analysis gets deeper.

There are endless questions we can ask of this data. Our main aim will be to identify the key contributors to total investment amount and time to acquisition/IPO. However, the various relationships mentioned above will also be explored along the way.

## Data acquisition, database setup, and database connection

### Data acquisition
That data are publicly available. Access must be requested, and the request is typically approved in a few hours. The source of the data is: https://data.crunchbase.com/docs/2013-snapshot. It is downloaded using a private key you are given once access is granted. The data are provided in a MySQL format and are licensed uncer Create Commons with Attribution. The downloaded file is a tar.gz file that contains one .sql file for each of the 11 tables in the database. The database was generated using mysqldump. Store these .sql files locally.

### Database setup
After all .sql files are downloaded, create a MySQL database locally following the database setup instructions below.

#### Create p3 database
```
mysql -u root -p
mysql > create database p3;
```

#### Load tables into database using command line
For each of the 11 .sql files run:
```
mysql -u root -p p3 < cb_acquisitions.sql
```

#### Make sure tables are all loaded
```
mysql -u root -p
mysql > use p3;
mysql > SHOW TABLES;
```

### Database connection
We use MySQLdb to make database queries. This required pip installation of mysqlclient, which will automatically be installed when running `make env` as outlined in the instructions below.

## Running the analysis
Simply run the below commands.
```
make env
source activate cb
make all
```

Refer to main.ipynb for a summary of the key results. Important dataframes and figures can also be found in the results folder. All analysis notebooks are in the main directory.
