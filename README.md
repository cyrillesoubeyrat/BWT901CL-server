# BWT901CL-server
Python based sensor data server for the WITMOTION BWT901CL Bluetooth (2.0) 9 axis inertial sensor
- Setup the bluetooth host conroller, pair the device if needed and connect the selected device
- Output received sensor data to stdout

## Usage
```bash
python sensor_app.py
```
- From the dialog box, select the HC-06 device of interrest
- The sensor data are dumped to standard output
- Press any key in terminal to exit

## Supported platforms
Only tested on Raspberry PI 4 B for now

## Architecture
<img width="780" height="409" alt="architecture" src="https://github.com/user-attachments/assets/401f23f8-6c8b-4122-b113-50e6b43a4481" />
