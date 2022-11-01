import turtle
from turtle import Turtle, Screen
import random
class Sample:
    def __init__(self):
        self.over = Turtle()
        self.score = Turtle()
        self.colors = ["green", "yellow", "orange", "blue"]
        self.turt = []
        self.t1 = Turtle()
        self.screen = Screen()
        self.char()
        self.forv()
        self.cond = True
        self.t1.goto(0, -280)
        self.over.hideturtle()
        self.score.penup()
        self.scored = 2
        self.score.hideturtle()
        self.score.goto(-300, 280)
    def cars(self):
          self.over.hideturtle()
          self.score.hideturtle()
          for i in range(110):
            self.turt.append(turtle.Turtle())
          for star in range(0, 110):
            self.turt[star].color(random.choice(self.colors))
            self.turt[star].shape("square")
            self.turt[star].penup()
            self.ycord = random.randint(-240, 280)
            self.xcord = random.randint(200, 2560)
            self.turt[star].goto(self.xcord, self.ycord)
    def mov(self):
        self.over.hideturtle()
        self.score.hideturtle()
        for star in range(0, 110):
            self.turt[star].setheading(180)
            self.turt[star].forward(10)
    def prov(self):
        self.over.hideturtle()
        self.score.hideturtle()
        for i in range(110):
            if self.t1.distance(self.turt[i]) <= 20:
                self.over.write("GAME OVER", align="center", font=("Arial", 22, "bold"))
                self.cond=False
        if self.t1.ycor()>=280:
            self.score.clear()
            self.score.write(f"Level : {self.scored}", align="left", font=("Arial", 18, "normal"))
            self.over.hideturtle()
            self.scored += 1
            self.t1.goto(0, -295)
            for i in range(110):
                self.turt.append(turtle.Turtle())
            for star in range(0, 110):
                self.turt[star].color(random.choice(self.colors))
                self.turt[star].shape("square")
                self.turt[star].penup()
                self.ycord = random.randint(-240, 280)
                self.xcord = random.randint(200, 2560)
                self.turt[star].goto(self.xcord, self.ycord)
            for star in range(0, 110):
                self.turt[star].setheading(180)
                self.turt[star].forward(10)
                for m in range(1, 11):
                    self.turt[star].speed(m+1)

    def char(self):
        self.over.hideturtle()
        self.score.hideturtle()
        self.t1.shape("turtle")
        self.t1.color("black")
        self.t1.setheading(90)
        self.t1.penup()
    def forv(self):
        self.t1.forward(10)