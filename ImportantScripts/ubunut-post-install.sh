#!/bin/bash
# post installing script for Ubuntu 14.04 Trusty Tahr Desktop
#
# Check for Updates
sudo apt-get -y update
# Upgrade Packages
sudo apt-get -y upgrade
# Major Upgrades
sudo apt-get -y dist-upgrade
# Install Essentials
sudo apt-get -y install dconf-editor nitrogen synaptic vlc gimp gimp-data gimp-plugin-registry gimp-data-extras bleachbit flashplugin-installer unace unrar zip unzip p7zip-full p7zip-rar sharutils rar uudeview mpack arj cabextract file-roller libxine1-ffmpeg mencoder flac faac faad sox ffmpeg2theora libmpeg2-4 uudeview libmpeg3-1 mpeg3-utils mpegdemux liba52-dev mpeg2dec vorbis-tools id3v2 mpg321 mpg123 libflac++6 totem-mozilla icedax lame libmad0 libjpeg-progs libdvdread4 libdvdnav4 libswscale-extra-2 ubuntu-restricted-extras xbmc cheese filezilla chromium-browser vim ufw tree inkscape gparted gimp shutter remmina putty remmina-plugin-* clamav byobu tcpdump gparted htop traceroute mtr netcat socat htop traceroute mtr netcat socat iftop tshark iperf nmap tcputils cryptsetup lynis rkhunter chkrootkit multitail rdiff-backup duplicity nethogs iotop nethogs iotop screen tmux apt-file inxi makepasswd iptraf curl hddtemp dtrx python-pip build-essential python-dev aptitude git ethtool mtr-tiny pv grc mosh aria2 htop hping3
sudo apt-get install xpad
sudo apt-get -y install python-virtualenv python-setuptools python-dev build-essential python-matplotlib
sudo pip install --upgrade virtualenv
sudo apt-get install -y python-pip
sudo apt-get -y install git
sudo pip -y install Glances
sudo pip -y install PySensors
# Install oracle Java 8
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer
# Play encrypted DVD in Ubuntu 14.04
sudo apt-get -y install libdvdread4
sudo /usr/share/doc/libdvdread4/install-css.sh
# Disable shopping suggestions
gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"
# Chromium Flash
sudo apt-get -y install pepperflashplugin-nonfree
sudo update-pepperflashplugin-nonfree --install
# crash report popups, disable apport
sudo sed -i 's/1/0/g' /etc/default/apport
sudo service apport stop
# Install Handbrake with MP4
sudo apt-get purge handbrake # remove any old versions
sudo add-apt-repository ppa:stebbins/handbrake-snapshots
sudo apt-get -y update
sudo apt-get -y install handbrake-gtk
# Enable Firewall
sudo ufw enable
# Update DB (locate)
sudo updatedb
# Clean Up
echo "Cleaning Up" &&
sudo apt-get -y -f install &&
sudo apt-get -y autoremove &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean
#
sudo apt-get -y update && sudo apt-get -y upgrade
