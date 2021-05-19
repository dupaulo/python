import turtle

star = turtle.Turtle()
star.shape('turtle')

for i in range(50):
 star.forward(i)
 star.forward(1)
 star.right(50)
 star.left(14)

turtle.done()