from mcpi.minecraft import Minecraft
mc = Minecraft.create()
LAVA = 10
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, LAVA, 1)
    
