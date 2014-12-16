import picamera,time

def getCharProfile():
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

    name = input("what is your name?")
   
    hair = ""
    while not (hair in ["black","brown","blonde","ginger"]):
        hair = input("what is your hair colour?")

    eye = ""
    while not (hair in ["blue","brown","green"]):
        eye = input("what is your eye colour?")    

    glasses = input("Do you have glasses?")

    facialhair = input("Do you have FacialHair?")

import json

def load():
    try:
        with open ("peopleData.txt",mode="r")as file:
            people = json.read(file)
    except IOError: 
        print("it didnt work")
        people= []
    return people

#def store():
    #people = getCharProfile():
    







#people = load()

