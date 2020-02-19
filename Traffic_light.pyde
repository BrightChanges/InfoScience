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

    
    




    
