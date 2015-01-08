import picamera,time,json

def getCharProfile():
    name = input("what is your name")

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
        filename = name
                

       
    hair = ""
    while not (hair in ["black","brown","blonde","ginger"]):
        hair = input("what is your hair colour?")

    eye = ""
    while not (eye in ["blue","brown","green"]):
        eye = input("what is your eye colour?")    

    glasses = input("Do you have glasses?[yes/no]")

    facialhair = input("Do you have FacialHair?[yes/no]")

    hat = input("Do you have a hat on?[yes/no]")
    return [name,hair,eye,glasses,facialhair,hat] 

def load():
    try:
        with open ("people.txt",mode="r")as file:
            people = json.read(file)
    except IOError: 
        print("it didnt work")
        people=[]
    return people

def store(people):
    person = getCharProfile()
    people.append(person)
    with open("people.txt",mode='w') as file:
        json.dump(people,file)
    return people

people = load()
print(people)
people = store(people)
