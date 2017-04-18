## Setting up development environment using Virtual Machine environment
This guide is written for setting up development environment for Keymanager (and runtime) development using a virtual machine  (vm) setup.
The code repositories will be shared between Host and VM via NFS sharing. The dependencies will be installed in VM and Pycharm IDE will be setup in host machine to do development work. 

- For more in depth information check README.FIRST.md
- In this guide, both host and VM are running Ubuntu 16.04.2 (Xenial Xerus)

Download and install Virtualbox [link](https://www.virtualbox.org/wiki/Linux_Downloads) on host machine
Setup a VM running Ubuntu 16.04 [source](http://releases.ubuntu.com/16.04/).
- Recommended hardware specifications for VM: Memory >= 3072MB, HDD >= 20GB
- Setup the networking in Bridged Adapter mode (virtualbox-manager -> vm -> settings -> Network -> Attached to (change to Bridged Adapter))

### Clone the repositories on Host Machine
```sh
sudo apt-get update
sudo apt-get install -y git
mkdir shared
cd shared
git clone https://gitlab.ssh.com/ukm/keymanager.git
git clone https://gitlab.ssh.com/ukm/runtime.git
```

### Setup NFS sharing on host machine
Install NFS-Server on localmachine 
```sh 
sudo apt-get update
sudo apt-get install nfs-kernel-server
```
Export the paths (to be shared) from host machine
```sh
sudo vi /etc/exports
```
Add following lines to /etc/exports (Please replace <username> and <ip> with respective information)



### Compile runtime
```sh
make check-env
sudo apt-get install build-essential automake autoconf libtool libffi-dev libreadline-dev bison flex libcrack2-dev libsasl2-dev libsqlite3-dev
make check-env
make all RUNTIMEDIR=~/projects/runtime_compiled
```

### Make keymanager
```sh
make local RUNTIME=~/projects/runtime_compiled
make check
make build RUNTIME=~/projects/runtime_compiled
```

### Setup psql
```sh
sudo apt-get install postgresql postgresql-contrib
sudo -su postgres
# Use password Finnair12
createuser -P -s keymanager
sudo vi /etc/postgresql/9.3/main/pg_hba.conf
# Edit as follows:
local   all             all                                     trust
host    all             all             127.0.0.1/32            md5

sudo service postgresql restart
```

### Setup nginx
```sh
sudo apt-get install nginx
sudo service nginx stop
sudo bin/setup-nginx
sudo cp ~/projects/keymanager/env/nginx/sshmgr /etc/nginx/conf.d/default.conf
sudo cp ~/projects/keymanager/env/nginx/sshmgr-rate.conf /etc/nginx/conf.d/00-rate.conf

# Modify /etc/nginx/conf.d/default.conf
ssl_certificate      /etc/ssl/certs/ukmserver.crt;
ssl_certificate_key  /etc/ssl/private/ukmserver.key;
ssl_client_certificate /etc/ssl/certs/ukmca.crt;

sudo service nginx start
```

### Setup Keymanager & run migrations
```sh
make autosetup
sudo mkdir /etc/ssh2
# Use hostkey as key filename
ssh-keygen -t rsa -b 4096 -C "firstname.lastname@ssh.com"
sudo cp ~/.ssh/hostkey* /etc/ssh2
```

### Run Backend & Frontend
```sh
./bin/runbackend
./bin/runfrontend
```
Go to https://localhost/
