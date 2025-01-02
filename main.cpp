#include <iostream>
#include <iomanip>
#include <algorithm>
#include <random>
#include <unistd.h>
#include "headers\list.h"
#include "headers\maze.h"
using namespace std;

#include <SDL2/SDL.h>

// class maze_creation
// {
//     const int grid_size = 50;
//     const int rows = 10;
//     const int columns = 10;

//     int window_height = 500;
//     int window_width = 500;

//     SDL_Renderer *renderer = NULL;
//     SDL_Window *window = NULL;
//     SDL_Event window_event;

// public:
//     int create_windows()
//     {

//         if (SDL_Init(SDL_INIT_EVERYTHING) < 0)
//         {
//             cout << "Error: " << SDL_GetError << endl;
//             return -1;
//         }

//         window = SDL_CreateWindow("new", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, window_width, window_height, 0);

//         if (!window)
//         {
//             cout << "Error creating window: " << SDL_GetError() << endl;
//             return -1;
//         }

//         renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

//         if (!renderer)
//         {
//             cout << "Failed to create renderer: " << SDL_GetError() << endl;
//             return -1;
//         }

//         return 0;
//     }

//     void draw_grid()
//     {

//         SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
//         SDL_RenderClear(renderer);

//         SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);

//         for (int i = 0; i < rows; i++)
//         {
//             SDL_RenderDrawLine(renderer, 0, i * grid_size, columns * grid_size, i * grid_size);
//         }

//         for (int i = 0; i < columns; i++)
//         {
//             SDL_RenderDrawLine(renderer, i * grid_size, 0, i * grid_size, rows * grid_size);
//         }

//         SDL_RenderPresent(renderer);
//     }

//     void run_window()
//     {
//         while (true)
//         {
//             if (SDL_PollEvent(&window_event))
//             {
//                 if (SDL_QUIT == window_event.type)
//                 {
//                     break;
//                 }
//             }
//         }
//     }

//     void delete_window()
//     {
//         SDL_DestroyWindow(window);

//         SDL_Quit();
//     }

//     void move_cell(LinkedList &visit)
//     {
//         int i = 0;
//         int j = 0;
//         // for (int i = 0; i < 10; i++)
//         // {
//         //     for(int j = 0; j< 10;j++)
//         //     {

//         //         SDL_Rect cell = {i * grid_size, j * grid_size, grid_size, grid_size};

//         //         if (i % 2 == 0)
//         //         {
//         //             SDL_SetRenderDrawColor(renderer, 160, 200, 0, 255);

//         //             SDL_RenderFillRect(renderer, &cell);

//         //             SDL_RenderPresent(renderer);
//         //         }
//         //         else
//         //         {
//         //             SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);

//         //             SDL_RenderFillRect(renderer, &cell);

//         //             SDL_RenderPresent(renderer);
//         //         }

//         //         sleep(1);
//         //     }
//         // }
//         Node *temp = visit.getHead();
//         while (temp->next != nullptr)
//         {
//             SDL_Rect cell = {temp->position.x * grid_size, temp->position.y * grid_size, grid_size, grid_size};

//             SDL_SetRenderDrawColor(renderer, 160, 200, 0, 255);

//             SDL_RenderFillRect(renderer, &cell);

//             SDL_RenderPresent(renderer);

//             temp = temp->next;
//             sleep(1);
//         }
//     }
// };

int main(int argc, char **args)
{
    LinkedList visited;
    stack stack_input;
    
    maze_creation maze1;

    maze1.create_windows();
    maze1.draw_grid();
    
    // maze1.move_cell(4,3);
    // maze1.move_cell(3,2);
    // maze1.move_cell(2,2);
    // maze1.move_cell(1,3);
    // maze1.move_cell(1,4);
    // maze1.move_cell(2,5);
    // maze1.move_cell(3,6);
    // maze1.move_cell(4,7);
    // maze1.move_cell(5,6);
    // maze1.move_cell(6,5);
    // maze1.move_cell(7,4);
    // maze1.move_cell(7,3);
    // maze1.move_cell(6,2);
    // maze1.move_cell(5,2);










    maze m1(10);
    m1.create_grid(visited);
    m1.display();
    m1.maze_generation(visited, stack_input,maze1);
    cout << endl;
    m1.display();
    visited.display();
    cout << endl;



    maze1.run_window();
    maze1.delete_window();

    return 0;
}