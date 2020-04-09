bears = ['bears', 'bears' , 'bears']


def setup():
    size (500, 500)
    for i in range (98):
        bears.append('bears')
    bears[1] = 'bear'    
    items = (0, 'bears')
    index, letter = items
    for index, letter in enumerate (bears):
        print index, letter #There is a problem with floating the text here)
        

# def draw():
