CON

  _clkmode = xtal1 + pll16x
  _xinfreq = 5_000_000

  MAX_SPEED = 1700
  MIN_SPEED = 1300
 
    COMMAND_BASE = 2000

    COMMAND_STOP                  = COMMAND_BASE + 0
    COMMAND_FORWARD               = COMMAND_BASE + 1
    COMMAND_LEFT                  = COMMAND_BASE + 2
    COMMAND_RIGHT                 = COMMAND_BASE + 3

    COMMAND_PING                  = COMMAND_BASE + 10                        

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

  repeat
    rx := Serial.getDec
    if rx == COMMAND_STOP
      PWM.set(0, 1500)
      PWM.set(1, 1500)
      Serial.str(String("ACK", 13))

    elseif rx == COMMAND_FORWARD    
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED
      PWM.set(0, rx)
      PWM.set(1, rx)
      Serial.str(String("ACK", 13))
      
    elseif rx == COMMAND_LEFT
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED 
      PWM.set(0, rx)
      Serial.str(String("ACK", 13))
      
    elseif rx == COMMAND_RIGHT
      rx := MIN_SPEED #> Serial.getDec <# MAX_SPEED
      PWM.set(1, rx)
      Serial.str(String("ACK", 13))

    elseif rx == COMMAND_PING
      Serial.str(String("ACK", 13))
          
    else
      Serial.str(String("NACK", 13))