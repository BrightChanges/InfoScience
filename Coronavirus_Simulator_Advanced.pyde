from __future__ import division
Xlst = list()
Ylst = list()
HealthState =["Infected", "Healthy"] #False - infected
days = [30, -1]
NumOfHumans = 25
NumOfMoving = 25
CriticalDist = 40 
iteration = 0
Infected = 1
Recovered = 0
DaysNeededToRecover = 30 #int convert a number into an interger number #int(random(100,200))

def bargraph():
    global Infected, Xlst, HealthState
    Healthy = len(Xlst) - Infected
    
    text("Infected",230, 545)
    text(Infected,550, 545)
    fill(255,0,0)
    rect(315, 530,Infected*5,20)
    fill(0)
    text("Healthy",230, 575)
    text(Healthy,550, 575)
    stroke(0)
    fill(255)
    rect(315, 560,Healthy*5,20)
    fill(0)
    text("Recovered",230, 605)
    text(Recovered,550, 605)
    fill(137,242,255)
    rect(340, 587,Recovered*5,20)
    



    
    
def setup():
    global Xlst,Ylst, NumOfHumans,HealthState
    size(600,700)

    
    for i in range(NumOfHumans):
        ValX = int(random(50,450))
        Xlst.append(ValX)
        ValY = int(random(50,450))
        Ylst.append(ValY)
        ValY = int(random(50,450))
        Ylst.append(ValY)
        HealthState.append("Healthy")
        days.append(-1)
        
def distance(x1,x2,y1,y2):
    a = (x1 - x2)
    b = (y1 - y2)
    c = sqrt(a**2 + b**2)
    return c
    
def draw():
    global Xlst,Ylst, HealthState, NumOfHumans, CriticalDist, iteration, Healthy, Infected, Recovered, DaysNeededToRecover, NumOfMoving
    background(255,254,237)
    strokeWeight(2)

    Infected = 0
 #   Recovered = 0
    for ind in range(NumOfHumans):
        if HealthState[ind] == "Infected":
            Infected += 1

    
    bargraph()  
    for ind in range(NumOfHumans):
        if HealthState[ind] == "Healthy":
            fill(255)   #healthy
        elif HealthState[ind] == "Recovered":
            fill(137,242,255)
        else:
            fill(255, 0, 0) #infected
        
        if HealthState[ind] == "Infected":
            days[ind] -= 1
            if days[ind] == 0:
                HealthState[ind] = "Recovered" 
                Recovered += 1
                days[ind] = 0 #0 for recovered, -1 for healthy, and 30 for sick

            
                               
        #movement of the circles   
        circle(Xlst[ind], Ylst[ind], 40) 
        
        #calculating the distance between the circles
        for nei in range(NumOfHumans):
            if nei==ind:
                continue
            d = distance(Xlst[ind], Xlst[nei], Ylst[ind], Ylst[nei])
            if d < CriticalDist and (HealthState[nei] == "Infected" or HealthState[ind] == "Infected"):
                if HealthState[nei] == "Healthy":
                    HealthState[nei] = "Infected"
                    days[nei] = DaysNeededToRecover
                if HealthState[ind] == "Healthy":
                    HealthState[ind] = "Infected"
                    days[ind] = DaysNeededToRecover
            

                                
    for m in range(NumOfMoving):
        Xlst[m] = Xlst[m] + random(-10,10)
        Ylst[m] = Ylst[m] + random(-10,10)
        
        if Xlst[m] > 500:
            Xlst[m] = 500
        if Xlst[m] < 0:
            Xlst[m] = 0
        if Ylst[m] > 500:
            Ylst[m] = 500
        if Ylst[m] < 0:
            Ylst[m] = 0

 

    
    iteration = iteration + 1
    fill(0)
    textSize(20)
    text("iteration = ",50,550)
    text(iteration,160,550)
    delay(100)
    
    
    
    
