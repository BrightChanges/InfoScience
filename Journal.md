$$$This is my journal$$$

CLASS NO.1:

1.What did we do?
We work as a team of 3 to write the commands for a robot to make a jelly bread using the jelly jars, the knife, cooking paper's bag and the bag of bread.

2.What did you learn?
I learned that to make a robot to do something, like making a jelly bread, I cannot just tell it: ''Make a jelly bread''. I need to give it very very specific and small commands like: ''Take a knife'', ''Stick the knife into the jelly jar'', ''Go down with the knife''. More importantly, today, I learned how to combine small commands into a big command. By repeating this big commands, I had saved time to write the command for the robot.

3.Question I have:No questions








CLASS NO.2:

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

3.Question I have: No questions

4.##Homework##:
1.Add lines from the middle of the window to each circle
2.Add lines from circle to circle









CLASS NO.3: 

1.What did we do? 
Creating a dice that give us random value each time we click
2.What did you learn?
I learnt the command if(), range of value of number in Python( 0~0.99=1, 1~1.99=2), draw a rectangle with curves,strengthen my understanding of def draw():, rbg value of main color like white, black, red.
3.Question I have: No questions

##Coding of today##
def setup():

    size(600,600)
    def draw():
    x=0 
    
def mouseClicked():

    n = random(0,6)
    print(n)
    background(0)
    fill(255)
    rect(100, 100, 400, 400, 20);
    fill(255,0,0)
    if 0<=n<1:
        circle(300,300,50)
    if 1<=n<2:
       circle(200,200,50) 
       circle(400,400,50)
    if 2<=n<3:
        circle(200,200,50) 
        circle(300,300,50)
        circle(400,400,50)
    if 3<=n<4:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
    if 4<=n<5:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
        circle(300,300,50)
    if 5<=n<6:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
        circle(400,300,50)
        circle(200,300,50)
        
3.Question I have: No questions



CLASS NO.4:

1.What did we do?
Create atomatic growing graphs that shows the amount of result I got from rolling, total amount of rolls's counter, and makes the dice to roll by itself
2.What did you learn?
I learnt how to use the command def barGraph():, stroke(), in...range(), and strengthen my understanding of global variables, the command print() and how to create rectangles.

##Coding of today##
one_c = 0
two_c = 0
three_c = 0
four_c = 0
five_c = 0
six_c = 0
total=0

def setup():

    size(600,600)
    textSize(30);

    
    
def draw():

    x=0 
    mouseClicked()
    delay(5)
    barGraph()

    
    
    
def barGraph():

    global one_c, two_c, three_c, four_c, five_c, six_c
    fill(255)
    stroke(255,0,0)
    fill(255,0,0)
    rect(50,540-one_c,20,one_c)
    rect(150,540-two_c,20,two_c)
    rect(250,540-three_c,20,three_c)
    rect(350,540-four_c,20,four_c)
    rect(450,540-five_c,20,five_c)
    rect(550,540-six_c,20,six_c)
    for x in range(0,6):
        text(x+1, 50 + 100*x,570)
 
    
def mouseClicked():

    global one_c, two_c, three_c, four_c, five_c, six_c, total
    n = random(0,6)
    background(0)
    fill(255)
    rect(100, 100, 400, 400, 20);
    fill(255,0,0)
    
    if 0<=n<1:
        circle(300,300,50)
        one_c +=1
        total +=1
        
    if 1<=n<2:
       circle(200,200,50) 
       circle(400,400,50)
       two_c +=1
       total +=1
       
    if 2<=n<3:
        circle(200,200,50) 
        circle(300,300,50)
        circle(400,400,50)
        three_c += 1
        total +=1
        
    if 3<=n<4:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
        four_c += 1
        total +=1
        
    if 4<=n<5:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
        circle(300,300,50)
        five_c += 1
        total +=1
    if 5<=n<6:
        circle(200,200,50) 
        circle(400,400,50)
        circle(200,400,50)
        circle(400,200,50)
        circle(400,300,50)
        circle(200,300,50)
        six_c += 1
        total +=1
    text("Number of rolls :",10,30) 
    text(total,300,30)  
    print("the number of 1", one_c)
    print("the number of 2", two_c)
    print("the number of 3", three_c)
    print("the number of 4", four_c)
    print("the number of 5", five_c)
    print("the number of 6", six_c)
3. Question I have: No questions




CLASS NO.5
1.What did we do? 
We create a traffic light that turn the light brighter for red, yellow, green in an order.
2.What did you learn?
I learn how to set up waiting time by using millis() and setting up another variable and reset codes by using close()

##Coding of today##
timer = 0
def setup():

    size(600,600)
    strokeWeight(10)
    fill(255,255,255)
    stroke(0,0,0)
    rect(200,100,200,400,20)
    
    timer=millis()    
    
def draw():

    global timer
    # turn off all LED
  
    
    clear()
    if millis()> timer + 1000:
        # red
        clear()
        fill(255,0,0)
        circle(300,180,100)
    if millis()> timer + 5000:
        # yellow
        clear()
        fill(255,255,0)
        circle(300,300,100)
        print(timer)
    
    if millis()> timer + 10000:
        clear()
        fill(0,255,0)
        circle(300,420,100)
        print(timer)
        
    if millis()> timer + 15000:
        timer = millis()

def clear():

    fill(128,0,0)
    circle(300,180,100)
    fill(149,143,24)
    circle(300,300,100)
    fill(0,100,0)
    circle(300,420,100)
3.Question I have: No questions



