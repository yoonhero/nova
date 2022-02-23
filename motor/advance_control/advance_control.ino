#include <Stepper.h>
#include <Servo.h>

//////////////////////////// STRUCTURE ////////////////////////////////
struct leftOrRightCondition
{
  bool left;
  bool right;
};

struct goOrbackCondition
{
  bool forward;
  bool backward;
};


//////////////////////////// CLASSES ////////////////////////////////
class Led
{
private:
  byte pin;

public:
  Led(byte pin)
  {
    this->pin = pin;
    init();
  }

  void init()
  {
    pinMode(pin, OUTPUT);

    off();
  }

  void on()
  {
    digitalWrite(pin, HIGH);
  }

  void off()
  {
    digitalWrite(pin, LOW);
  }
};


//class MyServo{
//  private:
//    int pin;
//    int angle;
//    Servo servo;
//
//  public:
//    MyServo(int servoPin){
//      this->pin = servoPin;
//
//      init();
//    }
//
//    void init(){
//      servo.attach(pin);
//    }
//
//    void turn(){
//      angle += 30;
//      if (angle == 210){
//        angle = 0;
//      } 
//      servo.write(angle);
//      
//    }
//};

//////////////////////////// DECLATION OF FUNCTION ////////////////////////////////

// get distance from sensor (cm float)
float recognizeDistance();

// manipulation system

struct leftOrRightCondition leftOrRight();
struct goOrbackCondition goOrback();

// Servo

void servoInit();
void servoTurn(int angle);


//////////////////////////// VARIABLES ////////////////////////////////
int joyStickPin = 7;

int echoPin = 12;
int trigPin = 13;


Led goSign(6);
Led stopSign(5);
Led backSign(4);

Servo servo;
int servoPin = 3;


//////////////////////////// SETUP ////////////////////////////////
void setup()
{
  Serial.begin(9600);

  pinMode(joyStickPin, INPUT_PULLUP);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  servo.attach(servoPin);
  servoInit();
}




//////////////////////////// LOOP ////////////////////////////////
void loop()
{

  

  struct goOrbackCondition fbCon;
  struct leftOrRightCondition lrCon;

  fbCon = goOrback();
  lrCon = leftOrRight();

  goSign.off();
  stopSign.off();
  backSign.off();

  if (fbCon.forward)
  {
    goSign.on();
  }
  else if (fbCon.backward)
  {
    backSign.on();
  }
  else
  {
    stopSign.on();
  }

  if (lrCon.left){
    servoTurn(135);
  } else if(lrCon.right){
    servoTurn(45);
  } else {
    servoTurn(90);
  }

  delay(1000);
}


//////////////////////////// FUNCTIONS ////////////////////////////////

void servoInit(){
  servoTurn(90);
}

void servoTurn(int angle){
  servo.write(angle);
}

float recognizeDistance()
{
  digitalWrite(trigPin, LOW);
  digitalWrite(echoPin, LOW);

  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);

  delayMicroseconds(2);

  digitalWrite(trigPin, LOW);

  // echo Pin 이 HIGH 를 유지한 시간을 저장한다.
  unsigned long duration = pulseIn(echoPin, HIGH);

  float distance = ((float)(340 * duration) / 10000) / 2;

  return distance;
}

float getJoystickVal(int analogPin)
{
  // get y axis value
  float analog_value = analogRead(analogPin);

  return analog_value;
}

// return (Forward Condition, Backward Condition)
struct goOrbackCondition goOrback()
{
  float y_axis_value = getJoystickVal(0);

  struct goOrbackCondition con;

  con.forward = false;
  con.backward = false;

  if (y_axis_value > 800)
  {

    float dis = recognizeDistance();
    if (dis < 10)
    {
      Serial.println("stop!!!!!");
      return con;
    }

    // go forward
    Serial.println("GO forward!!");
    con.forward = true;
  }
  else if (y_axis_value < 300)
  {

    // go backward
    Serial.println("GO Back!!");
    con.backward = true;
  }
  else
  {

    // stop
    Serial.println("STOP!!");
  }

  return con;
}

// return (left condition, right condition)
struct leftOrRightCondition leftOrRight()
{
  float x_axis_value = getJoystickVal(1);

  struct leftOrRightCondition con;

  con.left = false;
  con.right = false;

  if (x_axis_value > 800)
  {

    // right turn
    Serial.println("Go Right");
    con.right = true;
  }
  else if (x_axis_value < 300)
  {

    // left turn
    Serial.println("Go Left");
    con.left = true;
  }
  else
  {
    // stop
    Serial.println("STOP!!!");
  }

  return con;
}

//
//class FBMotor {
//  private:
//    byte pin;
//    byte state;
//    byte delayTime;
//    int stepsPerRev = 2048;
//    int stepperPins[4] = {11, 9, 10, 8};
//    Stepper stepper(stepsPerRev, stepperPins[0], stepperPins[1], stepperPins[2], stepperPins[3]);
//
//  public:
//    FBMotor(byte pin){
//      this->pin = pin;
//      init();
//    }
//
//    void init(){
//      pinMode(pin, INPUT);
//
//      stepper.setSpeed(10);
//    }
//
//    void forward(){
//      stepper.step(stepsPerRev);
//      delay(1000);
//    }
//
//    void back(){
//      stepper.step(-stepsPerRev);
//      delay(1000);
//    }
//};
