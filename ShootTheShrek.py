import pgzrun
from random import randint

TITLE="Shoot The Shrek"

WIDTH=500
HEIGHT=500
message="Click Shrek Potter to shoot him"
shrek = Actor('shrekpotter')

def draw():
    screen.clear()
    screen.fill(color=(100,28,30))
    shrek.draw()
    screen.draw.text(message, center=(200,10),fontsize=30)

def place_shrek():
    shrek.x=randint(50,WIDTH-50)
    shrek.y=randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if shrek.collidepoint(pos):
        message ="Good shot"
        place_shrek()
    else:
        message="You missed lol"

place_shrek()
pgzrun.go()