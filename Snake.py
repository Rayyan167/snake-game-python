from turtle import Turtle

SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.new_snake = []
        self.create_snake()
        self.head = self.new_snake[0]

    def create_snake(self):
        for i in SNAKE_POSITIONS:
            self.add_segment(i)


    def add_segment(self,i):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(i)
        self.new_snake.append(snake)


    def extend(self):
        self.add_segment(self.new_snake[-1].position())


    def move(self):
        for i in range(len(self.new_snake) - 1, 0, -1):
            new_x = self.new_snake[i - 1].xcor()
            new_y = self.new_snake[i - 1].ycor()
            self.new_snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
