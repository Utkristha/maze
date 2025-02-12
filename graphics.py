# from cell import *
import pygame
import os

class maze_creation:

    def __init__(self,row,grid):
        pygame.init()
        self.width = 700
        self.rows = row
        self.screen = pygame.display.set_mode((700,700))
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid = grid
        self.size = self.width / self.rows
        self.screen.fill("white")
        self.user_text = ''
        self.base_font = pygame.font.Font(None,32)
        self.start_pos = None
        self.end_pos = None

    


    def start_screen(self):
        pygame.init()
        self.screen.fill("white")
        
        font = pygame.font.Font(None, 50)
        input_font = pygame.font.Font(None, 40)

        input_box_width, input_box_height = 200, 50
        input_box = pygame.Rect((self.width - input_box_width) // 2, (700 - input_box_height) // 2, input_box_width, input_box_height)

        color_active = pygame.Color("dodgerblue2")
        color_passive = pygame.Color("gray")
        color = color_passive
        active = False
        user_text = ""

        running = True
        while running:
            self.screen.fill((255, 255, 255))

            prompt_text = font.render("Enter Maze Size: ", True, (0, 0, 0))
            self.screen.blit(prompt_text, (220, 290))

            pygame.draw.rect(self.screen, color, input_box, 2)

            text_surface = input_font.render(user_text, True, (0, 0, 0))
            self.screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                        color = color_active
                    else:
                        active = False
                        color = color_passive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if user_text.isdigit() and int(user_text) > 0:
                                return int(user_text)
                            else:
                                user_text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode



    def grid_maker(self):

        pygame.draw.line(self.screen,"black",(700,0),(700,self.screen.get_width()),4)
        offset = 2

        for i in range(0,self.rows):
            for j in range(0,self.rows):

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running  = False
                        return

                coord = self.grid[i][j].get_pos()

                if (self.grid[i][j].get_wall_status()["right"]):
                    pygame.draw.line(self.screen,"black",((coord["x"]+1) * self.size,coord["y"] * self.size),
                                        ((coord["x"]+1)*self.size,(coord["y"]+1)*self.size))
                    
                if (self.grid[i][j].get_wall_status()["left"]):
                    pygame.draw.line(self.screen,"black",((coord["x"]) * self.size,coord["y"] * self.size),
                                        ((coord["x"])*self.size,(coord["y"]+1)*self.size))
                    
                if (self.grid[i][j].get_wall_status()["up"]):
                    pygame.draw.line(self.screen,"black",((coord["x"]) * self.size,coord["y"] * self.size),
                                        ((coord["x"]+1)*self.size,(coord["y"])*self.size))
                    
                if (self.grid[i][j].get_wall_status()["down"]):
                    pygame.draw.line(self.screen,"black",((coord["x"]) * self.size,(coord["y"]+1) * self.size),
                                        ((coord["x"]+1)*self.size,(coord["y"]+1)*self.size))
                    
                pygame.display.update()
                # pygame.time.delay(500)


        mouse_pressed = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        x = int(mouse[0] / self.size)
        y = int(mouse[1] / self.size)
        if(mouse[0] < 700):
            if(mouse_pressed[0] == True):
                pygame.draw.rect(self.screen, "green",
                    (int(x * self.size) , int(y * self.size) ,
                    int(self.size), int(self.size) ))
                self.grid[x][y].set_type("start",True) 
                self.start_pos = (x, y)
                if self.grid[x][y].get_type()["end"] == True:
                    self.grid[x][y].set_type("end",False)

            elif(mouse_pressed[2] == True):
                pygame.draw.rect(self.screen, "red",
                    (int(x * self.size), int(y * self.size),
                    int(self.size), int(self.size)))
                self.grid[x][y].set_type("end",True)
                self.end_pos = (x, y)
                if self.grid[x][y].get_type()["start"] == True:
                    self.grid[x][y].set_type("start",False)
            if(mouse_pressed[1] == True):
                
                for i in range(self.rows):
                    for j in range(self.rows):
                        self.grid[i][j].set_type("start", False)
                        self.grid[i][j].set_type("end", False)
                        self.grid[i][j].visited = False
                        self.grid[i][j].solve_visited = False

                self.start_pos = None
                self.end_pos = None
                
                self.screen.fill("white")
                self.grid_maker()
                
                pygame.display.update()
                pygame.time.delay(200)

        
        pygame.display.update()



    def grid_per_cell(self, cell):

        pygame.draw.line(self.screen,"black",(700,0),(700,self.screen.get_width()),4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        coord = cell.get_pos()
        walls = cell.get_wall_status()

        # print(f"{cell.get_pos()} = {cell.get_wall_status()} ->")
        offset = 2  # Shrink the rectangle slightly

        # Draw the rectangle with the offset
        pygame.draw.rect(self.screen, "blue",
            (int(coord["x"] * self.size) + offset, int(coord["y"] * self.size) + offset,
            int(self.size) - 2 * offset, int(self.size) - 2 * offset))

        if walls["right"]:
            pygame.draw.line(self.screen, "black",
                            ((coord["x"] + 1) * self.size, coord["y"] * self.size),
                            ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))

        if walls["left"]:
            pygame.draw.line(self.screen, "black",
                            (coord["x"] * self.size, coord["y"] * self.size),
                            (coord["x"] * self.size, (coord["y"] + 1) * self.size))

        if walls["up"]:
            pygame.draw.line(self.screen, "black",
                            (coord["x"] * self.size, coord["y"] * self.size),
                            ((coord["x"] + 1) * self.size, coord["y"] * self.size))

        if walls["down"]:
            pygame.draw.line(self.screen, "black",
                            (coord["x"] * self.size, (coord["y"] + 1) * self.size),
                            ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))

        # Adjust for missing walls (not condition)
        if not walls["right"]:
            pygame.draw.line(self.screen, "white",
                            ((coord["x"] + 1) * self.size, coord["y"] * self.size),
                            ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))

        if not walls["left"]:
            pygame.draw.line(self.screen, "white",
                            (coord["x"] * self.size, coord["y"] * self.size),
                            (coord["x"] * self.size, (coord["y"] + 1) * self.size))

        if not walls["up"]:
            pygame.draw.line(self.screen, "white",
                            (coord["x"] * self.size, coord["y"] * self.size),
                            ((coord["x"] + 1) * self.size, coord["y"] * self.size))

        if not walls["down"]:
            pygame.draw.line(self.screen, "white",
                            (coord["x"] * self.size, (coord["y"] + 1) * self.size),
                            ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))

        pygame.display.update()

        # Draw the rectangle again after updating walls
        pygame.draw.rect(self.screen, "white",
            (int(coord["x"] * self.size) + offset, int(coord["y"] * self.size) + offset,
            int(self.size) - 2 * offset, int(self.size) - 2 * offset))

        # pygame.time.delay(100)

        self.clock.tick(60)


    def solve_mage_display(self,solved_path):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        offset = 2 
        for i in range(0,len(solved_path)):
            cell = solved_path[i]
            coord = cell.get_pos()
            walls = cell.get_wall_status()
            # print(cell_pos)


            if cell.get_type()["start"]:
                color = "green"
            elif cell.get_type()["end"]:
                color = "red"
            else:
                color = "purple" 

            pygame.draw.rect(self.screen, color,
                (int(coord["x"] * self.size), int(coord["y"] * self.size),
                self.size, self.size ))

            if walls["right"]:
                pygame.draw.line(self.screen, "black",
                                ((coord["x"] + 1) * self.size, coord["y"] * self.size),
                                ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))

            if walls["left"]:
                pygame.draw.line(self.screen, "black",
                                (coord["x"] * self.size, coord["y"] * self.size),
                                (coord["x"] * self.size, (coord["y"] + 1) * self.size))

            if walls["up"]:
                pygame.draw.line(self.screen, "black",
                                (coord["x"] * self.size, coord["y"] * self.size),
                                ((coord["x"] + 1) * self.size, coord["y"] * self.size))

            if walls["down"]:
                pygame.draw.line(self.screen, "black",
                                (coord["x"] * self.size, (coord["y"] + 1) * self.size),
                                ((coord["x"] + 1) * self.size, (coord["y"] + 1) * self.size))
            
            pygame.display.flip()   
                 
            # pygame.time.delay(50)
            self.clock.tick(6000)
            # print("nice")
