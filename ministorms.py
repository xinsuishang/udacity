import turtle

def draw_square(draw):
    for i in range(1,5):
        draw.forward(100)
        draw.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()
