import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SPEED = 100  # milliseconds
SPACE_SIZE = 20  # size of each square
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "white"

class Snake: 
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # starting position (Snake head  +  body)
        for i in range (BODY_PARTS):
            self.coordinates.append([i * SPACE_SIZE, 0])

        # Drawing the snake 
        for x , y in self.coordinates:
            square = canvas.create_rectangle(
                x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0,(WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(
            x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag="food"
        )

def next_trun (snake, food):
    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "dowm":
        y += SPACE_SIZE
    elif direction == "left":
        y -= SPACE_SIZE
    elif direction == "right":
        y += SPACE_SIZE

    # insert new head 
    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(
        x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    ) 
    snake.squares.insert(0,square)

    # if snake eats food 
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1 
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else :
        # remove tail
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_trun, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == "left" :
        if direction != "right" :
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down" :
        if direction != "up":
            direction = new_direction

def check_collisions(snake) :
    x,y = snake.coordinates[0]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates [1:]:
        if x == body_part[0] and y == body_part[1] :
            return True

    return False

def game_over () :
    canvas.delete("all")
    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text = "GAME OVER",
        fill = "red",
        font=("Arial", 30),
    )   


# main program 

window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = tk.Label(window, text= f"Score : {score}", font=("Arial", 14))
label.pack()

canvas = tk.Canvas(window, bg = BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

# Center window

x = (window.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (window.winfo_screenheight() // 2) - (HEIGHT // 2)
window.geometry(f"{WIDTH}x{HEIGHT+20}+{x}+{y}")

snake = Snake()
food = Food()

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction ("up"))
window.bind("<Down>", lambda event: change_direction("down"))

next_trun (snake, food)

window.mainloop()