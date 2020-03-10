grid = [ [1]*8 for n in range(8)]
grid[0][0] = -1
grid[7][7] = -1

w=70

def setup():
    size(800,600)
    
def draw():
    x,y= 0,0
    for row in grid:
        for col in row:
            if col == -1:
               fill(255,0,0)
            else:
                fill(255)
            rect(x,y,w,w)
            x=x+w
        y=y+w
        x=0
        
def mousePressed():
    grid[mouseY/w][mouseX/w] = grid[mouseY/w][mouseX/w]*-1
            
