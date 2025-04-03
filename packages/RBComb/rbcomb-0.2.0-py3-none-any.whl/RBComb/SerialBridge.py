import serial as serial;
import numpy as np;

class SerialBridge:
    def __init__(self, serialPort, alwaysOpen=False, baudRate=5000000):
        self.serialPort = serialPort;
        self.alwaysOpen = alwaysOpen;
        self.baudRate = baudRate
        if self.alwaysOpen:
            self.serialHandle = serial.Serial(self.serialPort, self.baudRate, bytesize=8, stopbits=2, timeout=500);
        
    def sendArray(self, transferBuffer):
        if not self.alwaysOpen:
            self.serialHandle = serial.Serial(self.serialPort, self.baudRate, bytesize=8, stopbits=2, timeout=1);
            self.serialHandle.reset_input_buffer();
        self.serialHandle.write(transferBuffer.astype('ubyte'));
        if not self.alwaysOpen:
            self.closeConnection();
    
    def getData(self, length):
        return self.serialHandle.read(length);
    
    def flushInput(self):
        self.serialHandle.reset_input_buffer();
        
    def _internal_sendCommand(self, command):
        transferBuffer = np.arange(0,1, dtype='uint8')
        transferBuffer[0] = 192 + command;
        self.sendArray(transferBuffer); 
        
    def _internal_setDataBuff(self, dataToFill):
        transferBuffer = np.arange(0,3, dtype='uint8')
         # Set the 6 lsb's of the "Data" register 
        transferBuffer[0] = (dataToFill % 64);
        
        # Set the bits 11 to 6 of the "Data" register
        dataToFill = int(dataToFill / 64);
        transferBuffer[1] = 64 + (dataToFill % 64);
        
        # Set the bits 17 to 12 of the "Data" register
        dataToFill = int(dataToFill / 64);
        transferBuffer[2] = 128 + (dataToFill % 64);
        self.sendArray(transferBuffer); 
        
    def _internal_setNX_SINGEN_REG(self, dataToFill):
        # Set lower 12 bits
        self._internal_setDataBuff(dataToFill % (2**18))
        self._internal_sendCommand(22);
        # Set upper 12 bits
        self._internal_setDataBuff(int(dataToFill/(2**18)) % (2**18))
        self._internal_sendCommand(23); 
    
    def _internal_setBraidingMemoryAddress(self, braidingAddress):
        self._internal_setDataBuff(braidingAddress);
        self._internal_sendCommand(20);
        
    def selectBoard(self, boardID):
        data = np.arange(0,1, dtype='uint8')
        data[0] = boardID + 224;
        self.sendArray(data); 
    
    def selectAllBoards(self):
        self.selectBoard(15);
        
    def selectLaser(self):
        self.selectBoard(14);

    def closeConnection(self):
        self.serialHandle.close();

    def enableClock(self):
        self._internal_sendCommand(26);
        
    def disableClock(self):
        self._internal_sendCommand(27);