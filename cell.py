class cell:
    def __init__(self,x,y):
        self.visited = False
        self.solve_visited = False
        self.wall_status = {
            "up" : 1,
            "down" : 1,
            "left" : 1,
            "right" : 1
        }
        self.pos = {
            "x" : x,
            "y" : y
        }
        self.type = {
            "start" :False,
            "end" : False
        }

    def get_visited(self):
        return self.visited
    
    def get_wall_status(self):
        return self.wall_status
    
    def get_pos(self):
        return self.pos
    
    def set_wall_status(self,wall):
        if wall in self.wall_status:
            self.wall_status[wall] = 0

    def set_visited(self):
        self.visited = True

    def set_type(self,type,true_false):
        if type in self.type:
            self.type[type] = true_false

    def get_type(self):
        return self.type

    def get_solve_visited(self):
        return self.solve_visited
    
    def set_solve_visited(self):
        self.solve_visited = True

    
    def __lt__(self, other):
        return (self.pos["x"], self.pos["y"]) < (other.pos["x"], other.pos["y"])