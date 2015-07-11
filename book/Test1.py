
import turtle
pen = turtle.Pen()
turtle.bgcolor("black")
pen_color = "green"
pen.pencolor(pen_color)
pen.penup()
pen.forward(-300)
pen.pendown()
nam = "mathHomwork.py"
x = int((250 + 4) / 4)
pen.write(nam, font = ("Arial", x, "bold"))
problem = turtle.textinput("Enter a math problem","Enter a math problem, or 'q' to quit:   ")
while (problem != "q"):
    print("The answer to", problem,"is:", eval(problem))
    problem = turtle.textinput("Enter a math problem","Enter a math problem, or 'q' to quit:   ")

