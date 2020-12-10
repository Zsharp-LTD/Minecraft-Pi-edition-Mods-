#import functions
from mcpi.minecraft import Minecraft
from time import sleep

#define variables
mc = Minecraft.create()
flower = 38

#mainloop
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
    
