# the app

# how to run the app

```docker-compose up -d --force-recreate --build```

# how to import the csv 

```./import_csv.sh```

# project structure

the library is inside geoservice dir
the api is inside rest-api dir
the csv importer is inside csv_importer

#deploy

TODO: create cloud formation template

Created a VPC
Created a Internet gateway
Create a route for 0.0.0.0/0 pointing to internet gateway to provide internet access



