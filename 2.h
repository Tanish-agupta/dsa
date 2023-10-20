#ifndef BIGINTEGER_H
#define BIGINTEGER_H



struct node {
    int data;
    struct node *next;
};


struct node* createnode(int data);
void insertAtFront(struct node** head, int data);
void insertatend(struct node** head, int data);
struct node* addBigIntegers(struct node* num1, struct node* num2);
void print(struct node* node);
void freeList(struct node* head);
struct node* subtractBigIntegers(struct node* num1, struct node* num2);
void  divideNumbers(char input[], int divisor);

#endif
