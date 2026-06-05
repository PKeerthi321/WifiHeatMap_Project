from flask import Flask, jsonify, render_template
import serial
import threading
import numpy as np
import time

app = Flask(__name__)

PORT = 'COM5'
BAUD = 115200
GRID_SIZE = 10

heatmap = np.full((GRID_SIZE, GRID_SIZE), -100)

x, y = 0, 0

def read_serial():
    global x, y

    # connect safely
    while True:
        try:
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print(f"✅ Connected to {PORT}")
            break
        except:
            print("Waiting for ESP32...")
            time.sleep(2)

    best_rssi = -100

    while True:
        try:
            line = ser.readline().decode(errors='ignore').strip()

            if not line:
                continue

            print("RAW:", line)

            if line == "START":
                best_rssi = -100

            elif line == "END":
                heatmap[y][x] = best_rssi

                x = (x + 1) % GRID_SIZE
                if x == 0:
                    y = (y + 1) % GRID_SIZE

            elif "," in line:
                ssid, rssi = line.split(",")
                rssi = int(rssi)

                if rssi > best_rssi:
                    best_rssi = rssi

        except Exception as e:
            print("Error:", e)

# start thread
threading.Thread(target=read_serial, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(heatmap.tolist())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

