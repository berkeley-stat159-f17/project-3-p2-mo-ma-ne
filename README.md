[![Build Status](https://travis-ci.org/berkeley-stat159-f17/project-3-p2-mo-ma-ne.svg?branch=master)](https://travis-ci.org/berkeley-stat159-f17/project-3-p2-mo-ma-ne)

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
The data are publicly available from [Crunchbase](https://www.crunchbase.com/). This project specifically uses the [2013 Crunchbase Snapshot](https://data.crunchbase.com/v3.1/docs/2013-snapshot). Access must be requested, and the request is typically approved in a few hours. It is downloaded using a private key you are given once access is granted. The data are provided in a MySQL format and are licensed under Creative Commons with Attribution. The downloaded file is a tar.gz file that contains one .sql file for each of the 11 tables in the database. The database was generated using mysqldump. Store these `cb_*.sql` (where `*` denotes any string) files locally, in a single directory.

### Database setup
After all .sql files are downloaded, create a MySQL database locally. Instructions are provided below, but you will need to ensure that you have MySQL installed. If you have homebrew, we recommend running
```
brew install mysql
```
There are many other mysql installation options, and more information can be found in the [MySQL downloads documentation](https://dev.mysql.com/downloads/installer/).


#### Create p3 database

##### MySQL without a password
If your MySQL database does not require a password, run the following set of commands in the directory containing the `cb_*.sql` files. This will create the database and load the files into it.

```
mysql -u root -e "create database p3"
for sqlfile in cb_*.sql; do
	mysql -u root p3 < sqlfile
done
```

##### MySQL with a password
If your MySQL database has a password, run the following set of commands in the directory containing the `cb_*.sql` files. Enter your password whenever prompted. This will create the database and load the files into it.

```
mysql -u root -p -e "create database p3"
for sqlfile in cb_*.sql; do
	mysql -u root -p p3 < sqlfile
done
```


#### Make sure tables are all loaded

You can check that the files have loaded properly by executing the following from the command line:

```
mysql -u root -p
mysql > use p3;
mysql > SHOW TABLES;
```

### Database connection
We use MySQLdb to make database queries. This required pip installation of mysqlclient, which will automatically be installed when running `make env` as outlined in the instructions below.

## Running our analysis

Once you are ready to begin running the analysis, enter
```
make env
source activate cb
```
in the repository's base directory to create and activate the required conda environment.

If your MySQL database does not require a password, running all of the notebooks can be accomplished by executing

```
make all
```
in the repo's base directory. 

If your MySQL database does require a password, then the `make all` command will fail. It relies on nbconvert to execute the Jupyter notebooks in place, and nbconvert does not accept user input. In this case you must manually execute the notebooks.

## Your analysis of our analysis

Once the notebooks have been run, refer to main.ipynb for a summary of the key results. Important dataframes and figures can also be found in the results folder. All analysis notebooks are in the main directory.

## Licensing conditions

We have licensed our analysis and associated code under the FreeBSD license (see [license.md](https://github.com/berkeley-stat159-f17/project-3-p2-mo-ma-ne/blob/master/license.md)). Please note that this license _only_ applies to our **code**, and not the associated data. The data belongs to Crunchbase. Their license (provided with the datasets after download) expressly prohibits redistribution of the data used in this project without prior permission from Crunchbase. It is for this reason that we have not included the complete datasets with this repository, and have made a conscious effort to limit the size of all tables displayed herein.