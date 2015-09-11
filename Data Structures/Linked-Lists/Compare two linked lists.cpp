#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
struct Node
{
	int data;
	Node *next;
};
int CompareLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method
  Node *tempA = new Node;
  Node *tempB = new Node;  
  
  tempA = headA;
  tempB = headB;
  
  bool flag = true;
  
  while(tempA != NULL && tempB != NULL){
      if (tempA->data != tempB->data){
          flag = false;
          break;
      }
      else{
          tempA = tempA->next;
          tempB = tempB->next;
      }
  }
  if ((tempA == NULL && tempB != NULL) || (tempB == NULL && tempA != NULL)){
      flag = false;
  }
    
 
  if(flag == true){
      return 1;
  } else {
      return 0;
  }  
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
		cout<<CompareLists(A,B)<<"\n";
	}
}
