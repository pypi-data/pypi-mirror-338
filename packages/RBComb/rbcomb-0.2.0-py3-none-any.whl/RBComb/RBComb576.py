import numpy as np;

class RBComb576:
    def __init__(self, bridgeLink):
        self.bridgeLink = bridgeLink;
        self.bridge2Comps = np.zeros([6,16], dtype='int');
        self.bridge2Comps[:]   = 2**18;
        self.bridge2Comps[4,:] = 2**8;
        self.bridge2Comps[5,:] = 2**6;
        self.braidingOrder = np.array([1]*16,dtype='int');
        for i in range(15):
            self.braidingOrder[i+1] = 2*self.braidingOrder[i];

    def sendDataToAllDACs(self, dataToSend, ldacBubble=False):
        if ldacBubble:
            self.bridgeLink._internal_setNX_SINGEN_REG(dataToSend + 2**24);
        else:
            self.bridgeLink._internal_setNX_SINGEN_REG(dataToSend);   
        self.bridgeLink._internal_sendCommand(25);
        
    def setGain(self, highGain):
        # True means gain of 2, false means gain of 1
        if highGain:
            self.sendDataToAllDACs(2**22 + 2**21 + 2**20 + 2**2);
        else:
            self.sendDataToAllDACs(2**22 + 2**21 + 2**20);

    def outputRampUp(self):
        self.bridgeLink._internal_sendCommand(28);

    def outputRampDown(self):
        self.bridgeLink._internal_sendCommand(29);
    
    def setPhase(self, sineGenerator, newPhase):
        self.bridgeLink._internal_setNX_SINGEN_REG(newPhase);
        self.bridgeLink._internal_sendCommand(0+sineGenerator);
        
    def setFrequency(self, sineGenerator, newFrequency):
        self.bridgeLink._internal_setNX_SINGEN_REG(newFrequency);
        self.bridgeLink._internal_sendCommand(4+sineGenerator);
        
    def setSweepFrequencyStep(self, sineGenerator, newFrequencyStep):
        self.bridgeLink._internal_setNX_SINGEN_REG(newFrequencyStep);
        self.bridgeLink._internal_sendCommand(8+sineGenerator);
        
    def setSweepFrequencyMax(self, sineGenerator, newFrequencyMax):
        self.bridgeLink._internal_setNX_SINGEN_REG(newFrequencyMax);
        self.bridgeLink._internal_sendCommand(16+sineGenerator);
        
    def setBraidingLength(self, newBraidingLength):
        self.bridgeLink._internal_setDataBuff(newBraidingLength);
        self.bridgeLink._internal_sendCommand(52);
        
    def setBraidingFrame(self, newBraidingFrame):
        self.bridgeLink._internal_setNX_SINGEN_REG(newBraidingFrame);
        self.bridgeLink._internal_sendCommand(59);
        
    def setBraidingSpeed(self, newBraidingSpeed):
        self.bridgeLink._internal_setNX_SINGEN_REG(newBraidingSpeed);
        self.bridgeLink._internal_sendCommand(60);
    
    def setBraidingOrder(self, braidingOrder):
        self.bridgeLink._internal_setDataBuff(int(np.sum(braidingOrder*self.braidingOrder[0:len(braidingOrder)])));
        self.bridgeLink._internal_sendCommand(51);

    def setBraidingAB(self, braidingAB):
        self.bridgeLink._internal_setDataBuff(int(np.sum(braidingAB*self.braidingOrder[0:len(braidingAB)])));
        self.bridgeLink._internal_sendCommand(50);

    def setBraidingHold(self, braidingHold):
        self.bridgeLink._internal_setDataBuff(int(np.sum(braidingHold*self.braidingOrder[0:len(braidingHold)])));
        self.bridgeLink._internal_sendCommand(53);
    
    def setCurrentState(self, newState):
        self.bridgeLink._internal_setDataBuff(int(np.sum(newState*self.braidingOrder[0:5])));
        self.bridgeLink._internal_sendCommand(61);
        
    def setNextState(self, newState, delay):
        self.bridgeLink._internal_setNX_SINGEN_REG(delay);
        self.bridgeLink._internal_setDataBuff(int(np.sum(newState*self.braidingOrder[0:5])));
        self.bridgeLink._internal_sendCommand(62);
    
    def setTaylorCoefficients(self, output, BSequence, coeffs):
        # Convert coefficients to two's complement
        coeffs2Comp = np.array(coeffs, dtype = 'int');
        coeffs2Comp[coeffs < 0] +=  self.bridge2Comps[coeffs < 0];
        coeffs2Comp[4,:] = (2**8)*coeffs2Comp[4,:] + coeffs2Comp[5,:];
        for j in range(16):
            braidingAddress = output*32+j;
            if BSequence:
                braidingAddress += 16;
            self.bridgeLink._internal_setBraidingMemoryAddress(braidingAddress)
            # Here we will add the two's complement and coefficient merging functions
            for i in range(5):
                currentCoeff = coeffs2Comp[i,j];
                self.bridgeLink._internal_setDataBuff(currentCoeff);
                self.bridgeLink._internal_sendCommand(58-i);
        
    def setAmplitude(self, sineGenerator, channelNum, targetAmplitude):
        # Conversion to two's complement
        if targetAmplitude < 0:
            targetAmplitude = 262144 + targetAmplitude;
        
        transferBuffer = np.arange(0,7, dtype='uint8')
        
        # Set the 6 lsb's of the "Data" register to the 5 lsbs of the channel num
        transferBuffer[0] = (channelNum % 64);
        
        # Set the bits 11 to 6 of the "Data" register to the bits 11-6 of the channel num
        channelNum = int(channelNum / 64);
        transferBuffer[1] = 64 + (channelNum % 64);
        
        # Transfer the 9 lsb's of the data register into the address register
        transferBuffer[2] = 192 + 20;
        
        # Set the 6 lsb's of the "Data" register to the 5 lsbs of the amplitude num
        transferBuffer[3] = (targetAmplitude % 64);
        
        # Set the bits 11 to 6 of the "Data" register to the bits 11-6 of the amplitude 
        targetAmplitude = int(targetAmplitude / 64);
        transferBuffer[4] = 64 + (targetAmplitude % 64);
        
        # Set the bits 17 to 12 of the "Data" register to the bits 17-12 of the amplitude 
        targetAmplitude = int(targetAmplitude / 64);
        transferBuffer[5] = 128 + (targetAmplitude % 64);
        
        # Perform memory write-up
        transferBuffer[6] = 192 + 12 + sineGenerator;
        
        # Send it to the board
        self.bridgeLink.sendArray(transferBuffer); 