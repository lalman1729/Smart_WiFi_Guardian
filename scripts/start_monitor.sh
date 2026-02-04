#!/bin/bash

echo "[*] Starting monitor mode..."

sudo airmon-ng check kill
sudo airmon-ng start wlan0

echo "[+] Monitor mode enabled"
