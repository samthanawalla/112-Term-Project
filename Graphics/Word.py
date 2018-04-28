from panda3d.core import *
from direct.showbase import DirectObject
from Utils.Picker import *
import direct.directbase.DirectStart
from panda3d.physics import *
import random

#Word object which tracks and moves its location
class Word(DirectObject.DirectObject):
	def __init__(self, render, x, y, z, label, color):
		self.x = x
		self.y = y
		self.z = z
		self.label = label
		path = "Graphics/models/" + color + "sphere.egg"
		self.sphere = loader.loadModel(path)
		self.sphere.setScale(1.1)
		self.myPicker = Picker(self.onHit)
		self.myPicker.makePickable(self.sphere)
		self.sphere.setPos(self.x, self.y, self.z)
		text = TextNode(label)
		text.setText(label)
		text.setTextColor(0, 0, 0, 1)
		text.setAlign(TextNode.ACenter)
		textNode = self.sphere.attachNewNode(text)
		textNode.setScale(1.3)
		textNode.setPos(0,-2,0)
		####
		node = NodePath(label)
		node.reparentTo(render)
		an = ActorNode(label)
		anp = node.attachNewNode(an)
		base.physicsMgr.attachPhysicalNode(an)
		self.sphere.reparentTo(anp)
		an.getPhysicsObject().setMass(3)
		
	def move(self):
		(x, y, z) = self.sphere.getPos() 
		if(z<-5):
			print(z)
			self.sphere.detachNode()
			return False
		return True

	def onHit(self):
		ob = self.myPicker.getObjectHit(base.mouseWatcherNode.getMouse()) 
		if(ob!=None):
			(choice1, choice2) = (self.getChoice(), self.getChoice())
			if(choice1 == "move" or choice2 == "move"):
				(x,y,z) = ob.getPos()
				(dx,dy,dz) = (random.randint(0,5),random.randint(0,5),random.randint(0,5))
				ob.setPos(x+dx,y+dy,z+dz)
			else:
				ob.setPos(0,0,-20)

	def getChoice(self):
		return random.choice(["pop", "move", "move"])

