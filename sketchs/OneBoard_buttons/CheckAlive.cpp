#include <Arduino.h>

#include "packets.h"

class CheckAlive {
  private:
    static unsigned long last_time;
  public:
    static void check(){
      if (millis() - last_time > 500) {
        last_time = millis();
        Packets::sendPacket("000000");
      }
    }
};
