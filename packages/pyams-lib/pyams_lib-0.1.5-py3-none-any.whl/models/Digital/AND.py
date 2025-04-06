﻿#-------------------------------------------------------------------------------
# Name:        AND
# Author:      Dhiabi Fathi
# Created:     14/03/2022
# Update:      04/10/2024
# Copyright:   (c) PyAMS
# Licence:     free
#-------------------------------------------------------------------------------

from PyAMS import model,signal,param
from electrical import voltage


# AND Gate Model----------------------------------------------------------------
class AND(model):
     def __init__(self,Out,In1,In2):
        #Signals declarations---------------------------------------------------
         self.Vin1 = signal('in',voltage,In1)
         self.Vin2 = signal('in',voltage,In2)
         self.Vout = signal('out',voltage,Out)
        #Parameter declarations-------------------------------------------------
         self.IL=param(0.2,'V','In low voltage')
         self.IH=param(3.2,'V','In high voltage')
         self.OL=param(0.0,'V','Out low voltage')
         self.OH=param(5.0,'V','Out high voltage')

     def analog(self):
         if((self.Vin1<=self.IL)or(self.Vin2<=self.IL)):
            self.Vout+=self.OL
         elif((self.Vin1>=self.IH)and(self.Vin2>=self.IH)):
            self.Vout+=self.OH



