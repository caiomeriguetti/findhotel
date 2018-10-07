from fabric.operations import local

local(' && '.join([
    'cd /src/deploy',
    'eval "$(ssh-agent -s)"'
    'ssh-add findhotel.pem',
    'fab setup_instance -H ubuntu@54.174.222.228'
]))