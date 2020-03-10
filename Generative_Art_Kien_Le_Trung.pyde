def setup():
    size(1000, 1000)
    background(255, 255, 255)
    

    noStroke()

    
    for c in range(1000):
        center_x= random(200, 800)
        center_y= random(200, 800)
        cs=50
        #Draw Shadow
        noStroke()
        fill(15,15,15,10)
        for i in range(30):
            circle(center_x,center_y,cs-i*5)
     
    #Draw Circle
        stroke(30,30,30)
        fill(random(50, 255), random(50, 255), random(200, 255))
        circle(center_x-25,center_y-25,cs)
        
   
