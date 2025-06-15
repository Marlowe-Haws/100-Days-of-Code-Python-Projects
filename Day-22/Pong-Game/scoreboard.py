from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-0, 270)
        self.write(f"{self.player_1_score}  :  {self.player_2_score}",
                   align="center", font=("Courier", 20, "normal"))

    def final_score(self):
        self.clear()
        if self.player_1_score > self.player_2_score:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.goto(0, 30)
        self.write("Game over.", align="center", font=("Courier", 20, "normal"))
        self.goto(0, 0)
        self.write(f"{winner} is the winner!", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -30)
        self.write(f"Final score {self.player_1_score}:{self.player_2_score}",
                   align="center", font=("Courier", 20, "normal"))
