#include "packets.h"
#include "CheckAlive.cpp"


void setup() {
  Serial.begin(9600);

  //write your setup here
}

unsigned long CheckAlive::last_time = millis();

void loop() {
  CheckAlive::check();

  //write your loop here
}
