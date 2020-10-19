void setup()
{
pinMode(A0,INPUT);
pinMode(5,OUTPUT);
Serial.begin(9600);  
}

void loop()
{
 int ldr = analogRead(A0);
  if (ldr > 500){
    digitalWrite(5,HIGH);
  }
  else{
    digitalWrite(5,LOW);
  }
  Serial.println(analogRead(A0));
}