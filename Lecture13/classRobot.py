#4. Create a Robot class with the following attributes: orientation (left, right, up, down), 
# position_x, position_y. The Robot class should have the following methods: move, turn, and display_position. 
# The move method should take a number of steps and move the robot in the direction it is currently facing. 
# The turn method should take a direction (left or right) and turn the robot in that direction. 
# The display_position method should print the current position of the robot.

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

class Robot:

    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y
    

    def move(self, step):
        if self.orientation == RIGHT:
            self.position_x +=step

        elif self.orientation == LEFT:
            try:
                if self.position_x - step < 0:
                    raise Exception("please, turn your robot")
                else:
                    self.position_x -=step
            except Exception as e:
                print(e)

        elif self.orientation == DOWN:
            self.position_y +=step

        elif self.orientation == UP:
            try:
                if self.position_y - step < 0:
                    raise Exception("please, turn your robot")
                else:
                    self.position_y -=step
            except Exception as e:
                print(e)
        

    def turn(self, direction):
        if direction == LEFT: 
            if self.orientation == DOWN:
                self.orientation = RIGHT
            elif self.orientation == RIGHT:
                self.orientation = UP
            elif self.orientation == UP:
                self.orientation = LEFT
            elif self.orientation == LEFT:
                self.orientation = DOWN

        elif direction == RIGHT: 
            if self.orientation == DOWN:
                self.orientation = LEFT
            elif self.orientation == RIGHT:
                self.orientation = DOWN
            elif self.orientation == UP:
                self.orientation = RIGHT
            elif self.orientation == LEFT:
                self.orientation = UP


    def display_position(self):
        return (self.position_x, self.position_y)



Droid = Robot(UP, 0, 0)
print(Droid.display_position())
Droid.turn(RIGHT)
Droid.move(5)
print(Droid.display_position())
Droid.turn(RIGHT)
Droid.move(10)
print(Droid.display_position())
Droid.turn(RIGHT)
Droid.move(2)
print(Droid.display_position())