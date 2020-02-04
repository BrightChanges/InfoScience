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

    circle(x, y, z)
    fill(0)
    textSize(z/3);
    text ("Kien", x, y)
    print(x, y)
    line(500,500,x,y)
