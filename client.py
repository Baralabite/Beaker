import pygame, socket

HOST = ("192.168.52.3", 80)

class Application:
    def __init__(self):
        self.running = False
        self.surface = None
        self.joystick = None

    def start(self):
        pygame.init()

        #Initialize screen
        self.surface = pygame.display.set_mode((120, 50))

        self.joystick = pygame.joystick.Joystick(0)
        print "Joystick:", self.joystick.get_name()
        self.joystick.init()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(HOST)
        
        self.running = True
        self.loop()

    def stop(self):
        self.running = False

    def handleEvents(self):
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                self.stop()                

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
