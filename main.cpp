#include <iostream>
#include <iomanip>
#include "headers\list.h"
using namespace std;

class Node;

// Node *head = nullptr;

class maze
{
    int n;
    char **maze_pointer;
    public:

    maze():n(1)
    {
        maze_pointer = new char*[n];
        maze_pointer[0] = new char;
    }    

    maze(int size)
    {
        n = size;
        maze_pointer = new char*[n];
        for(int i=0;i<n;i++)
        {
            maze_pointer[i] = new char;
        }
    }    

    ~maze()
    {
        for(int i=0;i<n;i++)
        {
            delete[] maze_pointer[i];
        }
        delete[] maze_pointer;
    }

    void display()
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cout<<setw(5)<<maze_pointer[i][j];
            }
            cout<<endl;
        }
    }

    void create_grid(stack &visit,stack &store)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {

                maze_pointer[i][j] = '*';
                visit.push(i,j);

            }
        }
    }
};

int main()
{
    stack visited,stack_input;
    maze m1(5);
    m1.create_grid(visited,stack_input);
    m1.display();
    visited.view();
    return 0;

}