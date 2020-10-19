void setup()
{
  Serial.begin(9600);
  pinMode(4,OUTPUT);
  pinMode(8,OUTPUT);
}

void loop()
{
  if (Serial.available()){
    char buz = Serial.read();
    if (buz == '1') {
      digitalWrite(4,HIGH);
      digitalWrite(8,HIGH);
      Serial.println("BUZZER AND LED IS ON");
    }
    	if (buz == '0'){
      		digitalWrite(4,LOW);
            digitalWrite(8,LOW);
            Serial.println("BUZZER AND LED IS OFF");
        }
    		if (buz == '2'){
            	Serial.println("BUZZER IS BLINKING LIKE A BULB");
                digitalWrite(4,HIGH);
                Serial.println("BUZZER IS ON");
                delay(1000);
                digitalWrite(4,LOW); 
                Serial.println("BUZZER IS OFF");
                delay(1000);
                digitalWrite(4,HIGH);
                Serial.println("BUZZER IS ON");
                delay(1000);
                digitalWrite(4,LOW); 
                Serial.println("BUZZER IS OFF");
                delay(1000);
                digitalWrite(4,HIGH);
                Serial.println("BUZZER IS ON");
                delay(1000);
                digitalWrite(4,LOW); 
                Serial.println("BUZZER IS OFF");
                delay(1000);
            }
            }
    	
}