#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
using namespace std;
struct Node
{
	int data;
	Node* next;
	Node* prev;
};
/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev
   }
*/
Node* SortedInsert(Node *head,int data)
{
   Node* temp = head;
   
    
   Node* New = new Node;
   New->data = data;
   New->next = NULL;
   New->prev = NULL;
    
    // Complete this function
   // Do not write the main method. 
   if(head == NULL){
       
       
       head = New;
     
       return head;
       
   }


   if(head->data > data){
       New->next = head;
       head->prev = New;
       head = New;

       return head;
   }
   
   while(1){
       if(temp -> data > data){
           New->next = temp;
           New->prev = temp->prev;
           
           Node* s = temp->prev;
           temp->prev = New;
           s->next = New;
           
           return head;        
       }
       
       if(temp->next == NULL){
           New->prev = temp;
           temp->next = New;
           break;
       }
       temp = temp->next;
   }    
   return head; 
}

void Print(Node *head) {
	if(head == NULL) return;
	while(head->next != NULL){ cout<<head->data<<" "; head = head->next;}
	cout<<head->data<<" ";
	while(head->prev != NULL) { cout<<head->data<<" "; head = head->prev; }
	cout<<head->data<<"\n";
}
int main()
{
	int t; cin>>t;
	Node *head = NULL;
	while(t--) {
	   int n; cin>>n;
           head = NULL;
	   for(int i = 0;i<n;i++) {
		   int x; cin>>x;
		   head = SortedInsert(head,x);
	       Print(head);
	   }
	}
}
