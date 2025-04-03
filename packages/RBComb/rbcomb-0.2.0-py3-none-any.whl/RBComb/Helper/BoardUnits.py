import numpy as np;

class BoardUnits:
    def __init__(self, masterClock= 100.0e6, clockDivider = 713.0):
        self.boardMasterClock = masterClock;
        self.clockDivider = clockDivider;
        self.sampleRate = self.boardMasterClock/self.clockDivider;
        
    def convertFrequencyIntegerToHz(self, integerFrequency):
        return integerFrequency*float(self.sampleRate)/float(2**32);

    def convertFrequencyHzToInteger(self, hzFrequency):
        return int(np.round(hzFrequency*float(2**32)/float(self.sampleRate)));
    
    def convertTimeToSteps(self, time):
        return int(np.round(time*float(self.sampleRate)));
    
    def convertFrequencyRangeToSweepSpeed(self, frequencyStart, frequencyEnd, sweepDuration):
        return int(np.round((frequencyEnd - frequencyStart)*float(2**32)/((float(self.sampleRate)**2)*sweepDuration)));

    def convertDegreesPhaseToInteger(self, degreesPhase):
        return int(np.round((2**32)*np.mod(degreesPhase/360.0,1.0)));

    def convertNormalizedAmplitudeToInteger(self, amplitude):
        if amplitude < 0:
            return 1 + int(np.ceil(amplitude*(2**17-1)));
        else:
            return int(np.floor(amplitude*(2**17-1)));

    def convertBraidingDurationToIntegerSpeed(self, braidDuration):
        return int(np.round(float(2**28)/(self.sampleRate*braidDuration)));
    
    def convertIntegerSpeedToBraidDuration(self, integerSpeed):
        return float(2**28)/(self.sampleRate*float(integerSpeed));

