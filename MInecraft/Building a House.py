import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()
mc.setBlocks(-90,-10,-90,90,80,90,0)#clears area


def house(x,y,z):
    mc.setBlocks(x,y,z,x+5,y+4,z+7,45)#makes brick block
    mc.setBlocks(x+1,y,z+1,x+4,y+4,z+6,0)#clears a hole in brickblock
    mc.setBlocks(x,y-1,z,x+5,y-1,z+7,5)#makes a wood floor
    mc.setBlocks(x,y+5,z,x+5,y+5,z+7,20)#makes glass roof
    mc.setBlocks(x+2,y,z,x+3,y+1,z,0)#makes doorway

house(20,0,20)
house(30,0,20)
house(40,0,20)
house(50,0,20)
house(60,0,20)
house(70,0,20)
house(80,0,20)
house(20,0,0)
house(30,0,0)
house(40,0,0)
house(50,0,0)
house(60,0,0)
house(70,0,0)
house(80,0,0)
