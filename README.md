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
for Debian based systems (X11-forwarding currently not supported): 
```sh
./run.sh
```
Arch, Fedora and Windows support will be added in the future. 
## data infrastructer
Postgresql will be used as the databaseservice. EXPERIMENTAL!!!
1. Upload the timetable_database_dump.sql file to your PostgreSQL server. 
2. Set the ip, username, password and databasename in the config.yaml file. 
