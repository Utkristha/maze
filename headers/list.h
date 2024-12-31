#include <iostream>
using namespace std;
int ZERO = 0;

class Node
{
    public:

    struct cooridnate{
        int x;
        int y;
    }position;

    Node *next;

    Node(int x_=0,int y_=0)
    {
        this->position.x = x_;
        this->position.y = y_;
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

    void insert(int position=0,int x_=0,int y_=0)
    {
        Node *newnode = new Node;
        newnode->position.x = x_;
        newnode->position.y = y_;
        
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
            cout<<"("<<temp->position.x<<","<<temp->position.y<<")"<<"->";
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

    // Handle case when the position to remove is the head node
    if (position == 0)
    {
        Node* temp = head;
        head = head->next;  // Move head to the next node
        delete temp;        // Delete the old head
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
            temp->next = temp->next->next; // Unlink the node to delete
            delete toDelete;               // Delete the node
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
    void push(int x_=0,int y_ = 0)
    {
        l1.insert(ZERO,x_,y_);
    }
    void pop()
    {
        l1.remove(ZERO);
    }
    void view()
    {
        l1.display();
    }
};

    