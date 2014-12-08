#SOS
import RPi.GPIO as GP,time         
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#Defining dot
def dot():
    GP.output(11,GP.HIGH)                                                 
    time.sleep(0.5)
    GP.output(11,GP.LOW)
    time.sleep(0.25)
#Defining dash
def dash():
    GP.output(11,GP.HIGH)
    time.sleep(0.8)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

def morse():
        if name == "A":
            dot()
            dash()
        elif name == "B":
            dash()
            dot()
            dot()
            dot()
