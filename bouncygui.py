"""
program: bouncygui.py
author : audrey 10/20/2020

GUI-based version of the bouncy.py app from chapter 3.
Program will calculate the total distance travelled by a bouncing ball.
User will input:
   	The starting height of the ball
   	How bouncy the ball is
   	How many bounces the ball will make
The output should be the total distance that the ball travels
"""

from breezypythongui import EasyFrame
from tkinter.font import Font 

class Bouncy(EasyFrame):

	def__init__(self):
		"""sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Bouncy App", background = "lightblue")
		#create a variable to store a Front object
		myFont = Font(family = "Courier New", size = 16, weight = "bold")

		#Add the label widgets
		self.addLabel(text = "Bouncy experment", row = 0, column = 0 , columnspan = 2 , background = "lightblue", font = myFont)

		self.addLabel(text = "Intital Height", row = 1, column = 0, background = "lightblue")
		self.addLabel(text = "Bounciness Index:" , row = 2, column = 0, background = "lightblue")
		self.addLabel(text = "No of Bounciness :", row = 3 ,column = 0 ,background = "lightblue")
		self.addLabel("Total Distance:", row = 5 , column = 0 , background = "lightblue")

		#add the entry field widgets 
		self.height = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.index = self.addFloatField(value =0.0 , row = 2, column = 1 )
		self.bounces = self.addIntegerField(value =0.0,row= 3, column = 1)
		self.distance = self addFloatField(value = 0.0 , row = 5 , column = 1, precision = 2 , sate = "read only")

		#add the command button 
		self.addButton(text = "compute", row = 4, column = 0, columnspan = 2, command = self.bounce) 
		self.myButton["foreground"] = "red"
		self.myButton["background"] = "yellow"

	def bounce(self):
		""" calculates the total distance traveled give the inputs."""
		# input phase
		height = self.height.getNumber()
		index  = self.index.getNumber()
		bounces = self.bounces.getNumber()
		​
		# accumulator variable for the total distance traveled
		totalDistance = 0.0
		​
		# for loop to determine the total distance traveled
		for count in range(bounces):
			totalDistance += height
			height *= index
			totalDistance += height 
		​
		# output of the total distance
		self.distance.setNumber(totalDistance)





#definition of the main() fuction
def main():
	Bouncy().mainloop()
#global call to main()
main()