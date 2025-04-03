import numpy as np;

class FunctionInterpolator:
    def __init__(self):
        self.yScaling = (2**17-1);
        self.fpgaDependentRange = np.arange(-(2**17),(2**17),64, dtype='float');
        self.functionDependentRange = np.arange(0,0.25*0.25,64.0*0.25*0.25/(2**18));
        self.divRatio = 2**18;
        self.interpolationMatrix = ((np.array((np.transpose(np.array([
                ((self.fpgaDependentRange**0)), 
                ((self.fpgaDependentRange**1)/(self.divRatio**1)), 
                ((self.fpgaDependentRange**2)/(self.divRatio**2)), 
                ((self.fpgaDependentRange**3)/(self.divRatio**3)), 
                ((self.fpgaDependentRange**4)/(self.divRatio**4)), 
                ((self.fpgaDependentRange**5)/(self.divRatio**5))]))), dtype='float')))/self.yScaling;
        
    # Here we must add safety to check that there are no overflows:
    # 1. In the parameters
    # 2. In the final results
    # 3. In the intermediate calculations
    def performInterpolation(self, function):
        result = np.zeros((6,16), dtype='float');
        for ind in range(16):
            result[:,ind] =  np.round(np.linalg.lstsq(self.interpolationMatrix, 
                                             function(float(ind)*0.25*0.25+self.functionDependentRange), rcond=None)[0]);
        return np.array(result,dtype='int');
    
    # Here we check for overflows in intermediate and final results
    def performPartialValidation(self, interpolationResults, part):
        result = np.zeros(len(self.fpgaDependentRange));
        coefficients = interpolationResults[:,part];
        for i in range(6):
            result = result*self.fpgaDependentRange;
            result = np.array(result/self.divRatio, dtype = 'int');
            result = result + coefficients[len(coefficients)-i-1];
        return result;
    
    def performValidation(self, interpolationResults):
        for i in range(16):
            if i == 0:
                p1 = self.performPartialValidation(interpolationResults,i);
            else:
                p1 = np.append(p1, self.performPartialValidation(interpolationResults,i));
        return p1;
    
    def getXRange(self):
        return np.arange(0,1.0,64*0.25*0.25/(2**18));
    
    def getConstantFunction(self, offsetValue):
        func = lambda x: (offsetValue+np.zeros(np.shape(x),dtype='float'));
        return self.performInterpolation(func);
        