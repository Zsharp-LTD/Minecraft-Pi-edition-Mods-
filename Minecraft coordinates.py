from mcpi.minecraft import Minecraft
from turtle import *
import time
mc = Minecraft.create()
style = ('Courier', 30, 'italic')
while True:
    pos = mc.player.getPos()
    write(pos, font=style, align='center')
    time.sleep(0.2)
    clear()