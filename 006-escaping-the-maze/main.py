def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def sort_obstacle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def sort_maze():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

while front_is_clear():
    move()
turn_left()
sort_maze()