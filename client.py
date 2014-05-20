import pygame, socket

HOST = ("192.168.52.3", 80)

MAX_SPEED = 400
PULSE_MIDDLE = 1500

class Application:
    def __init__(self):
        self.running = False
        self.surface = None
        self.joystick = None
        
        self.joy_pos = (0, 0)
        self.speeds = (0, 0)

    def start(self):
        pygame.init()

        #Initialize screen
        self.surface = pygame.display.set_mode((120, 50))

        self.joystick = pygame.joystick.Joystick(0)
        print "Joystick:", self.joystick.get_name()
        self.joystick.init()

        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect(HOST)
        
        self.running = True
        self.loop()

    def stop(self):
        self.running = False

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            elif event.type == pygame.JOYAXISMOTION:
                if event.value > 1 or event.value < -1:
                    continue

                if event.axis == 1:
                    self.joy_pos = self.joy_pos[0], -float("{0:.2f}".format(event.value))
                elif event.axis == 0:
                    self.joy_pos = float("{0:.2f}".format(event.value)), self.joy_pos[1]

                self.calculateSpeeds()

    def calculateSpeeds(self):
        left = MAX_SPEED*self.joy_pos[1]
        right = left

        if self.joy_pos[0] < 0:
            left = left - (right*abs(self.joy_pos[0]))*2
        else:
            right = right - (left*abs(self.joy_pos[0]))*2
        
        self.speeds = left, right

    def loop(self):
        #While the running flag is true...
        while self.running:
            self.surface.fill((0,0,0))

            self.handleEvents()

            pygame.display.flip()

        #When the running flag is set to false, quit loop and shutdown everything!            
        pygame.quit()
        quit()

if __name__ == "__main__":
    app = Application()
    app.start()
