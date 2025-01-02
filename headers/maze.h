#ifndef MAZE_H
#define MAZE_H

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <random>
#include <unistd.h>
#include "list.h"
#include "graphics.h"

using namespace std;

enum direction
{
    up = 1,
    down = 2,
    left_ = 3,
    right_ = 4
};


// Node *head = nullptr;

class maze
{
    int n;
    char **maze_pointer;

public:
    maze() : n(1)
    {
        maze_pointer = new char *[n];
        maze_pointer[0] = new char;
    }

    maze(int size)
    {
        n = size;
        maze_pointer = new char *[n];
        for (int i = 0; i < n; i++)
        {
            maze_pointer[i] = new char[n];
        }
    }

    ~maze()
    {
        for (int i = 0; i < n; i++)
        {
            delete[] maze_pointer[i];
        }
        delete[] maze_pointer;
    }

    void display()
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << setw(5) << maze_pointer[i][j];
            }
            cout << endl;
        }
    }

    void create_grid(LinkedList &visit)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                maze_pointer[i][j] = '*';
                visit.insert(i * n + j, i, j, false);
            }
        }
    }

    void neighbour_processing(int x, int y, LinkedList &visit, stack &store, bool visit_status,maze_creation &maze1)
    {
        if (x >= 0 && x < n && y >= 0 && y < n)
        {
            Node *temphead = visit.getHead();
            while (temphead)
            {
                if (temphead->position.x == x && temphead->position.y == y)

                {

                    if (temphead->position.visited == false)
                    {
                        store.push(x, y, visit_status);

                        maze_pointer[x][y] = '0';

                        temphead->position.visited = visit_status;

                        maze1.move_cell(x,y);
                    }
                }
                temphead = temphead->next;
            }
        }
    }

    void maze_generation(LinkedList &visit, stack &store,maze_creation &maze2)
    {
        int starting_i = 0, starting_j = 0;
        bool visit_status = true;
        store.push(starting_i, starting_j, visit_status);

        maze2.move_cell(0,0);

        while (!store.isEmpty())
        {

            Node *temp;
            temp = store.peek();
            store.pop();

            maze_pointer[temp->position.x][temp->position.y] = '0';

            int directions[4] = {up, down, left_, right_};
            shuffle(begin(directions), end(directions), default_random_engine());

            for (int dir : directions)
            {
                int x = temp->position.x;
                int y = temp->position.y;

                switch (dir)
                {
                case up:
                    x += 1;
                    // cout << "up" << endl;
                    break;
                case down:
                    // cout << "down" << endl;
                    x -= 1;
                    break;
                case left_:
                    // cout << "left" << endl;
                    y -= 1;
                    break;
                case right_:
                    // cout << "right" << endl;
                    y += 1;
                    break;
                }
                neighbour_processing(x, y, visit, store, visit_status,maze2);
            }
        }
    }
};
#endif // MAZE_H