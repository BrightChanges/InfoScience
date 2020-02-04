x2=0
y2=0
x=500
y=500

def setup():
    size(1000,1000)
    background(255)
    textAlign(CENTER, CENTER)
def draw():
    print("")
    
def mouseClicked():
    global x2, y2, x, y
    x2=x
    y2=y
    x= mouseX
    y= mouseY
    z= random(10,100)
    r= random(0,255)
    g= random(0,255)
    b= random(0,255)
    fill(r, g, b)
    line( x, y, x2, y2)
    circle(x, y, z)
    fill(0)
    textSize(z/3);
    text ("Kien", x, y)


    
    

    
