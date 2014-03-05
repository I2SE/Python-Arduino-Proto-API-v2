
#ifndef SERIAL_RATE
#define SERIAL_RATE         115200
#endif

#ifndef SERIAL_TIMEOUT
#define SERIAL_TIMEOUT      5
#endif

#include <EEPROM.h>

void configure_pins(){
    char count = readData();
    for (int i = 0; i < count; i++) {
        pinMode(readData(), OUTPUT);
    } 
}

void setup() {
    Serial.begin(SERIAL_RATE);
    Serial.setTimeout(SERIAL_TIMEOUT);
}

void loop() {
    switch (readData()) {
        case 0 :
            //set digital low
            digitalWrite(readData(), LOW); break;
        case 1 :
            //set digital high
            digitalWrite(readData(), HIGH); break;
        case 2 :
            //get digital value
            Serial.println(digitalRead(readData())); break;
        case 3 :
            // set analog value
            analogWrite(readData(), readData()); break;
        case 4 :
            //read analog value
            Serial.println(analogRead(readData())); break;
        case 97:
            //read identifier
            Serial.println(EEPROM.read(0)); break;
        case 98:
            //set identifier
            EEPROM.write(0, readData()); break;
        case 99:
            //configure the i/o pins
            configure_pins();
            break;
        case 100:
            break;
    }
}

char readData() {
    Serial.println("w");
    while(1) {
        if(Serial.available() > 0) {
            return Serial.parseInt();
        }
    }
}
