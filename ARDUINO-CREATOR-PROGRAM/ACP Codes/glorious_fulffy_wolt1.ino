//Echo = Pin 9
// Triggered = Pin 10
void setup()
{
  pinMode(10, OUTPUT);
  pinMode(9, INPUT);
  Serial.begin(9600);
  
}

void loop()
{
  digitalWrite(10,LOW);
  delayMicroseconds(2);
  digitalWrite(10,HIGH);
  delayMicroseconds(10);
  digitalWrite(10,LOW);
  long time = pulseIn (9, HIGH);
  int distance = 0.0343*time/2;
  
  Serial.println(distance);
  delay(100);
}