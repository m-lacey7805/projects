import picamera,time

def getPicture(name):
    try:
        with picamera.PiCamera() as camera:
            check = False
            while check == False:
                camera.start_preview()
                time.sleep(2)
                filename = "{0}.jpg".format (name)
                camera.capture(filename)
                camera.stop_preview()
                if input("Do u like ur Picture?[y/n]") == "y":
                        check = True

    except ("picamera.exc.PiCameraMMALError:","picamera.exc.PiCameraError:"):
        print("your Camera is not detected, please insert PiCamera and resart")
        filename = ""
    return filename                

def getCharProfile():
   name = input("what is your name?")
   

def getHairColour():
    hair = ""
    while not (hair in ["black","brown","blonde","ginger"]):
        hair = input("what is your hair colour?")

def getEyeColour():
    eye = ""
    while not (hair in ["blue","brown","green"]):
        eye = input("what is your eye colour?")    

    
def getGlasses():
    glasses = input("Do you have glasses?")


def getFacialHair():
    facialhair = input("Do you have FacialHair?")


