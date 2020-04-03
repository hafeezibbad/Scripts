#!/bin/bash
# Post-install script for ubuntu installation

# Check for update
sudo apt update && sudo apt upgrade && sudo apt dist-upgrade

# Install essential utilities
sudo apt install -y git vlc flashplugin-installer unace unrar zip unzip p7zip-full p7zip-rar sharutils rar uudeview mpack arj cabextract file-roller libxine1-ffmpeg mencoder flac faac faad sox ffmpeg2theora libmpeg2-4 uudeview libmpeg3-1 mpeg3-utils mpegdemux liba52-dev mpeg2dec vorbis-tools id3v2 mpg321 mpg123 libflac++6 totem-mozilla icedax lame libmad0 libjpeg-progs libdvdread4 libdvdnav4 libswscale-extra-2 ubuntu-restricted-extras xbmc cheese filezilla chromium-browser vim ufw tree inkscape gparted gimp shutter remmina putty remmina-plugin-* clamav byobu tcpdump gparted htop traceroute mtr netcat socat htop traceroute mtr netcat socat iftop tshark iperf nmap tcputils cryptsetup lynis rkhunter chkrootkit multitail rdiff-backup duplicity nethogs iotop nethogs iotop screen tmux apt-file inxi makepasswd iptraf curl hddtemp dtrx python-pip build-essential python-dev aptitude git ethtool mtr-tiny pv grc mosh aria2 htop hping3

# Disable shopping suggestions
gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"

# crash report popups, disable apport
sudo sed -i 's/1/0/g' /etc/default/apport
sudo service apport stop

# Install python and related dependencies
sudo apt -y install python3-setuptools python3-dev python3-venv build-essential python-matplotlib python3-pip

# Major Upgrades
sudo apt-get -y dist-upgrade

# Font-powerline 
sudo apt install fonts-powerline  

# Install brave browser
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
sudo sh -c 'echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com `lsb_release -sc` main" >> /etc/apt/sources.list.d/brave.list'
sudo apt update
sudo apt install brave-browser brave-keyring

# Install Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/custom/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions

# Install bat
# https://github.com/sharkdp/bat#installation

# Useful utilities
# https://github.com/MrRaindrop/tree-cli
# https://httpie.org/
# https://hisham.hm/htop/
# https://linuxize.com/post/linux-watch-command/
# https://lnav.org/
# https://kubernetes.io/docs/tasks/tools/install-kubectl/
sudo apt install -y tree httpie watch lnav kubectl

# Color scheme for ubuntu https://github.com/Mayccoll/Gogh/blob/master/content/install.md

# Update DB (locate)
sudo updatedb

sudo apt -y update && sudo apt -y upgrade
# Clean Up
echo "Cleaning Up" &&
sudo apt-get -y -f install &&
sudo apt-get -y autoremove &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean
