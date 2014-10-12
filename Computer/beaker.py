import socket, time

"""
Beaker is a shiny frontend for the communications. You can
put in "beaker.moveForward(10)" and it'll change that into
packet ids, etc and send it to the TCP-Serial Bridge, which
in turn forwards anything it gets onto the serial port.
"""

class Commands:
    def __init__(self):
        pass
    
    COMMAND_BASE = 2000

    COMMAND_STOP                  = COMMAND_BASE + 0
    COMMAND_FORWARD               = COMMAND_BASE + 1
    COMMAND_LEFT                  = COMMAND_BASE + 2
    COMMAND_RIGHT                 = COMMAND_BASE + 3

    COMMAND_PING                  = COMMAND_BASE + 10  

class Beaker:
    def __init__(self):
        self.socket = None
        self.recv_buffer = ""
        self.recv_ack = True

    """Connects to the TCP/Serial bridge."""
    def connect(self, host):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.socket.connect(host)
        #self.socket.setblocking(0)

    def disconnect(self):
        self.socket.close()

    """This is the equivalent of an update function"""
    def poll(self):
        pass

    """Sends the raw data"""
    def send(self, raw):
        self.socket.send(str(raw)+"\r")
        self.recv_ack = False

    #=====[Useful Commands!]=====#

    def stopWheels(self):
        self.send(Commands.COMMAND_STOP)
        time.sleep(0.01) #TODO

    def moveWheels(self, speed):
        self.send(Commands.COMMAND_FORWARD)
        self.send(str(speed))
        time.sleep(0.01) #TODO: Replace with "wait until ACK"

    def moveLeftWheel(self, speed):
        self.send(Commands.COMMAND_LEFT)
        self.send(str(speed))
        time.sleep(0.01) #TODO

    def moveRightWheel(self, speed):
        self.send(Commands.COMMAND_RIGHT)
        self.send(str(speed))
        time.sleep(0.01) #TODO
