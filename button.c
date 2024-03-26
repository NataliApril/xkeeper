#include <wiringPi.h>
#include <stdio.h>

#define LED 29
#define BUTTON 27

//using namespace std;

int main() {
	if (wiringPiSetup() == -1) {
		printf ("setup failed!\n");
		return 1;
	}
	pinMode(LED, OUTPUT);
	pinMode(BUTTON, INPUT);
	digitalWrite(LED, HIGH);
	
	/*while (1) {
		digitalWrite(LED, HIGH);
		delay(500);
		digitalWrite(LED, LOW);
		delay(500);
	}*/
	while(1) {
		if (digitalRead(BUTTON) == 0) {
			digitalWrite(LED, LOW);
			printf("LED OFF\n");
		} else {
			digitalWrite(LED, HIGH);
			printf ("LED ON\n");
		}
	}
	return 0;
}
