# WiFi RSSI Heatmap and Signal Mapping System

A real-time wireless signal mapping and visualization system developed using ESP8266, Firebase Realtime Database, SD card logging, and RSSI-based distance estimation. The system collects WiFi signal strength measurements, stores them locally and on the cloud, and generates signal coverage heatmaps for wireless network analysis.

## Overview

Understanding wireless signal coverage is critical for network planning, indoor localization, IoT deployments, and communication system optimization. This project measures WiFi Received Signal Strength Indicator (RSSI) values, estimates transmitter distance using propagation models, and visualizes signal distribution through heatmaps.

The system combines embedded sensing, cloud integration, local data logging, and data visualization to provide a complete wireless signal analysis platform.

## Features

* Real-Time WiFi RSSI Monitoring
* ESP8266-Based Data Acquisition
* Distance Estimation from RSSI
* SD Card Data Logging
* Firebase Realtime Database Integration
* I2C LCD Status Display
* Signal Coverage Mapping
* RSSI Heatmap Generation
* Cloud-Based Data Storage
* Serial Plotter Visualization Support

## Hardware Components

| Component        | Purpose            |
| ---------------- | ------------------ |
| ESP8266 NodeMCU  | Main Controller    |
| WiFi Transmitter | Signal Source      |
| SD Card Module   | Local Data Storage |
| I2C LCD (0x27)   | Real-Time Display  |
| Power Supply     | System Power       |

## System Architecture

```text
WiFi Access Point
        │
        ▼
ESP8266 RSSI Scanner
        │
 ┌──────┴──────┐
 ▼             ▼
SD Card     Firebase
Logging      Database
 │             │
 └──────┬──────┘
        ▼
 Data Processing
        │
        ▼
Heatmap Generation
        │
        ▼
Coverage Analysis
```

## Working Principle

1. ESP8266 scans nearby WiFi networks.
2. RSSI values are collected from the target SSID.
3. Distance is estimated using a path loss model.
4. Measurements are displayed on the LCD.
5. Data is stored on the SD card.
6. Records are uploaded to Firebase.
7. Collected data is processed to generate signal heatmaps.
8. Coverage patterns are analyzed for optimization.

## Technologies Used

### Programming

* Embedded C
* Arduino IDE
* Python

### Embedded Systems

* ESP8266
* I2C Communication
* SPI Communication

### Cloud Services

* Firebase Realtime Database

### Data Processing

* NumPy
* Pandas
* Matplotlib

## Sample Data Format

```csv
Timestamp,RSSI(dBm),Distance(m)
10:00:05,-48,1.2
10:00:10,-54,2.1
10:00:15,-61,3.8
10:00:20,-67,5.2
```

## Distance Estimation Model

The system estimates distance using a logarithmic path-loss model:

```text
Distance = 10^((RSSI0 - RSSI)/(10 × n))
```

Where:

* RSSI0 = Reference RSSI at 1 meter
* RSSI = Measured Signal Strength
* n = Environmental Path Loss Exponent

## Applications

* Wireless Network Planning
* Indoor Localization Research
* Smart Building Deployments
* IoT Infrastructure Analysis
* Signal Coverage Optimization
* Academic Research
* Wireless Communication Studies

## Example Outputs

### Real-Time Monitoring

```text
RSSI : -57 dBm
Distance : 2.4 m
```

### Heatmap Visualization

* Signal Strength Distribution
* Coverage Analysis
* Dead Zone Detection
* Access Point Placement Optimization

## Future Improvements

* Multi-Node Signal Mapping
* Real-Time Web Dashboard
* GPS-Based Outdoor Mapping
* Machine Learning-Based Localization
* Automated Coverage Optimization
* Multi-Access Point Analysis
* Mobile Application Integration

## Project Structure

```text
WiFi-RSSI-Heatmap-System/
│
├── Arduino_Code/
│   ├── wifi_scanner.ino
│
├── Data/
│   ├── rssi_logs.csv
│
├── Firebase/
│   ├── upload_module.py
│
├── Heatmap/
│   ├── heatmap_generator.py
│
├── Results/
│   ├── coverage_maps/
│
└── README.md
```

## Author

**P. Keerthi Reddy**

Electronics and Communication Engineering
Chaitanya Bharathi Institute of Technology (CBIT)

Areas of Interest:

* Embedded Systems
* Wireless Localization
* IoT Systems
* Signal Processing
* Intelligent Navigation Technologies

## License

This project is licensed under the MIT License.
