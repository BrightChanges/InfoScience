#This is my journal

Class No.1:
1.What did we do?
We work as a team of 3 to write the commands for a robot to make a jelly bread using the jelly jars, the knife, cooking paper's bag and the bag of bread.

2.What did you learn?
I learned that to make a robot to do something, like making a jelly bread, I cannot just tell it: ''Make a jelly bread''. I need to give it very very specific and small commands like: ''Take a knife'', ''Stick the knife into the jelly jar'', ''Go down with the knife''. More importantly, today, I learned how to combine small commands into a big command. By repeating this big commands, I had saved time to write the command for the robot.

3.Question I have:




Class No.2:
1.What did we do? 
Installed Python

Learn to use def, fill, print, set up background, size, generate random color, x and y coordinates, mouseClicked.

##Coding of today##( generate a program that generate random color, random size circle each time I click into the window)
 
```.py
    def setup():
        size(1000,1000)
        background(255)
        textAlign(CENTER, CENTER)

    def draw():
        print("")

    def mouseClicked():
        x= mouseX
        y= mouseY
        z= random(10,100)
        r= random(0,255)
        g= random(0,255)
        b= random(0,255)
        fill(r, g, b)

        print(x)
        circle(x, y, z)
        fill(0)
        textSize(z/3);
        text ("Kien", x, y)
        print(x, y)
        line(500,500,x,y)
 ```
2.What did you learn? I that in Python, if I want "something1" to be infront of "something2", I need to code that "something" infront of "something2"

3.Question I have:

4.##Homework##:
1.Add lines from the middle of the window to each circle
2.Add lines from circle to circle


