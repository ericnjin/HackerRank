/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method
  Node* prev = NULL;
  Node* next = NULL;
  Node* temp = head;
    
  while(temp!=NULL){
      next = temp->next;
      temp->next=prev;
      prev = temp;
      temp = next;
  }  
  return prev;
}
