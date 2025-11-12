void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);  // Red LED
  pinMode(10, OUTPUT); // Green LED
  pinMode(11, OUTPUT); // Blue LED
}

void loop() {
  if (Serial.available() >= 3) {
    int r = Serial.read();
    int g = Serial.read();
    int b = Serial.read();
    
    analogWrite(9, r);
    analogWrite(10, g);
    analogWrite(11, b);
  }
}
