import socket, serial

PORT = ""

class Application:
    def __init__(self):
        self.running = False

        self.buffer = ""
        self.hasPacketStarted = None
        self.commands = ["SHUTDOWN", "HELP"]

        self.conn = None

    def start(self):
        self.running = True

        self.serial = serial.Serial(PORT)
        print "Connected to serial port:", self.serial.name
        ser.write(

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", 1997))
        self.socket.listen(1)
        print "Running server on:", ("0.0.0.0", 1997)

        self.loop()

    def stop(self):
        self.running = False

    def processByte(self, byte):
        if byte == "[" and not self.hasPacketStarted:
            self.hasPacketStarted = True
        elif byte == "]" and self.hasPacketStarted:
            self.hasPacketStarted = False
            self.onPacketRecieved(self.buffer)
            self.buffer = ""
        elif self.hasPacketStarted:
            self.buffer = self.buffer + byte

    def onPacketRecieved(self, packet):
        print "Packet Recieved:", packet
        
        cmd = packet.split(" ")[0]
        params = packet.split(" ")
        del params[0]
        
        if not cmd in self.commands:
            self.conn.send("NACK\n")
            return

        if cmd == "SHUTDOWN":
            self.stop()
            self.conn.send("ACK\n")
        elif cmd == "HELP":
            self.conn.send("COMMANDS:\n")
            for command in self.commands:
                self.conn.send(" - "+command+"\n")
            self.conn.send("ACK\n")

    def loop(self):
        self.conn, addr = self.socket.accept()
        self.conn.send("ACK\n")
        print "Connection from: ", addr
        buff = []
        while self.running:
            self.processByte(self.conn.recv(1))
            
        self.conn.close()
        quit()

if __name__ == "__main__":
    app = Application()
    app.start()
