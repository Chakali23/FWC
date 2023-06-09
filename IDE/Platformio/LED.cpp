#include<Arduino.h>

int x,y;
int p = 0,q = 0;
int D1,D2;

void setup()
{
	pinMode(2,INPUT);
	pinMode(3,OUTPUT);
	pinMode(13,OUTPUT);
}
void loop()
{
digitalWrite(13,HIGH);
delay(2000);
	x = digitalRead(2);
	digitalWrite(13,LOW);
	delay(1500);
	D1 = (q&&!x);
	D2 = (x);
	y = (p&&x);

	if(y==1)
	{
		digitalWrite(3,HIGH);
	}
	else
	{
		digitalWrite(3,LOW);
	}
	p = D1;
	q = D2;
}
