void setup()
{
  pinMode(10, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  for (int i=0;i<=255;i++){
  analogWrite(10,i);
  analogWrite(3,i);
    delay(30);
}
analogWrite(10,0);
analogWrite(3,0);  
  delay(30);

}