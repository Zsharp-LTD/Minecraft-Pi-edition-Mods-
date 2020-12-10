#import functions
from mcpi.minecraft import Minecraft

#define variables
mc = Minecraft.create()
LAVA = 10

#mainloop
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, LAVA, 1)
    
