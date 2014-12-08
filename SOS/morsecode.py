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
#Letters of alphabet in Morse
def morse(name):
        if name == "A":
            dot()
            dash()
            print ("A")
        elif name == "B":
            dash()
            dot()
            dot()
            dot()
            print ("B")
        elif name == "C":
            dot()
            dash()
            dot()
            dash()
        elif name == "D":
            dash()
            dot()
            dot()
        elif name == "E":
            dot()
        elif name == "F":
            dot()
            dot()
            dash()
            dot()
        elif name == "G":
            dash()
            dash()
            dot()
        elif name == "H":
            dot()
            dot()
            dot()
            dot()
        elif name == "I":
            dot()
            dot()
        elif name == "J":
            dot()
            dash()
            dash()
            dash()
        elif name == "K":
            dash()
            dot()
            dash()
        elif name == "L":
            dot()
            dash()
            dot()
            dot()
        elif name == "M":
            dash()
            dash()
        elif name == "N":
            dash()
            dot()
        elif name == "O":
            dash()
            dash()
            dash()
        elif name == "P":
            dot()
            dash()
            dash()
            dot()
        elif name == "Q":
            dash()
            dash()
            dot()
            dash()
        elif name == "R":
            dot()
            dash()
            dot()
        elif name == "S":
            dot()
            dot()
            dot()
        elif name == "T":
            dash()
        elif name == "U":
            dot()
            dot()
            dash()
        elif name == "V":
            dot()
            dot()
            dot()
            dash()
        elif name == "W":
            dot()
            dash()
            dash()
        elif name == "X":
            dash()
            dot()
            dot()
            dash()
        elif name == "Y":
            dash()
            dot()
            dash()
            dash()
        elif name == "Z":
            dash()
            dash()
            dot()
            dot()
            
        


msg= input("Enter message")
for each in msg:
    morse(each)
