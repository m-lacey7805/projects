
import mcpi.minecraft as minecraft,time# Imports time module and minecraft 
mc = minecraft.Minecraft.create()#connects to minecraft game
mc.setBlocks(-90,-10,-90,90,80,90,0)#Clears an area

Black=35,15   #sets Black variable to minecraft ID35:15 (Black wool Block)
Green=35,5    #sets Green variable to minecraft ID35:5 (Green wool Block)
Purple=35,10  #sets Purple variable to minecraft ID35:10 (Purple wool Block)
Pink=35,2     #sets Pink variable to minecraft ID35:2 (Pink wool Block)

def SIGreen(z,y,x): #defines the space invader
    #creates a green space invader
    mc.setBlocks(x+14,y,z+9,x,y,z,Black) #(creates a black wool cuboid (14,1,9)
    mc.setBlock(x+4,y,z+1,Green)
    mc.setBlock(x+10,y,z+1,Green)
    mc.setBlock(x+5,y,z+2,Green)
    mc.setBlock(x+9,y,z+2,Green)
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+3,Green)
    for Block in range(3,12):
        mc.setBlock(x+Block,y,z+4,Green)
    for Block in range(2,13):
        mc.setBlock(x+Block,y,z+5,Green)
    mc.setBlock(x+5,y,z+4,Black)
    mc.setBlock(x+9,y,z+4,Black)
    for Block in range(6,8):
        mc.setBlock(x+2,y,z+Block,Green)#iknow its not efficient :(
    for Block in range(6,8):
        mc.setBlock(x+12,y,z+Block,Green)  
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+6,Green)
    mc.setBlock(x+4,y,z+7,Green)
    mc.setBlock(x+10,y,z+7,Green)
    for Block in range(5,7):
        mc.setBlock(x+Block,y,z+8,Green)
    for Block in range(8,10):
        mc.setBlock(x+Block,y,z+8,Green)

def SIPurple(x,y,z): #defines the space invader
    #creates a Purple space invader
    mc.setBlocks(x+14,y,z+9,x,y,z,Black)#(creates a black cuboid (14,1,9)
    mc.setBlock(x+4,y,z+1,Purple)
    mc.setBlock(x+10,y,z+1,Purple)
    mc.setBlock(x+5,y,z+2,Purple)
    mc.setBlock(x+9,y,z+2,Purple)
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+3,Purple)
    for Block in range(3,12):
        mc.setBlock(x+Block,y,z+4,Purple)
    for Block in range(2,13):
        mc.setBlock(x+Block,y,z+50,Purple)#iknow its not efficient :(
    mc.setBlock(x+5,y,z+4,Black)
    mc.setBlock(x+9,y,z+4,Black)
    for Block in range(6,8):
        mc.setBlock(x+2,y,z+Block,Purple)
    for Block in range(6,8):
        mc.setBlock(x+12,y,z+Block,Purple) #its here :P
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+6,Purple)
    mc.setBlock(x+4,y,z+7,Purple)
    mc.setBlock(x+10,y,z+7,Purple)
    for Block in range(5,7):
        mc.setBlock(x+Block,y,z+8,Purple)
    for Block in range(8,10):
        mc.setBlock(x+Block,y,z+8,Purple)

def SIPink(x,y,z): #defines the space invader
    #creates a green Pink space invader
    mc.setBlocks(x+14,y,z+9,y,x,z,Black) #(creates a black cuboid (14,1,9)
    mc.setBlock(x+4,y,z+1,Pink)
    mc.setBlock(x+10,y,z+1,Pink)
    mc.setBlock(x+5,y,z+2,Pink)
    mc.setBlock(x+9,y,z+2,Pink)
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+3,Pink)
    for Block in range(3,12):
        mc.setBlock(x+Block,y,z+4,Pink) #iknow its not efficient :(
    for Block in range(2,13):
        mc.setBlock(x+Block,y,z+5,Pink)
    mc.setBlock(x+5,y,z+4,Black)
    mc.setBlock(x+9,y,z+4,Black)
    for Block in range(6,8):
        mc.setBlock(x+2,y,z+Block,Pink)
    for Block in range(6,8):
        mc.setBlock(x+12,y,z+Block,Pink)
    for Block in range(4,11):
        mc.setBlock(x+Block,y,z+6,Pink)
    mc.setBlock(x+4,y,z+7,Pink)
    mc.setBlock(x+10,y,z+7,Pink)
    for Block in range(5,7):
        mc.setBlock(x+Block,y,z+8,Pink) 
    for Block in range(8,10):
        mc.setBlock(x+Block,y,z+8,Pink)

while True: # while true do the space invader animation (this repeats the functions that told to do)
    SIPurple(0,0,0) #does the SIPurple function(makes a Purple space invader)
    time.sleep(0.5) # sleepy time for half a second
    SIGreen(0,0,0)  #does the SIGreen function(makes a Green space invader)
    time.sleep(0.5) # sleepy time for half a second
    SIPink(0,0,0)   #does the SIPink function(makes a Pink space invader)
    time.sleep(0.5) # sleepy time for half a second
    #Matt Lacey ;-)



