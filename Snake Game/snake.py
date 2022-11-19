from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        t1 = Turtle(shape="square")
        t1.color("white")
        t1.penup()
        t1.goto(position)
        self.segment.append(t1)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)
    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)