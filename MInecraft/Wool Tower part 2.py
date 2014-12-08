import mcpi.minecraft as minecraft,time,random # imports stuff
mc = minecraft.Minecraft.create()


mc.setBlocks(-30,-5,-30,30,30,30,0)#clears area
    
for Block in range (100,-1):#makes a verticle tower of wool
    mc.postToChat(Block)
    mc.setBlock(0,Block,0,35,Block)
    time.sleep(2)



