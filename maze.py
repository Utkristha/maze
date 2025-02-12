from cell import *
from graphics import * 
import heapq
import random


class maze_algo:
    def __init__(self,size,starting=0,ending=0):
        self.size = size
        self.starting = starting
        self.ending = ending
        self.grid = [[cell(i,j) for j in range(0,size)] for i in range(0,size)]
        self.stack = []
        self.display = maze_creation(size,self.grid[0][0])


    def maze_generation(self):
        current_cell = self.grid[0][0]
        current_cell.set_visited()


        self.stack.append(current_cell)

        

        while (self.stack):
            current_cell = self.stack.pop()


            neighbors = self.unvisited_neighbors(current_cell)

            if(neighbors):
                self.stack.append(current_cell)

                chosen = self.get_cell(neighbors)

                chosen.set_visited()

                self.remove_wall(current_cell,chosen)

                self.stack.append(chosen)

            # self.display.grid_per_cell(current_cell)

            


    def remove_wall(self,current_cell,neighbor_cell):

        current_cell_pos = current_cell.get_pos()
        neighbor_cell_pos = neighbor_cell.get_pos()


        delta_x = current_cell_pos["x"] - neighbor_cell_pos["x"]
        delta_y = current_cell_pos["y"] - neighbor_cell_pos["y"]
        if (delta_x < 0 ):
            self.grid[current_cell_pos["x"]][current_cell_pos["y"]].set_wall_status("right")
            self.grid[neighbor_cell_pos["x"]][neighbor_cell_pos["y"]].set_wall_status("left")
        if (delta_x > 0 ):
            self.grid[current_cell_pos["x"]][current_cell_pos["y"]].set_wall_status("left")
            self.grid[neighbor_cell_pos["x"]][neighbor_cell_pos["y"]].set_wall_status("right")
        if (delta_y < 0 ):
            self.grid[current_cell_pos["x"]][current_cell_pos["y"]].set_wall_status("down")
            self.grid[neighbor_cell_pos["x"]][neighbor_cell_pos["y"]].set_wall_status("up")
        if (delta_y > 0 ):
            self.grid[current_cell_pos["x"]][current_cell_pos["y"]].set_wall_status("up")
            self.grid[neighbor_cell_pos["x"]][neighbor_cell_pos["y"]].set_wall_status("down")

    
    def get_cell(self,neighbors):
        num = len(neighbors)
        rand_place = random.randint(0,num-1)
        return neighbors[rand_place]
        

    def unvisited_neighbors(self,current_cell):
        neighbors = []

        pos = current_cell.get_pos()
        pos_x = pos["x"]
        pos_y = pos["y"]

        if (pos_x >0 and not self.grid[pos_x-1][pos_y].get_visited()):
            neighbors.append(self.grid[pos_x-1][pos_y])

        if (pos_x <self.size-1 and not self.grid[pos_x+1][pos_y].get_visited()):
            neighbors.append(self.grid[pos_x+1][pos_y])

        if (pos_y >0 and not self.grid[pos_x][pos_y-1].get_visited()):
            neighbors.append(self.grid[pos_x][pos_y-1])

        if (pos_y <self.size -1 and not self.grid[pos_x][pos_y+1].get_visited()):
            neighbors.append(self.grid[pos_x][pos_y+1])

        return neighbors
    
    def view_cells(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                print(f"cell[{i}][{j}] = {self.grid[i][j].get_wall_status()}")
    
    def get_grid(self):
        return self.grid
    


    def solve_maze(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        # Mark the end cell
        self.grid[end_x][end_y].set_type("end", True)

        # Initialize the stack with the start cell and its path
        visited_cell = []
        visited_cell.append((self.grid[start_x][start_y], [self.grid[start_x][start_y]]))

        # Dictionary to keep track of parent cells for path reconstruction
        parent = {}

        # Flag to indicate if the end cell has been found
        end_found = False

        while visited_cell:
            current_cell, current_path = visited_cell.pop()
            current_cell.set_solve_visited()

            # If the end cell is found, break out of the loop
            if current_cell.get_type()["end"]:
                end_found = True
                break

            # Explore neighbors
            current_cell_pos = current_cell.get_pos()
            wall_status = current_cell.get_wall_status()

            # Left neighbor
            if wall_status["left"] == 0 and not self.grid[current_cell_pos["x"] - 1][current_cell_pos["y"]].get_solve_visited():
                neighbor = self.grid[current_cell_pos["x"] - 1][current_cell_pos["y"]]
                visited_cell.append((neighbor, current_path + [neighbor]))
                parent[neighbor] = current_cell

            # Right neighbor
            if wall_status["right"] == 0 and not self.grid[current_cell_pos["x"] + 1][current_cell_pos["y"]].get_solve_visited():
                neighbor = self.grid[current_cell_pos["x"] + 1][current_cell_pos["y"]]
                visited_cell.append((neighbor, current_path + [neighbor]))
                parent[neighbor] = current_cell

            # Up neighbor
            if wall_status["up"] == 0 and not self.grid[current_cell_pos["x"]][current_cell_pos["y"] - 1].get_solve_visited():
                neighbor = self.grid[current_cell_pos["x"]][current_cell_pos["y"] - 1]
                visited_cell.append((neighbor, current_path + [neighbor]))
                parent[neighbor] = current_cell

            # Down neighbor
            if wall_status["down"] == 0 and not self.grid[current_cell_pos["x"]][current_cell_pos["y"] + 1].get_solve_visited():
                neighbor = self.grid[current_cell_pos["x"]][current_cell_pos["y"] + 1]
                visited_cell.append((neighbor, current_path + [neighbor]))
                parent[neighbor] = current_cell

        # Reconstruct the path if the end cell was found
        if end_found:
            path = []
            cell = current_cell
            while cell in parent:
                path.append(cell)
                cell = parent[cell]
            path.append(self.grid[start_x][start_y])  # Add the start cell
            path.reverse()  # Reverse to get the path from start to end

            # Display the solved path
            self.display.solve_mage_display(path)

        

# Example usage:
# solved_path = self.solve_maze()
# self.display.solve_mage_display(solved_path)

    # copied from chat gpt to see how it looks compared to my dfs 
    # want to implement it myself someday


    
    # ###########################################################
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    # ########################################################### 
    #  



    # def solve_maze_dijkstra(self, starting=(0, 0), ending=None):
    #     if ending is None:
    #         ending = (self.size - 1, self.size - 1)
        
    #     start_cell = self.grid[starting[0]][starting[1]]
    #     end_cell = self.grid[ending[0]][ending[1]]
        
    #     pq = []
    #     heapq.heappush(pq, (0, start_cell))  # (distance, cell)
        
    #     # Distance dictionary
    #     dist = {cell: float('inf') for row in self.grid for cell in row}
    #     dist[start_cell] = 0
        
    #     # Parent dictionary for path reconstruction
    #     parent = {}

    #     processed = set()
        
    #     while pq:
    #         current_dist, current_cell = heapq.heappop(pq)
            
    #         if current_cell == end_cell:
    #             break

    #         if current_cell in processed:
    #             continue


    #         processed.add(current_cell)
            
    #         current_pos = current_cell.get_pos()
    #         neighbors = self.get_reachable_neighbors(current_cell)
            
    #         for neighbor in neighbors:
    #             new_dist = current_dist + 1  
    #             if new_dist < dist[neighbor]:
    #                 dist[neighbor] = new_dist
    #                 parent[neighbor] = current_cell
    #                 heapq.heappush(pq, (new_dist, neighbor))
        
        
    #     path = []
    #     cell = end_cell
    #     while cell in parent:
    #         path.append(cell)
    #         cell = parent[cell]
    #     path.append(start_cell)
    #     path.reverse()
        
        
    #     self.display.solve_mage_display(path)
        
    # def get_reachable_neighbors(self, current_cell):
    #     """Returns neighbors that are reachable (no walls in between)."""
    #     neighbors = []
    #     current_pos = current_cell.get_pos()
    #     wall_status = current_cell.get_wall_status()
        
    #     if wall_status['left'] == 0 and current_pos['x'] > 0:
    #         neighbors.append(self.grid[current_pos['x'] - 1][current_pos['y']])
    #     if wall_status['right'] == 0 and current_pos['x'] < self.size - 1:
    #         neighbors.append(self.grid[current_pos['x'] + 1][current_pos['y']])
    #     if wall_status['up'] == 0 and current_pos['y'] > 0:
    #         neighbors.append(self.grid[current_pos['x']][current_pos['y'] - 1])
    #     if wall_status['down'] == 0 and current_pos['y'] < self.size - 1:
    #         neighbors.append(self.grid[current_pos['x']][current_pos['y'] + 1])
        
    #     return neighbors


    # def solve_maze_a_star(self, starting=(0, 0), ending=None):
    #     if ending is None:
    #         ending = (self.size - 1, self.size - 1)
        
    #     start_cell = self.grid[starting[0]][starting[1]]
    #     end_cell = self.grid[ending[0]][ending[1]]
        
    #     # Priority queue stores (f(n), cell), where f(n) = g(n) + h(n)
    #     pq = []
    #     heapq.heappush(pq, (0, start_cell))  # (f(n), cell)
        
    #     # Distance dictionary for g(n) (actual distance)
    #     dist = {cell: float('inf') for row in self.grid for cell in row}
    #     dist[start_cell] = 0
        
    #     # Heuristic dictionary for h(n) (estimated distance to goal)
    #     heuristic = {cell: self.manhattan_distance(cell, end_cell) for row in self.grid for cell in row}
        
    #     # Parent dictionary for path reconstruction
    #     parent = {}
        
    #     # Set to track processed cells
    #     processed = set()
        
    #     while pq:
    #         current_f, current_cell = heapq.heappop(pq)
            
    #         # If the destination cell is reached, break early
    #         if current_cell == end_cell:
    #             break
            
    #         # Skip if the cell has already been processed
    #         if current_cell in processed:
    #             continue
            
    #         processed.add(current_cell)
            
    #         current_pos = current_cell.get_pos()
    #         neighbors = self.get_reachable_neighbors(current_cell)
            
    #         for neighbor in neighbors:
    #             # Skip already processed neighbors
    #             if neighbor in processed:
    #                 continue
                
    #             # Calculate g(n) and h(n) for this neighbor
    #             new_g = dist[current_cell] + 1  # Actual distance (g(n))
    #             new_h = heuristic[neighbor]  # Heuristic (h(n))
    #             new_f = new_g + new_h  # Total cost (f(n) = g(n) + h(n))
                
    #             # Update the distance and parent if this is a better path
    #             if new_g < dist[neighbor]:
    #                 dist[neighbor] = new_g
    #                 parent[neighbor] = current_cell
    #                 heapq.heappush(pq, (new_f, neighbor))
        
    #     # Reconstruct the path from the end to the start
    #     path = []
    #     cell = end_cell
    #     while cell in parent:
    #         path.append(cell)
    #         cell = parent[cell]
        
    #     # Add the start cell to the path
    #     path.append(start_cell)
    #     path.reverse()
        
    #     # Visualize the solved path
    #     self.display.solve_mage_display(path)

    # def manhattan_distance(self, cell, goal_cell):
    #     """Heuristic: Manhattan distance between two cells."""
    #     cell_pos = cell.get_pos()
    #     goal_pos = goal_cell.get_pos()
    #     return abs(cell_pos["x"] - goal_pos["x"]) + abs(cell_pos["y"] - goal_pos["y"])
