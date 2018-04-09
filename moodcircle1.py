#Filename: example2.py
#Author: Manya Trehan
#Date: 2018-03-02



from graphics import*

def main():
	win= GraphWin("Mood Circle",800,800)
	aCircle = Circle(Point(250,250),85)
	aCircle.draw(win)
	point = win.getMouse()
	
	aColoredCircle = Circle(Point(250,250),85)
	
	if point.getX()<200 and point.getY()<250:
		aColoredCircle.setFill("red")
		
	elif point.getX()<225 and point.getY()<250:
		aColoredCircle.setFill("blue")
		
	elif point.getX()>250 and point.getY()<250:
		aColoredCircle.setFill("black")
		
	elif point.getX()<275 and point.getY()<250:
		aColoredCircle.setFill("orange")
		
		
	
`	elif point.getX()<200 and point.getY()<500:
		aColoredCircle.setFill("pink")
		
	elif point.getX()<225 and point.getY()<500:
		aColoredCircle.setFill("yellow")
		

			elif point.getX()>250 and point.getY()<500:
		aColoredCircle.setFill("purple")
		
	elif point.getX()<275 and point.getY()<500:
		aColoredCircle.setFill("brown")
		
	
	aColoredCircle.draw(win)
	
	win.getMouse()
	
main()