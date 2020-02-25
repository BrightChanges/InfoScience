offset=50
def setup():
    size(500,500)
    background(255)

def draw():
    stroke(0)
    line(0,0,500,0) #Line
    y=0
    for n in range(10):
        line(0,y,500,y)
        y=y+50
        
    fill(3,0,0)  #First round's first black square
    stroke(255)
#odd rows
    d=0
    for n in range(5):
        c=0
        for n in range(5):
            square(c,d,50)
            c=c+100
        d=d+100

        
#even rows  
    d=50
    global offset
    for n in range(5):
        c= 0+ offset
        for n in range(5):
            square(c,d,50)
            c=c+100
        d=d+100
        
def mouseClicked():
    global offset
    offset=offset+1

        

    
    
    
        
    
