#!/bin/bash

#"Welcome to the Secure connection Environment"
#"########## Tux_Connect ###########"

conn_name=$1
conn_ip=$2
conn_port=$3
conn_user=$4
conn_pass=$5

cd /home/$USER/.Tux_Connect/configs
echo "sshpass -p $conn_pass ssh -p $conn_port $conn_user@$conn_ip" | gpg -c > $conn_name

echo ""$(date)" New Connection '$1' Added" >> ../logs/conn_logs.txt
echo "" >> ../logs/conn_logs.txt

