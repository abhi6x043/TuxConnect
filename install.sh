#!/bin/bash

echo ""
echo "############### Welcome to TuxConnect #################"
echo "############### Designed by abhi6x043 #################"
echo ""

echo "The installer trying to install the program on your computer."
read -p "Do you wish to continue [y/n] " usrnp1

case $usrnp1 in
    [yY][eE][sS]|[yY])
 echo ""
 echo "Installing TuxConnect"
 echo "Make sure you are having a good internet connectioin before installing"
 read -p "Enter to continue" usrnp3
 echo ""
 echo "This program is compatible with Debian/Ubuntu based Distributions"
 echo "So, please be sure that you are having one"
 echo "Otherwise, please wait for the updates. Sorry for the inconvinence caused"
 read -p "Enter [y/n] to Continue: " usrnp2


 case $usrnp2 in
     [yY][eE][sS]|[yY])
  echo ""
  echo "Ready for installatioin"
  echo "Installing Dependencies"
  sudo apt install -y sshpass python3 python3-tk gpg gnome-terminal xed
  mkdir -p /home/$USER/.Tux_Connect
  cp -r * /home/$USER/.Tux_Connect/
  mkdir -p /home/$USER/.Tux_Connect/configs
  mkdir -p /home/$USER/.Tux_Connect/logs
  rm -f /home/$USER/.Tux_Connect/install.sh
  sed -i 's/abhi/'$USER'/g' /home/$USER/.Tux_Connect/docs/add_conn.desktop
  sed -i 's/abhi/'$USER'/g' /home/$USER/.Tux_Connect/docs/tux_connect.desktop
  sed -i 's/abhi/'$USER'/g' /home/$USER/.Tux_Connect/docs/tux_logs.desktop
  sudo cp /home/$USER/.Tux_Connect/docs/*.desktop /usr/share/applications/
  mv tux_connect.mp4 /home/$USER/Videos/
  echo ""
  echo "TuxConnect is Successfully installed"
  echo "Coded by Abhijith S [abhi6x043]"
  echo "How to Use Video (tux_connect.mp4) is now available on your ~/Videos directory"
  echo ""


  ;;
     [nN][oO]|[nN])
  echo ""
  echo "Thank you for showing your interest in TuxConnect."
  echo "We will update you shortly" 
        ;;
     *)
  echo "Invalid input..."
  exit 1
  ;;
 esac

 ;;
    [nN][oO]|[nN])
 echo ""
 echo "Thank you for showing your interest in TuxConnect."
 echo "We will update you shortly" 
       ;;
    *)
 echo ""
 echo "Invalid input..."
 exit 1
 ;;
esac


