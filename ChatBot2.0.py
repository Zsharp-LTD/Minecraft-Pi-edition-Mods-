#import and rename new modules
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Gather Data
Message = input("What do you want you ChatBot to say? ")

#Send Data
mc.postToChat(Message)
