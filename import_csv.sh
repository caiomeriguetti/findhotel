#!/bin/bash

docker-compose up -d geodb
docker-compose run csv-importer bash -c "cd /src/csv_importer && python import_csv.py"