x= [ ]
y= [ ]

def setup():
    global x, y
    size(500,500)
    
    #Setting up the 10 random coordinates
    for i in range(10):
        x.append(random(50,450))
        y.append(random(50,450))
            
                 

def draw():
    global x, y
    background(255)
      #Drawing the 10 individuals
    for individuals in range(10):
        strokeWeight(2)
        circle(x[individuals], y[individuals], 40)
        x[individuals]= x[individuals] + random(-10,10)
        y[individuals]= y[individuals] + random(-10,10)
        
        if x[individuals] > 500:
                x = 500
    
        if y[individuals] > 500:
                    y = 500
        if x[individuals] < 0:
                    x = 500
        if y[individuals] < 0:
                    y = 500
            
        delay(100)

    
    




   