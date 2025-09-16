import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Simple Obstacle Avoidance Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Player
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, -250)

# Goal zone
goal = turtle.Turtle()
goal.hideturtle()
goal.penup()
goal.goto(-300, 250)
goal.color("lightgreen")
goal.begin_fill()
for _ in range(2):
    goal.forward(600)
    goal.left(90)
    goal.forward(50)
    goal.left(90)
goal.end_fill()

# Obstacles
obstacles = []
for y in [-150, -50, 50, 150]:
    obs = turtle.Turtle()
    obs.shape("square")
    obs.shapesize(stretch_wid=1, stretch_len=4)
    obs.color("red")
    obs.penup()
    obs.goto(random.randint(-250, 250), y)
    obs.dx = random.choice([-3, 3])
    obstacles.append(obs)

# Movement
def go_left():
    x = player.xcor() - 20
    if x > -280:
        player.setx(x)

def go_right():
    x = player.xcor() + 20
    if x < 280:
        player.setx(x)

def go_up():
    y = player.ycor() + 20
    if y < 280:
        player.sety(y)

def go_down():
    y = player.ycor() - 20
    if y > -280:
        player.sety(y)

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")

# Collision check
def is_collision(t1, t2):
    return abs(t1.xcor() - t2.xcor()) < 40 and abs(t1.ycor() - t2.ycor()) < 20

# Game loop
while True:
    wn.update()

    # Move obstacles
    for obs in obstacles:
        obs.setx(obs.xcor() + obs.dx)
        if obs.xcor() > 280 or obs.xcor() < -280:
            obs.dx *= -1

        # Collision with player
        if is_collision(player, obs):
            player.goto(0, -250)
            print("Game Over!")
            time.sleep(1)

    # Reached goal
    if player.ycor() > 250:
        print("You Win!")
        player.goto(0, -250)
        time.sleep(1)
