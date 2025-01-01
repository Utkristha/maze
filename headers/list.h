#ifndef LIST_H
#define LIST_H

#include <iostream>
using namespace std;


// enum direction
// {
//     up = 1,
//     down = 2,
//     left_ = 3,
//     right_ = 4
// };

class Node
{
    public:

    struct cooridnate{
        int x;
        int y;
        bool visited;
    }position;

    Node *next;

    Node(int x_=0,int y_=0,bool status = false)
    {
        this->position.x = x_;
        this->position.y = y_;
        this->position.visited = status;
        this->next = nullptr;
    }
};

class LinkedList
{

    Node *head;
    int node_counter = 0;

    public:

    LinkedList()  
    {
        head = nullptr;
    } 

    ~LinkedList() 
    {
        Node* current = head;
        while (current) 
        {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
    Node* getHead()
    {
        return head;
    }
    void insert(int position=0,int x_=0,int y_=0,bool status = false)
    {
        Node *newnode = new Node;
        newnode->position.x = x_;
        newnode->position.y = y_;
        newnode->position.visited = status;
        
        if(position == 0)
        {
            if(head == nullptr)
            {
                head = newnode;
                newnode->next = nullptr;
            }
            else
            {
                newnode->next = head;
                head = newnode;
            }
            node_counter++;
        }
        else
        {
            Node *temp=head;
            for(int i=0;i<position-1 && temp!= nullptr ;i++)
            {
                temp = temp->next;
            }

            if(temp == nullptr)
            {
                newnode->next = temp->next;
                temp->next = newnode;
            }

            newnode->next = temp->next;
            temp->next = newnode;
            node_counter++;
        }
    }

    void display()
    {
        Node *temp;
        temp = head;
        while(temp != nullptr)
        {
            cout<<"("<<temp->position.x<<","<<temp->position.y<<"):"<<temp->position.visited<<"->";
            temp = temp->next;
            
        }
        cout<<"nullptr"<<endl;
    }

    int number_of_nodes()
    {
       return node_counter; 
    }

    void remove(int position)
{
    if (head == nullptr) 
    {
        cout << "List is empty!" << endl;
        return;
    }


    if (position == 0)
    {
        Node* temp = head;
        head = head->next;  
        delete temp;        
    } 
    else 
    {
        Node* temp = head;
        for (int i = 0; i < position - 1 && temp != nullptr; i++) 
        {
            temp = temp->next;
        }

        if (temp != nullptr && temp->next != nullptr) 
        {
            Node* toDelete = temp->next;
            temp->next = temp->next->next; 
            delete toDelete;               
        } 
        else 
        {
            cout << "Position out of range!" << endl;
        }
    }
    node_counter--;
}
};

class stack
{
    LinkedList l1;
    public:
    bool isEmpty()
    {
        return l1.getHead() == nullptr;
    }
    void push(int x_=0,int y_ = 0,bool status = false)
    {
        l1.insert(0,x_,y_,status);
    }
    void pop()
    {
        l1.remove(0);
    }
    Node* peek()
    {
        return l1.getHead();
    }
    void view()
    {
        l1.display();
    }
};

    


// class maze
// {
//     int n;
//     char **maze_pointer;

// public:
//     maze() : n(1)
//     {
//         maze_pointer = new char *[n];
//         maze_pointer[0] = new char;
//     }

//     maze(int size)
//     {
//         n = size;
//         maze_pointer = new char *[n];
//         for (int i = 0; i < n; i++)
//         {
//             maze_pointer[i] = new char[n];
//         }
//     }

//     ~maze()
//     {
//         for (int i = 0; i < n; i++)
//         {
//             delete[] maze_pointer[i];
//         }
//         delete[] maze_pointer;
//     }

//     void display()
//     {
//         for (int i = 0; i < n; i++)
//         {
//             for (int j = 0; j < n; j++)
//             {
//                 cout << setw(5) << maze_pointer[i][j];
//             }
//             cout << endl;
//         }
//     }

//     void create_grid(LinkedList &visit)
//     {
//         for (int i = 0; i < n; i++)
//         {
//             for (int j = 0; j < n; j++)
//             {
//                 maze_pointer[i][j] = '*';
//                 visit.insert(i * n + j, i, j, false);
//             }
//         }
//     }

//     void neighbour_processing(int x, int y, LinkedList &visit, stack &store, bool visit_status)
//     {
//         if (x >= 0 && x < n && y >= 0 && y < n)
//         {
//             Node *temphead = visit.getHead();
//             while (temphead)
//             {
//                 if (temphead->position.x == x && temphead->position.y == y)

//                 {

//                     if (temphead->position.visited == false)
//                     {
//                         store.push(x, y, visit_status);

//                         maze_pointer[x][y] = '0';

//                         temphead->position.visited = visit_status;
//                     }
//                 }
//                 temphead = temphead->next;
//             }
//         }
//     }

//     void maze_generation(LinkedList &visit, stack &store)
//     {
//         int starting_i = 0, starting_j = 0;
//         bool visit_status = true;
//         store.push(starting_i, starting_j, visit_status);

//         while (!store.isEmpty())
//         {

//             Node *temp;
//             temp = store.peek();
//             store.pop();

//             maze_pointer[temp->position.x][temp->position.y] = '0';

//             int directions[4] = {up, down, left_, right_};
//             shuffle(begin(directions), end(directions), default_random_engine());

//             for (int dir : directions)
//             {
//                 int x = temp->position.x;
//                 int y = temp->position.y;

//                 switch (dir)
//                 {
//                 case up:
//                     x += 1;
//                     // cout << "up" << endl;
//                     break;
//                 case down:
//                     // cout << "down" << endl;
//                     x -= 1;
//                     break;
//                 case left_:
//                     // cout << "left" << endl;
//                     y -= 1;
//                     break;
//                 case right_:
//                     // cout << "right" << endl;
//                     y += 1;
//                     break;
//                 }
//                 neighbour_processing(x, y, visit, store, visit_status);
//             }
//         }
//     }
// };


#endif // LIST_H