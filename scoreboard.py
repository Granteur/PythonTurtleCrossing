from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_scoreboard()
        
    #create scoreboard that keeps track of level, level should increase after successful crossing
    def increase_level(self):
        self.level += 1
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    #when turtle gets hit, print GAME OVER centerscreen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



