import turtle
turtle.shape('turtle')
turtle.speed(1)
for side_lenth in range(100,140,10):
    for i in range(3):
     turtle.forward(side_lenth)
     turtle.left( 120)

turtle.exitonclick()