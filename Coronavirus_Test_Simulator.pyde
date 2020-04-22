from __future__ import division
peoplemoving=20
x= [ ]
y= [ ]
h= ["Sick", "Healthy"] #False=> infected
days = [30,-1]
infected=1
healthy=24
runs=1

def setup():
    size(500,500)
    
    #Setting up the ... random coordinates
    for i in range(25):
        x.append(random(0,500))
        y.append(random(0,500))
        h.append("Healthy") #All healthy, h is health
        days.append(-1)
    textSize(12);
        
def distance(x1, x2, y1, y2):
    a=(x1-x2)
    b=(y1-y2)        
    c= sqrt(a**2 + b**2)
    return c
            
                 

def draw():
    global x, y, infected, healthy, peoplemoving, runs, days
    runs=runs+1
    background(255)


      #Drawing the individuals
    for individuals in range(len(x)):
        strokeWeight(2)
        if h[individuals] == "Healthy":
            fill(255)  #healthy
        elif h[individuals] == "Recovered":
            fill(111,255,133) #recovered
        else:
            fill(255,0,0)  #infected
            
        circle(x[individuals], y[individuals], 40)
        #calulate the distance to each neighbors
        for neighbors in range(len(x)):
            if neighbors == individuals:
                continue
            d = distance(x[individuals], x[neighbors], y[individuals], y[neighbors])
            if d < 40 and (h[neighbors] == "Sick" or h[individuals]=="Sick") and (h[individuals] == "Healthy" or h[neighbors] == "Healthy"):
                #infection happens
                days[individuals]=30
                h[individuals] = "Sick"
                h[neighbors] = "Sick"
                infected = infected + 1
                healthy = healthy -1
                if healthy <0:
                    healthy=0
                if infected >25:
                    infected=25   #Need to put infected, healthy stuff in another if statement
    if h[individuals] == "Sick":
        days[individuals] -=1
        if days[individuals] == 0:
            h[individuals] == "Recovered"
            
                     
        
            
            
            
                
            
        
    for m in range(peoplemoving):    #Number of peope moving
        x[m]= x[m] + random(-10,10)
        y[m]= y[m] + random(-10,10)    
        if x[m] > 500:
                x[m] = 500
    
        if y[m] > 500:
                    y[m] = 500
        if x[m] < 0:
                    x[m] = 0
        if y[m] < 100:
                    y[m] = 100
    barGraph()        
    delay(100)


def barGraph():
    global infected, healthy, runs
    strokeWeight(1)
    fill(255,0,0)
    rect(60, 10, infected, 10) #(x coordinate, y coordinate, width, height)
    fill(3,3,3)
    text('Infected', 10,20)
    text(infected, 180,20)
    strokeWeight(1)
    fill(255)
    rect(60, 30, healthy, 10)
    fill(3,3,3)
    text('Healthy', 10,40)
    text(healthy, 180, 35)
    text('Click screen to run the simulation again', 10, 60)
    text('Iteration # :', 10,80 )
    text(runs, 120,80)

# def mouseClicked():
#     global runs
#     # global infected, healthy, x, y, h, runs, peoplemoving, days
#     # infected=1
#     # healthy=24
#     # peoplemoving=20
#     # x= [ ]
#     # y= [ ]
#     # h= ["Sick", "Healthy"]
#     # days = [30,-1]
#     runs= runs+1
#     # setup()
    # draw() 
    #How do i connect the iteration with the recovereding day list?/ Still not working
    
    
    
    
