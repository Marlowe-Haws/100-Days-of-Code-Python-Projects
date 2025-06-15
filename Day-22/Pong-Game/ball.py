from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = self.xcor()
        self.y = self.ycor()
        self.move_x = 10
        self.move_y =10

    def update_x_y(self):
        self.x = self.xcor()
        self.y = self.ycor()

    def move(self):
            self.goto(self.x + self.move_x, self.y + self.move_y)
            self.update_x_y()

    def bounce(self, collision):
        if collision == "top" or collision == "bottom":
            self.move_y *= -1
        elif collision == "right" or collision == "left":
            self.move_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_x *= -1
        self.update_x_y()
      
