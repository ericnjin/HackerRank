#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
using namespace std;
struct Node
{
	int data;
	Node* next;
};
/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method.
    Node* temp1 = headA;
    Node* temp2 = headB;
    
    while(temp1 != NULL){
        while(temp2 != NULL){
            if(temp1 == temp2){
                return temp1->data;
            }
            temp2 = temp2->next;
        }
        temp2 = headB;
        temp1 = temp1->next;
    }
    return 1;
}

int main()
{
	Node *A, *B, *C, *D,*E,*F,*G;
	A = new Node();	B= new Node();  C= new Node(); D = new Node(); E = new Node(); F= new Node();G = new Node();
	A->data = 2; B->data = 4; C->data = 3; D->data = 5; E->data = 7; F->data = 6;G->data = 11;

	// case 1 = 
	A->next = B; B->next = C; C->next = D; D->next = E; E->next = NULL;
	F->next = G; G->next = C;
	cout<<FindMergeNode(A,F)<<"\n";
	//case 2.
	A->next = B; B->next = C; C->next = E;  E->next = NULL;
	F->next = G; G->next = D;D->next = C;
	cout<<FindMergeNode(A,F)<<"\n";
	//case 3:
	A->next = B; B->next = E; E->next = NULL;
	F->next = G; G->next = D;D->next = C; C->next = E;
	cout<<FindMergeNode(A,F)<<"\n";
}
