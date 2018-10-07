from fabric.operations import sudo, put


def setup_instance():
    # sudo('curl https://get.docker.com/ -o install_docker.sh')
    # sudo('chmod +x install_docker.sh')
    # sudo('./install_docker.sh')
    # sudo('mkdir -p /home/ubuntu/findhotel')
    # put(local_path='/src/geoservice', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # put(local_path='/src/python_env', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # put(local_path='/src/rest-api', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # put(local_path='/src/.env', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # put(local_path='/src/docker-compose.yml', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # put(local_path='/src/import_csv.sh', remote_path='/home/ubuntu/findhotel', use_sudo=True)
    # sudo('curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    # sudo('sudo chmod +x /usr/local/bin/docker-compose')
    # sudo('docker-compose --version')
    sudo('cd /home/ubuntu/findhotel && docker-compose up -d --build')
