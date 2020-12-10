#import and rename functions
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#define variables
tnt = 46

#mainloop
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, tnt, 1)
    
