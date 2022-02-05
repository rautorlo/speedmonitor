# Connexion Speed Monitor

## Prerequisites
The script uses speedtest-cli util.
1. To install speedtest-cli on **Ubuntu**:
    ```sudo apt install speedtest```
2. To install speedtest-cli using **pip**:
    ```sudo pip install speedtest-cli```

## Summary
This script checks the connection status (ping, download and upload speed) and creates a CSV with the values. The user can launch the script periodicaly in order to store the values in the same CSV file.

## Execution
- The script could be launched using a path argument: ```python3 speed.py /home/user/log``` to save the log files in a specific folder.
- The user can simply launch ```python3 speed.py```. In this option the log files will be created in the same directory that speed.py is located.