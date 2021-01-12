import time
from Motor import *
from ADC import *
class Light:
    def run(self, reverse=False):
        try:
            self.adc=Adc()
            self.PWM=Motor(reverse=reverse)
            self.PWM.setMotorModel(0,0,0,0)
            while True:
                L = self.adc.recvADC(0)
                R = self.adc.recvADC(1)
                if L < 2.99 and R < 2.99 :
                    self.PWM.setMotorModel(600,600,600,600)
                    
                elif abs(L-R)<0.15:
                    self.PWM.setMotorModel(0,0,0,0)
                    
                elif L > 3 or R > 3:
                    if L > R :
                        self.PWM.setMotorModel(-1200,-1200,1400,1400)
                        
                    elif R > L :
                        self.PWM.setMotorModel(1400,1400,-1200,-1200)
                    
        except KeyboardInterrupt:
           led_Car.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is starting ... ')

    from optparse import OptionParser

    p = OptionParser()
    p.add_option('-r','--reverse',action='store_true',dest='reverse',help='Reverse motor directions', default=False)

    (opts, args) = p.parse_args()

    led_Car=Light(reverse=opts.reverse)
    led_Car.run()


        
    

