#include <WiFi.h> // Use the correct library for your module
#include <HTTPClient.h>

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";
const char* serverUrl = "http://your-kestra-server/api/data";

int heartbeatPin = A0; // Example pin for heartbeat sensor
int glucosePin = A1;   // Example pin for glucose sensor

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  int heartbeat = analogRead(heartbeatPin); // Simulate sensor reading
  int glucose = analogRead(glucosePin);     // Simulate sensor reading

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = String("{\"heartbeat\":") + heartbeat + 
                         ",\"glucose\":" + glucose + "}";

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      Serial.println("Data sent successfully");
    } else {
      Serial.print("Error sending data: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("WiFi not connected");
  }

  delay(5000); // Adjust delay as needed
}
