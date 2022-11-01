import time
import turtle
from turtle import Screen
from genturt import Sample
import time
screen = Screen()
screen.screensize(600, 600)
sn = Sample()
screen.tracer(0)
screen.title("ROAD-CROSSING")
screen.listen()
sn.cond = True
sn.cars()
while sn.cond:
    screen.update()
    time.sleep(0.1)
    sn.char()
    sn.mov()
    sn.prov()
    screen.onkey(sn.forv, "Up")








screen.exitonclick()





