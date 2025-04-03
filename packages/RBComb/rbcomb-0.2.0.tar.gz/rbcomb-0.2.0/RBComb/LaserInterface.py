import numpy as np;
class LaserInterface:
    def __init__(self, bridgeLink):
        self.bridgeLink = bridgeLink;
        self.multvec = np.array([1, 2**8, 2**16, 2**24, 2*32, 2**40]);
        
    def _internal_vectToScalar(self, data):
        cumsum = 0;
        for i in range(6):
            cumsum = cumsum*256 + data[5-i];
        return cumsum;
    
    def _internal_numericalResponseCommand(self, command):
        self.bridgeLink._internal_sendCommand(command);
        data = self.bridgeLink.getData(6);
        if len(data) < 6:
            print('Insufficient data received. Check that the laser is selected.');
            return 0;
        return self._internal_vectToScalar(data);
    
    def requestDisplacement(self, axis):
        if axis < 0 or axis > 3:
            print('Axis must be 1, 2 or 3');
            return 0;
        return self._internal_numericalResponseCommand(53 + axis);

    #DEPRECATED
    def scheduleAcquisition(self, axis, delay):
        if axis < 0 or axis > 3:
            print('Axis must be 1, 2 or 3');
            return 0;
        self.bridgeLink._internal_setNX_SINGEN_REG(delay+((2**30)*(axis-1)));
        self.bridgeLink._internal_sendCommand(57);

    #DEPRECATED    
    def requestTimeTrace(self):
        result = np.zeros((2**15,2), dtype='float');
        self.bridgeLink.flushInput()
        self.bridgeLink._internal_setNX_SINGEN_REG(2**15+2**31);
        self.bridgeLink._internal_sendCommand(61)
        self.bridgeLink._internal_setNX_SINGEN_REG(0);
        self.bridgeLink._internal_sendCommand(58);
        buff =  self.bridgeLink.getData((2**15)*6);
        self.bridgeLink._internal_setNX_SINGEN_REG(2**16);
        self.bridgeLink._internal_sendCommand(61)
        buff +=  self.bridgeLink.getData((2**15)*6);
        currentTime = 0;
        for i in range(2**15):
            currentIndex = i*12;
            disp = self._internal_vectToScalar(buff[currentIndex:(currentIndex+6)]);
            deltaT = self._internal_vectToScalar(buff[(currentIndex+6):(currentIndex+12)]);
            currentTime += deltaT;
            result[i,0] = currentTime;
            result[i,1] = disp;
        return result;

    #Carli time trace request
    def requestTimeTraceCarli(self):
        result = np.zeros((self.length,2), dtype='float')
        #request data
        self.bridgeLink._internal_setNX_SINGEN_REG(0)
        self.bridgeLink._internal_sendCommand(58)
        #get data
        buff = self.bridgeLink.getData((self.length)*12)
        print(f'requested: {self.length}, gotten: {int(len(buff)/12)}')
        print(len(buff))
        if self.length != int(len(buff)/12):
            print("Communication failure")
            return None
        #process data
        currentTime = 0
        for i in range(int(self.length)):
            if i % 100000 == 0:
                print(i)
            currentIndex = i*12
            disp = self._internal_vectToScalar(buff[currentIndex:(currentIndex+6)])
            deltaT = self._internal_vectToScalar(buff[(currentIndex+6):(currentIndex+12)])
            currentTime += deltaT
            result[i,0] = currentTime
            result[i,1] = disp
        return result

    #Carli acquisition schedule
    def scheduleAcquisitionCarli(self, axis, delay, length=2**16):
        #set length of acquisition
        self.length = length
        self.bridgeLink.flushInput()
        self.bridgeLink._internal_setNX_SINGEN_REG(length+2**31)
        self.bridgeLink._internal_sendCommand(61)
        #schedule acquisition
        if axis < 0 or axis > 3:
            print("Axis must be 1, 2 or 3")
            return 0;
        self.bridgeLink._internal_setNX_SINGEN_REG(delay+((2**30)*(axis-1)))
        self.bridgeLink._internal_sendCommand(57)

    #OUT OF ORDER
    def isAcquisitionFinished(self):
        return self._internal_numericalResponseCommand(60) == 32768;
        
    def requestTimeSinceMeasurementEnded(self):
        return self._internal_numericalResponseCommand(59);
        
