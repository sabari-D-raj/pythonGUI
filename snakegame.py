from tkinter import*
import random 
from tkinter import messagebox
def createfood():
    x = random.randint(0, (game_width - space_size) // space_size) * space_size  #it will create random x position in canvas
    y = random.randint(0, (game_height - space_size) // space_size) * space_size  #it will create arandow y postion in canvas
    return canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color), [x, y]  #why i put [x,y] so it should coordinate in the cansvas as positin for the food
def move():
    global snake_coords, snake_squares, food, food_position, score
    x, y = snake_coords[0]
    #movement 
    if direction == "right":
        x += space_size  #why i put space,size because its width of one block like 20 i give so it increse exactly one step in grid
    elif direction == "left":
        x -= space_size
    elif direction == "up":
        y -= space_size     
    elif direction == "down":
        y += space_size

    newhead = [x, y]  #create new x and y
    snake_coords.insert(0, newhead)  #insert the x and y value to the new co ordinate
    squares = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snale_color)  # we created a new square for a new head
    snake_squares.insert(0, squares)
    #food hitting and score increase also the body
    if newhead == food_position:
        score += 1
        label.config(text="score{}".format(score))
        canvas.delete(food)
        food, food_position = createfood()
    else:
        del snake_coords[-1]
        canvas.delete(snake_squares[-1])
        del snake_squares[-1]


    #collision checking``
    if x >= game_width or y >= game_height or x < 0 or y < 0:
        game_over()
        return

    window.after(speed, move) #this will repeat the process like a loop

def game_over():
    messagebox.showinfo(title="snakegame", message="game over") 

def keybinding_direction(event):
    global direction
    key = event.keysym.lower() #.keysym it will give the name of key pressed as a string  its a tkinter function
    if key == "w" and direction != "down":   #  Why the Check direction != "down"? Imagine your snake is currently moving down. If the player presses "w" (up)                                             
        direction = "up"                    #and you allow the snake to instantly reverse direction, the snake will: it will make to 180
    elif key == "s" and direction != "up":
        direction = "down"
    elif key == "a" and direction != "right":
        direction = "left"
    elif key == "d" and direction != "left":
        direction = "right"

game_width = 600  #width of the gaming window
game_height = 600  #height of the gaming window
speed = 100  # speed in milisecond of snake moves
space_size = 20  #size of snake's rectangle and food
body = 3  #snake's intial size
snale_color = "green"
food_color = "red"
bg_color = "black"

window = Tk()
window.title("snake game")

snake_coords = [[100, 100], [80, 100], [60, 100]]  #the x co-ordinates are deacresed by 20 because it will make then line up side by side
snake_squares = []  #it will help with inresing of body
score = 0
direction = "right"

label = Label(text=f"score:{score}", font=('Arial', 16))  #format the value of score into the string
label.pack()

canvas = Canvas(window, bg=bg_color, height=game_height, width=game_width)
canvas.pack()

for x, y in snake_coords:
    squares = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snale_color)
    snake_squares.append(squares)  #snake body

food, food_position = createfood()

#key binding
window.bind("<w>", keybinding_direction)
window.bind("<s>", keybinding_direction)
window.bind("<a>", keybinding_direction)
window.bind("<d>", keybinding_direction)

move()
window.mainloop()
#what i learned: i learned a lot from this logic is still hard on me it take 2 weeks for me fuk i learned more about canvas grid ,aranging coordinates 
#its fun going do more projects when i have time and improve the logic, synatax and bulid in function ,modules 
#i will improve the game after gathering more knowledge(i'm happy) i'm improving day by day