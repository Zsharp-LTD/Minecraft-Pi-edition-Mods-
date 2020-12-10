#import functions
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#define variable
tnt = 46

#mainloop
while True:
    x, y, z, = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)
