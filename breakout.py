import turtle

# Set up the game window
window = turtle.Screen()
window.title("Breakout Clone")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -280)
paddle_speed = 30

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

brick_width = 80  # Adjust the width of the bricks
brick_height = 20  # Adjust the height of the bricks
brick_spacing = 2  # Adjust the spacing between bricks
bricks_per_row = 7  # Adjust the number of bricks in each row

for i in range(5):
    brick_color = colors[i]
    for j in range(bricks_per_row):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(brick_color)
        brick.shapesize(stretch_wid=1, stretch_len=brick_width / 20)  # Calculate stretch_len
        brick.penup()
        x_pos = -((bricks_per_row - 1) * (brick_width + brick_spacing) / 2) + j * (brick_width + brick_spacing)
        y_pos = 180 - i * (brick_height + brick_spacing)
        brick.goto(x_pos, y_pos)
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 270)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 16, "normal"))

# Lives
lives = 3
lives_display = turtle.Turtle()
lives_display.speed(0)
lives_display.color("white")
lives_display.penup()
lives_display.hideturtle()
lives_display.goto(0, 250)
lives_display.write("Lives: {}".format(lives), align="center", font=("Courier", 16, "normal"))

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 240:
        x += paddle_speed  # Faster right movement
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -240:
        x -= paddle_speed  # Faster left movement
    paddle.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_right, "Right")
window.onkeypress(paddle_left, "Left")

# Ball movement
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Collision checking
def check_collision():
    global score
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -260:
        if (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50) and ball.dy < 0:
            ball.sety(-260)
            ball.dy *= -1

    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    for brick in bricks:
        if brick.distance(ball) < 30:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            # Check collision direction for both x and y
            if ball.dx > 0:
                ball.dx *= -1
            elif ball.dy > 0:
                ball.dy *= -1
            score += 10  # Increase the score
            update_score()  # Update the score display

# Update the score and lives displays
def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 16, "normal"))

def update_lives():
    lives_display.clear()
    lives_display.write("Lives: {}".format(lives), align="center", font=("Courier", 16, "normal"))

# Main game loop
while True:
    window.update()
    move_ball()
    check_collision()

    if len(bricks) == 0:
        # You won!
        win_text = turtle.Turtle()
        win_text.speed(0)
        win_text.color("white")
        win_text.penup()
        win_text.hideturtle()
        win_text.goto(0, 0)
        win_text.write("Congratulations! You won!", align="center", font=("Courier", 24, "normal"))
        window.update()
        break

    if ball.ycor() < -290:
        # Lose a life
        lives -= 1
        update_lives()
        ball.goto(0, 0)
        ball.dy *= -1

        if lives == 0:
            # Game over
            game_over_text = turtle.Turtle()
            game_over_text.speed(0)
            game_over_text.color("white")
            game_over_text.penup()
            game_over_text.hideturtle()
            game_over_text.goto(0, 0)
            game_over_text.write("Game Over", align="center", font=("Courier", 24, "normal"))
            window.update()
            break

# Close the window when clicking
window.exitonclick()
