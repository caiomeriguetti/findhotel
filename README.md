# the app

# how to run the app

```docker-compose up -d --force-recreate --build```

# how to import the csv 

```./import_csv.sh```

# project structure

the library is inside geoservice dir
the api is inside rest-api dir
the csv importer is inside csv_importer
the deployment scripts are in deploy dir

there is a directory called python_env where you can find the Dockerfile for python environment
this Dockerfile is shared by rest-api and csv_importer

# time spent to create this solution

I worked on this solution for 5 hours on Sunday. This was my only available time on the weekend

#deploy

What i did manually in AWS:

Created a VPC
Created a Internet gateway
Create a route for 0.0.0.0/0 pointing to internet gateway to provide internet access
Created a security group for the instance
Created an elastic ip for the instance

I know that we can automate the tasks above with CloudFormation, Terraform or other similar technology but i didnt have 
enought time to do so.

But, suposing that we have an instance running somewhere else and it is ssh-able(elastic ip 35.174.212.246 is hardcoded in deploy/deploy.py):

The full deployment process:

```./deploy.sh full_deploy```

We can also run separated tasks with:
    
```./deploy.sh <task_name>```

Just to give an example, if you just want to run the installations:

```./deploy.sh setup_instance```

the list of tasks are in /deploy/fabfile.py

# The api endpoint on AWS

http://35.174.212.246:8080/205.8.7.210/info

