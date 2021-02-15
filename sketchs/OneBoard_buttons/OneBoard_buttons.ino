/*
 * This code is made to connect arduino to OneBoard software.
 * Replace BTN_NUMBER with the number of buttons you created and 
 * button_pins with the button pins. 
 * 
 * Change the PAUSE condition to true if you want to implement the pause button
 * and note that the last pin of button_pins array will became the pause button.
 */

#define BTN_NUMBER 9
byte button_pins[BTN_NUMBER] = {2,3,4,5,6,7,8,9,10};
#define PAUSE false



#include "packets.h"
#include "CheckAlive.cpp"


void setup() {
  Serial.begin(9600);

  //write your setup here
}

unsigned long CheckAlive::last_time = millis();
bool result = false;

void loop() {
  CheckAlive::check();
  for(int i = 0; i < BTN_NUMBER; i++){
    result = digitalRead(button_pins[i]);
    if(result){
      delay(100);   // debounce
      #if PAUSE
        if(i == BTN_NUMBER - 1){
          Packets::sendPacket("pause0");
        } else {
          char buffer[6];
          sprintf(buffer, "btnb%02d", i);
          Packets::sendPacket((String)buffer);
        }
      #else
        char buffer[6];
        sprintf(buffer, "btnb%02d", i);
        Packets::sendPacket((String)buffer);
      #endif
      
      

        while(digitalRead(button_pins[i])){
          CheckAlive::check();
        }
        delay(100);     // debounce
    }
  }
}
