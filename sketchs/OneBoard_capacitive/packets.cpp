#include <Arduino.h>

#include "packets.h"

#define START_BIT " "
#define STOP_BIT "#"


void Packets::sendPacket(const String& data)
{
  String message = START_BIT + data + STOP_BIT;
    if(data.length()!= 6) {
      message = (String)START_BIT + "err001" + (String)STOP_BIT;   // Error: trying to send more than 4 bytes data
    }
    Serial.print(message);
}



//#define START_BIT " "
//#define STOP_BIT "#"
