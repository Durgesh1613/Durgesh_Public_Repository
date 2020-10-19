void setup()
{
pinMode(2,INPUT);
pinMode(3,OUTPUT);
  
digitalWrite(2,HIGH);  
}

void loop()
{
digitalWrite(3,!(digitalRead(2)));
}
