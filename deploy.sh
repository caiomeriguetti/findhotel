#!/bin/bash

docker-compose run deployer bash -c "cd /src/deploy && python deploy.py"