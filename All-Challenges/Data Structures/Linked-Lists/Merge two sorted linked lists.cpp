#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
struct Node
{
	int data;
	Node *next;
};
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
  if(headA == NULL){
      return headB;
  }  else if(headB == NULL){
      return headA;
  } else{
      Node* head = NULL;
      Node* temp = new Node;
      
      while(headA!=NULL && headB!=NULL){
          if(headA->data < headB->data){
              if(head == NULL){
                  head = headA;
                  temp = head;
                  
                  headA = headA->next;
              } else {
                  temp->next = headA;
                  temp = headA;
                  
                  headA = headA->next;
              }
          }
          else{
              if(head == NULL){
                  head = headB;
                  temp = head;
                  
                  headB = headB->next;
              } else {
                  temp->next = headB;
                  temp = headB;
                  headB = headB->next;
              }
          }
      }
      if(headA == NULL && headB == NULL){
          temp = NULL;
      } else if(headA == NULL){
          temp->next = headB;
          temp = headB;
      } else {
          temp->next = headA;
          temp = headA;
      }
      return head;
  }
  
}
void Print(Node *head)
{
	bool ok = false;
	while(head != NULL)
	{
		if(ok)cout<<" ";
		else ok = true;
		cout<<head->data;
		head = head->next;
	}
        cout<<"\n";
}
Node* Insert(Node *head,int x)
{
   Node *temp = new Node();
   temp->data = x;
   temp->next = NULL;
   if(head == NULL) 
   {
       return temp;
   }
   Node *temp1;
   for(temp1 = head;temp1->next!=NULL;temp1= temp1->next);
   temp1->next = temp;return head;
}
int main()
{
	int t;
	cin>>t;
	while(t-- >0)
	{
		Node *A = NULL;
		Node *B = NULL;
		int m;cin>>m;
		while(m--){
			int x; cin>>x;
			A = Insert(A,x);}
		int n; cin>>n;
        while(n--){
			int y;cin>>y;
			B = Insert(B,y);
		}
		A = MergeLists(A,B);
		Print(A);
	}
}
