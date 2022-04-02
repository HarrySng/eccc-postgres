# Install superset


https://superset.apache.org/docs/installation/installing-superset-from-scratch/   
Revert back "Markup" version as the current version is no longer supported.
Install inside a venv.
```
python -m pip install markupsafe==2.0.1
```

## Install psycopg2
Needs to be installed from source
```
sudo apt-get install libpq-dev
sudo apt-get install python3-psycopg2
source venv/bin/activate
pip install psycopg2
sudo systemctl restart postgresql.service
```


Setup
```
superset db upgrade
export FLASK_APP=superset
superset fab create-admin
superset load_examples
superset init
```

Create shell file to run
```
#!/bin/bash
source venv/bin/activate
superset run -p 8088 --with-threads --reload --debugger
```
http://localhost:8088/

## Install postgres
```
sudo systemctl start postgresql.service
```

New user and db
```
sudo -i -u postgres
psql
CREATE ROLE user123 WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'mypass';
CREATE DATABASE mydb;
GRANT ALL PRIVILEGES ON DATABASE mydb to user123;
```

Edit the following file
```
sudo nano /etc/postgresql/12/main/pg_hba.conf   
# Change all "peer" to "md5"
```
Restart postgresql.service.   
This will allow terminal login using new user. If this is not edited, it defaults to looking for a database with the current Linux username.   


## Install phppgadmin
Set to false to let sudo users login   
```
sudo vim /etc/phppgadmin/config.inc.php
$conf['extra_login_security'] = false;
```

http://localhost/phppgadmin/

## Connect Postgres to superset
Connection string looks like:   
```
postgresql://{username}:{password}@{host}:{port}/{database}
```

In this case:
```
postgresql://eccc:eccc@localhost:5432/eccc
```