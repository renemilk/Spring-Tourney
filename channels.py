# -*- coding: utf-8 -*-
try:
	from ParseConfig import *
except:
	from tasbot.ParseConfig import *

class Main:
	sock = 0
	def onload(self,tasc):
		self.app = tasc.main
	def oncommandfromserver(self,command,args,socket):
		pass
	def onloggedin(self,socket):
		for channel in parselist(self.app.config["channelautojoinlist"],","):
			socket.send("JOIN " + channel + "\n")		
