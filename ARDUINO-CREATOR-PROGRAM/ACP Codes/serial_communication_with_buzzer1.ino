void setup()
{
  Serial.begin(9600);
  pinMode(4,OUTPUT);
}

void loop()
{
  if (Serial.available()){
    char buz = Serial.read();
    if (buz == '1') {
      digitalWrite(4,HIGH);
    }
    	if (buz == '0'){
      		digitalWrite(4,LOW);
        }
        }
    	
}