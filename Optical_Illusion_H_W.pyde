def setup():
#Lines
    size(720,480)
    background(0)
    stroke(180,180,180)
    strokeWeight(10)
    line(0,80,720,80)
    y=80
    for n in range(5):
        line(0,y,720,y)
        y=y+80
    
    line(80,0,80,480)
    x=80
    for n in range(8):
        line(x,0,x,480)
        x=x+80

def draw():
#The 1st row of white circles
    fill(255)
    strokeWeight(0)
    circle(80,80,10)
    y=80
    for n in range(5):
        circle(80,y,10)
        y=y+80
#Repetition of ''the 1st row of white circles''
    x=80
    for n in range(8):
        y=80
        for n in range(5):
            circle(x,y,10)
            y=y+80
        x=x+80
    
    
