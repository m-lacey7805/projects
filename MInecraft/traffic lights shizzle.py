import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

#move player to close origin
mc.player.setPos(10,20,0)

black=7
red=14
orange=1
green=5


#setup empty lights
while True:
    mc.setBlock(0,20,0,35,black)
    mc.setBlock(0,21,0,35,black)#red
    mc.setBlock(0,22,0,35,black)#amber
    mc.setBlock(0,23,0,35,black)#green
    mc.setBlock(0,24,0,35,black)
    mc.setBlock(0,25,0,35,black)
    time.sleep(3)
    mc.setBlock(0,21,0,35,red)
    time.sleep(5)
    mc.setBlock(0,22,0,35,orange)
    time.sleep(2)
    mc.setBlock(0,21,0,35,black)
    mc.setBlock(0,22,0,35,black)
    mc.setBlock(0,23,0,35,green)
    time.sleep(5)
    mc.setBlock(0,23,0,35,black)
    mc.setBlock(0,22,0,35,orange)
    time.sleep(3)



