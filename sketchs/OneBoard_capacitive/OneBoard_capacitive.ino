//String START_BIT = " ";
//String STOP_BIT = "#";

#include <CapacitiveSensor.h>

#define SAMPLING 100
#define BTN_NUMBER 8
#define RANGE 250

CapacitiveSensor b0 = CapacitiveSensor(A1,A2);   // send and receive pin
CapacitiveSensor b1 = CapacitiveSensor(12,13);
CapacitiveSensor b2 = CapacitiveSensor(10,11);
CapacitiveSensor b3 = CapacitiveSensor(2,3);
CapacitiveSensor b4 = CapacitiveSensor(4,5);
CapacitiveSensor b5 = CapacitiveSensor(6,7);
CapacitiveSensor toggle = CapacitiveSensor(8,9);
CapacitiveSensor pause = CapacitiveSensor(A4,A5);

CapacitiveSensor buttons[BTN_NUMBER] = {b0,b1,b2,b3,b4,b5,pause,toggle};

#include "packets.h"
#include "CheckAlive.cpp"


void setup() {
  b0.set_CS_AutocaL_Millis(0xFFFFFFFF);
  b1.set_CS_AutocaL_Millis(0xFFFFFFFF);
  b2.set_CS_AutocaL_Millis(0xFFFFFFFF);
  b3.set_CS_AutocaL_Millis(0xFFFFFFFF);
  b4.set_CS_AutocaL_Millis(0xFFFFFFFF);
  b5.set_CS_AutocaL_Millis(0xFFFFFFFF);
  pause.set_CS_AutocaL_Millis(0xFFFFFFFF);
  toggle.set_CS_AutocaL_Millis(0xFFFFFFFF);
  Serial.begin(9600);
}

unsigned long CheckAlive::last_time = millis();

void loop() {
  wait();
  long result = 0;
  for(int i = 0; i < BTN_NUMBER; i++){
    result = buttons[i].capacitiveSensor(SAMPLING);
    if(result > 100){
      if(i == 6){
        Packets::sendPacket("pause0");
      } else if(i == 7){
        Packets::sendPacket("toggle");
      } else {
        char buffer[6];
        sprintf(buffer, "btnb%02d", i);
        Packets::sendPacket((String)buffer);
      }
      

        while(buttons[i].capacitiveSensor(SAMPLING) > RANGE){
          wait();
        }
        for(int j = 0; j < 3; j++){
          delay(100);
          wait();err
        }
        buttons[i].reset_CS_AutoCal();
    }
  }
}



void wait(){
  CheckAlive::check();
}
