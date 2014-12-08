import mcpi.minecraft as minecraft #imports minecraftpi as minecraft
import time #imports time module
mc= minecraft.Minecraft.create() #connects to minecraft game

while True:   #while true do this
    Pos = mc.player.getPos()    #gets the position of player
    x = Pos.x    #creates variable x
    y = Pos.y    #creates variable y
    z = Pos.z    #creates variable z

    Block=41    #sets block variable to minecraft ID41 (Gold Block)

    mc.setBlock(x,y-1,z,Block)  #places a block where you are standing
    time.sleep(0.2)      #sleeps for 0.2 of a second
