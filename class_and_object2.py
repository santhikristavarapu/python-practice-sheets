class Room:
    name = "" 
    def __init__(self,name,walls):
        self.name = name
        self.floors = 1
        self.walls = walls
        self.door = 1 
    def open_door(self):
        print("door has been opened for",self.name)
    def see_walls(self):
        print("the",self.name,"has",self.walls,"walls")


bedroom = Room("bed-room",4)
bedroom.open_door()
bedroom.see_walls()
drawingroom = Room("drawing-room",4)
drawingroom.open_door()
drawingroom.see_walls()
kitchen = Room("kitchen",4)
kitchen.open_door()
kitchen.see_walls()
         
         
         