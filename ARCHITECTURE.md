# 🏗️ Smart Wi-Fi Guardian – System Architecture

### Architecture Explanation

1. User accesses the web dashboard via a browser  
2. Frontend sends requests to Flask REST APIs  
3. Backend scans the local network using ARP  
4. Connected devices and activity data are processed  
5. Results are returned and visualized in real time  

This modular design allows easy extension for threat detection,
blocking policies, and intrusion prevention.


[User Browser]
        |
[Dashboard UI]
        |
[Flask API Server]
   |           |
[ARP Scanner] [Stats Engine]
        |
[Router / Network]
        |
[Connected Devices]
