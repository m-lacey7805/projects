import mcpi.minecraft as minecraft,time,random
mc = minecraft.Minecraft.create()

while True:
    Pos = mc.player.getPos()
    x = Pos.x    #creates variable x
    y = Pos.y    #creates variable y
    z = Pos.z    #creates variable z

    Block = 13
    x = int(Pos.x)
    y = int(Pos.y)
    z = int(Pos.z)

    z = random.randint (z-15,z+15)
    x = random.randint (x-15,x+15)
    mc.setBlock(x,y+50,z,Block)
    time.sleep(0.01)
    
