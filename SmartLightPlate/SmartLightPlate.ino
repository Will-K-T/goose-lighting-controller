int plateStatePin = 8;
int prevState;

void setup() {
  pinMode(plateStatePin, INPUT);
  prevState = LOW;
  Serial.begin(9600);
}

void loop() {
  int result = digitalRead(plateStatePin);

  if (result != prevState){
    if (result == HIGH){
      // Lights should come on
      Serial.println("Button switched to on!");
    }
    else {
      // Lights should come off
      Serial.println("Button switched to off!");
    }

    prevState = result;
  }
}
