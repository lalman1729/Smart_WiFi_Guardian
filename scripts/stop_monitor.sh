#!/bin/bash

echo "[*] Stopping monitor mode..."

sudo airmon-ng stop wlan0mon
sudo service NetworkManager restart

echo "[+] Monitor mode disabled"
