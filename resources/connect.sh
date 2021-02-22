#!/bin/bash

#"Welcome to Tux_Connect"
#Designed by abhi6x043

conn_name=$1

cd /home/$USER/.Tux_Connect/configs/
echo ""$(date)" Connecting to '$1'" >> ../logs/conn_logs.txt
echo "" >> ../logs/conn_logs.txt

connect_Nw=`gpg -d $conn_name`
$connect_Nw


