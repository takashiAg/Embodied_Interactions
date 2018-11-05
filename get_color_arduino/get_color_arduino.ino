#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut 8

int whiteR = 180;
int whiteG = 240;
int whiteB = 170;
int blackR = 20;
int blackG = 20;
int blackB = 16;

void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
  Serial.begin(9600);
}

void loop() {
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  int r = pulseIn(sensorOut, LOW);
  delay(100); 

  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  int g = pulseIn(sensorOut, LOW);
  delay(100);
  
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  int b = pulseIn(sensorOut, LOW);
  delay(100);
  
  r = constrain(map(r, whiteR, blackR,0,255),0,255);
  g = constrain(map(g, whiteG, blackG,0,255),0,255);
  b = constrain(map(b, whiteB, blackB,0,255),0,255);

  Serial.println(String(r) + "," + String(g) + "," + String(b) );
}
