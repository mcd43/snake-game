import turtle
import random
import time

snake_body = []

def highscore():
  scores = open("scorehistorysnake.txt", "r")
  data = scores.readlines()
  return max(data) 

hs = highscore()

window = turtle.Screen()
window.bgcolor("Black")
w = 1200
h = 750
window.setup(w,h)
# window.title("Snake")
snake = turtle.Turtle()
snake.color("Purple")
snake.shape("circle")
snake.direction = "Stop"
snake.speed(0)
# snake.shapesize(1.5)

food = turtle.Turtle()
food.color("Red")
food.shape("circle")
# food.shapesize(0.7)
food.penup()
food.goto(100,100)
food.speed(0)

scoreboard = turtle.Turtle()
scoreboard.color("White")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-550,275)
FONT = ("Arial",20,"normal")
scoreboard.write("SCORE: "+ "\nHIGHSCORE: " + hs,font = FONT)
scoreboard.goto(-425,325)
scoreboard.goto(-425,325)

windowheight = 750
windowwidth = 1200
def moveup():
  snake.direction = "up"
def movedown():
  snake.direction = "down"
def moveright():
  snake.direction = "right"
def moveleft():
  snake.direction = "left"
def move():
  y = snake.ycor()
  x = snake.xcor()
  if snake.direction == "up":
    snake.sety(y+10)
  if snake.direction == "down":
    snake.sety(y-10)
  if snake.direction == "right":
    snake.setx(x+10)
  if snake.direction == "left":
    snake.setx(x-10)

def checkcollision(score):
  if snake.distance(food) < 15:
    growsnake()
    movefood()
    score += 1
  return score


def movefood():
  y = random.randint(-h/2,h/2)
  x = random.randint(-w/2, w/2)
  food.goto(x,y)

def checkbounds():
  y = snake.ycor()
  x = snake.xcor()
  if y >= 375:
    snake.sety(-h/2)
  if x >= 600:
    snake.setx(-w/2)
  if y <= -375:
    snake.sety(h/2)
  if x <= -600:
    snake.setx(w/2)

def updatescore(score, hs):
  scoreboard.undo()
  scoreboard.write(score, font = FONT)
  

def growsnake():
  body = turtle.Turtle()
  body.color("Purple")
  body.shape("circle")
  body.penup()
  body.speed(0)
  snake_body.append(body)
  for i in range(len(snake_body) - 1, 0, -1):
    x = snake_body[i-1].xcor()
    y = snake_body[i-1].ycor()
    snake_body[i].goto(x,y)
    if len(snake_body) > 0:
      x = snake.xcor()
      y = snake.ycor()
      snake_body[0].goto(x,y)

def showallsnake():
  for i in range(len(snake_body) - 1, 0, -1):
    x = snake_body[i-1].xcor()
    y = snake_body[i-1].ycor()
    snake_body[i].goto(x,y)
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x,y)

def checkdeath():
  if len(snake_body) > 1:
    for i in range(len(snake_body)- 1, 1, -1):
      print(snake_body[i].distance(snake))
      if snake_body[i].distance(snake) == 0.0:
        return False
  return True




def main():
  score = 0
  window.listen()
  window.onkeypress(moveup,"w")
  window.onkeypress(movedown,"s")
  window.onkeypress(moveright,"d")
  window.onkeypress(moveleft,"a")
  snake_body.append(snake)
  rungame = False
  while rungame:
      window.update()
      move()
      checkbounds()
      time.sleep(0.04)
      score = checkcollision(score)
      showallsnake()
      # rungame = checkdeath()
      updatescore(score, hs)
  scorefile = open("scorehistorysnake.txt","a")
  scorefile.write("\n" + str(score))
  scorefile.close()
  turtle.mainloop()


main()