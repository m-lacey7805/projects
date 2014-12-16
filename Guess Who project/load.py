import json

def load():
    try:
        with open ("test.txt",mode="rb")as file:
            data = json.read(file)
    except IOError:
        print("Failed")

load()
