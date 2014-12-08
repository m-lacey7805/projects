import mcpi.minecraft as minecraft,time,random
mc = minecraft.Minecraft.create()


mc.setBlocks(-30,-5,-30,30,30,30,0)
    
for Block in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14):
    mc.postToChat(Block)
    mc.setBlock(0,Block,0,35,Block)
    time.sleep(2)



