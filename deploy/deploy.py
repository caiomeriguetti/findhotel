from fabric.operations import local
import sys

task_name = sys.argv[1]

local(' && '.join([
    'cd /src/deploy',
    'eval "$(ssh-agent -s)"'
    'ssh-add findhotel_ec2.pem',
    'fab %s -H ubuntu@35.174.212.246' % task_name
]))