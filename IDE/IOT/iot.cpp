#include<WiFi.h>
#include<WiFiUdp.h>
#include<ArduinoOTA.h>

#ifndef STASSID
#define STASSID "suresh"
#define STAPSK "12345678"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

void OTAsetup()
{
	WiFi.mode(WIFI_STA);
	WiFi.begin(ssid,password);
	while(WiFi.waitForConnectResult() != WL_CONNECTED)
	{
		delay(6000);
		ESP.restart();
	}
	ArduinoOTA.begin();
}

void OTAloop()
{
	ArduinoOTA.handle();
}

int pinB = 2;
int pinF = 13;

void setup()
{
	OTAsetup();

	pinMode(pinB,INPUT);
	pinMode(pinF,OUTPUT);
}

void loop()
{
	OTAloop();

	bool B = digitalRead(pinB);

	bool F = !B;
	digitalWrite(pinF,F);
}
