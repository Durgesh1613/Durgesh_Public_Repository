void setup()
{
  pinMode(A0, INPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
    
}

void loop()
{
int pot = analogRead(A0);
int pwm = map(pot,0,1023,0,255);
  analogWrite(5,pwm);
  Serial.println(pwm);
  
}