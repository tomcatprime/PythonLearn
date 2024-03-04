import turtle as t
import heroes
import random
# from turtle import * - importing everything
#import turtle as t - importing module with alias so we use alias instead of name t.Turtle()

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.pensize(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
directions = [0, 90, 180, 270]

def square():
    tim.forward(100)
    tim.left(90)
    
# draw a dash line
def dash_line():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)    

for n in range(200):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))   

# for n in range(4):
#     square()

# for n in range(10):
#     dash_line()
    
# for shape_side in range(3, 11):
#     draw_shape(shape_side)

#random walk


# print(heroes.gen())
# hr = heroes.genarr(3)
# print(hr)
# print(type(hr))

