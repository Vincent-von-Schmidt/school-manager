# school-manager
## features
- timetable 
  - datatypes
    - database -> Postgresql
    - xml
    - json
  - Archenhold Gymnasium -> Vetretungsplan integration
- homework planer
  - google calendar sync
- exam planer 
  - google calendar sync 
- multi language support
  - en_us
  - de_de
  - more will be added soon

## build and run
### With custom Python installation: 
```sh
python3 -m pip install -r requirements.txt
python3 main.py
```
### Without Python installation: 
This will install docker on your system. The python enviroment will be created within a docker container. 
#### Debian based: 
```sh
./run.sh
```
#### Windows (not tested):
```
.\run.ps1
```
## data infrastructer
### PostgreSQL
1. Upload the database_dump_postgresql.sql file to your PostgreSQL server. 
2. Set the ip, username, password and databasename in the config.yaml file. 
### MySQL
1. Upload the database_dump_mysql.sql to your MySQL server.
2. Set the ip, port, username, password and the databasename in the config.yaml. 