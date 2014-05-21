CON

  _clkmode = xtal1 + pll16x
  _xinfreq = 5_000_000

  MAX_SPEED = 1700
  MIN_SPEED = 1300 

OBJ

  Serial:       "FullDuplexSerial"
  PWM   :       "Servo32v7"

PUB Main | rx

  waitcnt(clkfreq*2+cnt)
  Serial.start(31, 30, 0, 9600)
  Serial.str(String("Beaker Started", 13))

  PWM.start
  PWM.set(0, 1500)
  PWM.set(1, 1500)

  '2046 == Left
  '2047 == Right
  repeat
    rx := Serial.getDec
    if rx == 2044 'BOTH STOP
      PWM.set(0, 1500)
      PWM.set(1, 1500)
      Serial.str(String("ACK", 13))
    elseif rx == 2045 'BOTH FORWARD
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED
      PWM.set(0, rx)
      PWM.set(1, rx)
      Serial.str(String("ACK", 13))
    if rx == 2046
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED 
      PWM.set(0, rx)
      Serial.str(String("ACK", 13))
    elseif rx == 2047
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED
      PWM.set(1, rx)
      Serial.str(String("ACK", 13))
    else
      Serial.str(String("NACK", 13))
