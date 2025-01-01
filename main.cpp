#include <iostream>
#include <iomanip>
#include <algorithm>
#include <random>
#include <unistd.h>
#include "headers\list.h"
#include "headers\maze.h"

#include <SDL2/SDL.h>

using namespace std;

const int grid_size = 50;
const int rows = 10;
const int column = 10;

int main(int argc, char **args)
{
    // LinkedList visited;
    // stack stack_input;
    // maze m1(2);
    // m1.create_grid(visited);
    // m1.display();
    // m1.maze_generation(visited, stack_input);
    // cout << endl;
    // m1.display();
    // visited.display();
    // cout << endl;

    SDL_Renderer *renderer = NULL;
    SDL_Window *window = NULL;
    SDL_Event window_event;

    if (SDL_Init(SDL_INIT_EVERYTHING) < 0)
    {
        cout << "Error: " << SDL_GetError << endl;
        return -1;
    }

    window = SDL_CreateWindow("new", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 500, 500, 0);

    if (!window)
    {
        cout << "Error creating window: " << SDL_GetError() << endl;
        return -1;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    if (!renderer)
    {
        cout << "Failed to create renderer: " << SDL_GetError() << endl;
    }

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderClear(renderer);

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);

    for(int i=0;i<rows;i++)
    {
        SDL_RenderDrawLine(renderer,0,i * grid_size,column * grid_size,i * grid_size);
    }

    for(int i=0;i<column;i++)
    {
        SDL_RenderDrawLine(renderer,i*grid_size,0,i*grid_size,rows*grid_size);
    }

    SDL_RenderPresent(renderer);
    
    while (true)
    {
        if (SDL_PollEvent(&window_event))
        {
            if (SDL_QUIT == window_event.type)
            {
                break;
            }
        }
    }

    SDL_DestroyWindow(window);

    SDL_Quit();

    return 0;
}