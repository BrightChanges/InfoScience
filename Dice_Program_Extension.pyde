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
