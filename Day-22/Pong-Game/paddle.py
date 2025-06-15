from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        """Creates paddle for pong, input 'right' or 'left' to create each paddle."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "right":
            self.goto(350, 0)
        elif side == "left":
            self.goto(-350, 0)
        self.color("white")
        self.penup()
        self.x = self.xcor()
        self.y = self.ycor()

    def move_up(self):
        if not self.y > 200:
            self.goto(self.x, self.y + 50)
            self.y = self.ycor()


    def move_down(self):
        if not self.y < -200:
            self.goto(self.x, self.y - 50)
            self.y = self.ycor()
