#include <Arduino.h>

//**************************
//  LAN definitions
//**************************

#include <ESP8266WiFi.h>
#include <WebSocketsClient.h>
WebSocketsClient client;

// Remember to add the SSID/PASS
const char* ssid     = "kim";
const char* password = "katarzynkatereska15";

void setup() {
    Serial.begin(115200);

    // Init LAN
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        delay(250);
    }

    Serial.print("LAN OK - IP:");
    Serial.println(WiFi.localIP());
    client.begin("192.168.2.102", 7777);
    client.onEvent([](WStype_t type, uint8_t* payload, size_t length) {
        switch(type) {
            case WStype_DISCONNECTED:
                Serial.println("[WSc] Rozłączono!\n");
                break;
            case WStype_CONNECTED:
                Serial.printf("[WSc] Podłączono do: %s\n",  payload);
                break;
            case WStype_TEXT:
                Serial.printf("[WSc] Odebrane dane: %s\n", payload);
                // Tutaj możesz dodać jakieś akcje dla odebranych dane...
                break;
        }
    });
}

void loop() {
    client.loop();
}