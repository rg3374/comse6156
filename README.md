# COMS6156 Midterm Experiment
For the experiemnt we install and run InfluxDB and PostgreDB in a MAC laptop.\
Then we run queries and measure the query response time for both databases.

The scripts for InfluxDB and PostgreSQL insert simulated data into the respective database, run queries, measure the query response time and report it.

The .env (InfluxDB) and the database.ini (PostgreDB) files have not been checked in as they have user tokens and passwords.

## InfluxDB
### Install InfluxDB
1. Download the open source (OSS) version from https://docs.influxdata.com/influxdb/v1/introduction/download/
   Or
   > brew install influxdb

2. Follow directions in https://www.influxdata.com/blog/start-python-influxdb/ \
   Create a token and a bucket using directions above.\
   It should create a .env file with the following contents\
   TOKEN = '<Token>'\
   ORG = "<Org>"\
   BUCKET = '<Bucket>'

### Run InfluxDB
   > influxd

### Install InfluxDB Python client
   Create a virtual env
   >python3 -m venv venv

   Activate
   >source venv/bin/activate

   Install InfluxDB’s client library
   >pip install influxdb-client

### Run the script
   >cd influxDB-Tutorial\
   > python3 \_\_init.py\_\_

## PostgreSQL
### Install PostgreSQL
   > brew install postgresql

### Install PostgreSQL Client
   Create a virtual env
   >python -m venv venv

   Activate
   >source venv/bin/activate

   Install psycopg2
   > pip install psycopg2

### Create the database.ini file with the following contents
   [postgresql]\
   host=localhost\
   database=suppliers\
   user=<username>\
   password=<password>

### Run PostgreSQL
   > /opt/homebrew/opt/postgresql@14/bin/postgres -D /opt/homebrew/var/postgresql@14\
   > createuser -s <username> # this should match username in database.ini

   Follow instructions in https://neon.tech/postgresql/postgresql-python

### Run PostgreSQL Python client
   > psql -U postgres\
   > python connect.py\
   > python create_tables.py\
   > python insert.py\
   > python query.py

References
----------
Code from the following websites have been modified for this experiment:
1. Start with Python and InfluxDB https://www.influxdata.com/blog/start-python-influxdb/
2. PostgreSQL Python https://neon.tech/postgresql/postgresql-python
