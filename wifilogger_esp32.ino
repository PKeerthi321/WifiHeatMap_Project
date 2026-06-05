#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(1000);
}

void loop() {

  int n = WiFi.scanNetworks();

  Serial.println("START");

  for (int i = 0; i < n; i++) {
    Serial.print(WiFi.SSID(i));
    Serial.print(",");
    Serial.println(WiFi.RSSI(i));
  }

  Serial.println("END");

  delay(2000); // faster updates
}