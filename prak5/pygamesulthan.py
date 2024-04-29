import tkinter as tk
import random
import time

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 100
BLOCK_SIZE = 20

# Snake class
class Snake:
    def __init__(self):
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == "Right":
            new_head = (head_x + BLOCK_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - BLOCK_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - BLOCK_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + BLOCK_SIZE)
        self.segments = [new_head] + self.segments[:-1]

    def change_direction(self, direction):
        if direction == "Right" and self.direction != "Left":
            self.direction = direction
        elif direction == "Left" and self.direction != "Right":
            self.direction = direction
        elif direction == "Up" and self.direction != "Down":
            self.direction = direction
        elif direction == "Down" and self.direction != "Up":
            self.direction = direction

    def grow(self):
        self.segments.append(self.segments[-1])

    def draw(self, canvas):
        for segment in self.segments:
            x, y = segment
            canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill="green")

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn_food()

    def spawn_food(self):
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.position = (x, y)

    def draw(self, canvas):
        x, y = self.position
        canvas.create_oval(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill="red")

# Game class
class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack()
        self.is_game_over = False
        self.bind_keys()
        self.update()

    def bind_keys(self):
        self.master.bind("<KeyPress-Up>", lambda event: self.snake.change_direction("Up"))
        self.master.bind("<KeyPress-Down>", lambda event: self.snake.change_direction("Down"))
        self.master.bind("<KeyPress-Left>", lambda event: self.snake.change_direction("Left"))
        self.master.bind("<KeyPress-Right>", lambda event: self.snake.change_direction("Right"))

    def update(self):
        if not self.is_game_over:
            self.canvas.delete("all")
            self.snake.move()
            self.check_collision()
            self.snake.draw(self.canvas)
            self.food.draw(self.canvas)
            self.score_label.config(text=f"Score: {self.score}")
            self.master.after(DELAY, self.update)

    def check_collision(self):
        head = self.snake.segments[0]
        if head in self.snake.segments[1:]:
            self.game_over()
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            self.game_over()
        if head == self.food.position:
            self.snake.grow()
            self.food.spawn_food()
            self.score += 1

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", font=("Helvetica", 24))

# Main function
def main():
    root = tk.Tk()
    root.title("Snake Game")
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
