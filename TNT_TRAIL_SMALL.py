from mcpi.minecraft import Minecraft
mc = Minecraft.create()
tnt = 46
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, tnt, 1)
    
