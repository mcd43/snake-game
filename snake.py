import turtle
import random
import time

snake_body = []

score = 0

def highscore():
  scores = open("scorehistorysnake.txt", "r")
  data = scores.readlines()
  scores.close()
  return max(data) 

def createturtles(shape, color, size, x, y, hideturtle):
  t = turtle.Turtle()
  t.shape(shape)
  t.color(color)
  t.speed(0)
  t.direction = "Stop"
  t.shapesize(size, size, size)
  t.penup()
  t.goto(x,y)
  if hideturtle == True:
    t.hideturtle()
  return t

hs = highscore()

FONT = ("Arial",20,"normal")

window = turtle.Screen()
window.tracer(2, 2)
window.bgcolor("Black")
w = 1200
h = 750
window.setup(w,h)
# window.title("Snake")

snake = createturtles("circle", "Purple", 1.5, 0, 0, False)
food = createturtles("circle", "Red", 1.2, 100, 100, False)
scoreboard = createturtles("classic", "White", 1, -550, 275, True)

scoreboard.write("SCORE: " + "\nHIGHSCORE: " + hs,font = FONT)
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
  snakespeed = 10
  if snake.direction == "up":
    snake.sety(y+snakespeed)
  if snake.direction == "down":
    snake.sety(y-snakespeed)
  if snake.direction == "right":
    snake.setx(x+snakespeed)
  if snake.direction == "left":
    snake.setx(x-snakespeed)

def checkcollision(score):
  if snake.distance(food) < 15:
    body = createturtles("circle", "Purple", 1.5, 0, 0, False)
    snake_body.append(body)
    showallsnake()
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
  if y >= h/2:
    snake.sety(-h/2)
  if x >= w/2:
    snake.setx(-w/2)
  if y <= -h/2:
    snake.sety(h/2)
  if x <= -w/2:
    snake.setx(w/2)

def updatescore(score):
  scoreboard.undo()
  scoreboard.write(score, font = FONT)
  
def updatehighscore(score, hs):
  if score > int(hs):
    data = open("scorehistorysnake.txt", "w")
    data.write(str(score))
    data.close()

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
    print(snake_body)
    for idx in range(len(snake_body)-1, 0, -1):
      if snake_body[idx].distance(snake) < 15: 
        return False
  return True



def main():
  score = 0
  scoreboard.goto(-425,307)
  scoreboard.goto(-425,307)
  window.listen()
  window.onkeypress(moveup,"w")
  window.onkeypress(movedown,"s")
  window.onkeypress(moveright,"d")
  window.onkeypress(moveleft,"a")
  snake_body.append(snake)
  rungame = True
  while rungame:
      # window.update()
      move()
      checkbounds()
      time.sleep(0.04)
      score = checkcollision(score)
      showallsnake()
      rungame = checkdeath()
      updatescore(score)
      updatehighscore(score, hs)
  turtle.mainloop()


main()