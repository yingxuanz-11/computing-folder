#find the error here!  don't be fooled by the unfamiliar code!
import pyb

pyb.LED(3).on()                
pyb.delay(2000)                
switch_value = pyb.Switch()()  
pyb.LED(3).off()                

pyb.LED(4).on()                

if switch_value:
    pyb.usb_mode('CDC+MSC')
else:
    pyb.usb_mode('CDC+HID')

pyb.LED(4).off()               
