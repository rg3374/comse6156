This file lists commands to install and run InfluxDB and PostgreDB in a MAC laptop.

1. Install InfluxDB
   Download the open source (OSS) version from https://docs.influxdata.com/influxdb/v1/introduction/download/
   Or
   > brew install influxdb

2. Follow directions in https://www.influxdata.com/blog/start-python-influxdb/
   Create a token and a bucket using directions above. It should create a .env file with the following contents
   TOKEN = '<Token>'
   ORG = "<Org>"
   BUCKET = '<Bucket>'

2. Run InfluxDB
   > influxd

3. Install InfluxDB Python client
   #Create a virtual env
   >python3 -m venv venv
   #Activate
   >source venv/bin/activate
   #Install InfluxDB’s client library
   >pip install influxdb-client

3. Install InfluxDB Python client
   #Run the script
   >cd influxDB-Tutorial
   > python3 __init.py__

3. Install PostgreSQL
   > brew install postgresql

4. Install PostgreSQL Client
   #Create a virtual env
   >python -m venv venv
   #Activate
   >source venv/bin/activate
   #Install psycopg2
   > pip install psycopg2

4. Create database.ini file
   # Create the file database.ini file with the following contents
   [postgresql]
   host=localhost
   database=suppliers
   user=<username>
   password=<password>

4. Run PostgreSQL
   > /opt/homebrew/opt/postgresql@14/bin/postgres -D /opt/homebrew/var/postgresql@14
   > createuser -s <username> # this should match username in database.ini

   Follow instructions in https://neon.tech/postgresql/postgresql-python

3. Run PostgreSQL Python client
   > psql -U postgres
   > python connect.py
   > python create_tables.py
   > python insert.py
   > python query.py

The scripts for InfluxDB and PostgreSQL insert simulated data into the respectve database, run queries, measure the query response time and report it.
The .env and the database.ini files have not been checked in as they have user tokens and passwords.
