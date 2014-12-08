import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(3)
mc.postToChat("3")
time.sleep(2)
mc.postToChat("2")
time.sleep(2)
mc.postToChat("1")
time.sleep(1)

while True: 
    mc.player.setPos(0,69,0)
    time.sleep(3)
    mc.player.setPos(69,0,0)
    time.sleep(3)
    mc.player.setPos(0,0,69)
    time.sleep(1)
mc.postToChat("Teleportation Complete")
