import turtle
import random
import time


window = turtle.Screen()
window.title('3quare')
window.bgcolor('white')
window.setup(width=400, height=600)
window.tracer(0)


# functions
def box_border(x, y):
	box_border = turtle.Turtle()
	box_border.speed(0)
	box_border.shape('square')
	box_border.color('black')
	box_border.shapesize(stretch_wid=5, stretch_len=5)
	box_border.penup()
	box_border.goto(x, y)
	return box_border

def box_inside(x, y):
	box_inside = turtle.Turtle()
	box_inside.speed(0)
	box_inside.shape('square')
	box_inside.color('white')
	box_inside.shapesize(stretch_wid=4.5, stretch_len=4.5)
	box_inside.penup()
	box_inside.goto(x, y)

	return box_inside

def new_enemy(x, y):
	enemy = turtle.Turtle()
	enemy.speed(0)
	enemy.shape('square')
	enemy.color('white')
	enemy.shapesize(stretch_wid=4, stretch_len=4)
	enemy.penup()
	enemy.goto(x, y)

	return enemy

def attack():
	box1.enemy.color('white')

# classes
class box():
	def __init__(self, x, y):
		self.border = box_border(x, y) # makes a black box
		self.inside = box_inside(x, y) # basically the white box inside the black box on top. This will make a white box with black border
		self.enemy = new_enemy(x, y) # makes the actual enemies inside the boxes

# setting up the sqaures/boxes
box1 = box(-115, -200)
box2 = box(-5, -200)
box3 = box(105, -200)

# controls
window.listen()
window.onkeypress(attack(), '[')


# main game loop
while True:
	enemy = random.randint(1, 3)
	targeted_box = random.randint(1, 3)
	if enemy == 1:
		if targeted_box == 1:
			box1.enemy.color('black')
		elif targeted_box == 2:
			box2.enemy.color('black')
		else:
			box3.enemy.color('black')

	window.update()
