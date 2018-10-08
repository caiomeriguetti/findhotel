from fabric.operations import sudo, put


def download_app_files():
    put('/src/deploy/findhotel_git', '/home/ubuntu/findhotel_key', use_sudo=True)
    sudo('eval "$(ssh-agent -s)" && chmod 400 /home/ubuntu/findhotel_key && \
    ssh-add /home/ubuntu/findhotel_key && \
    cd /home/ubuntu && rm -rf findhotel && \
    git clone git@github.com:caiomeriguetti/findhotel.git')


def setup_instance():
    sudo('curl https://get.docker.com/ -o install_docker.sh')
    sudo('chmod +x install_docker.sh')
    sudo('./install_docker.sh')
    sudo('curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    sudo('sudo chmod +x /usr/local/bin/docker-compose')
    sudo('docker-compose --version')
    sudo('apt-get install -y git')


def start_services():
    sudo('cd /home/ubuntu/findhotel_git && docker-compose up -d --build --force-recreate rest-api geodb')


def import_csv():
    sudo('cd /home/ubuntu/findhotel_git && ./import_csv.sh')


def full_deploy():
    setup_instance()
    download_app_files()
    import_csv()
    start_services()

