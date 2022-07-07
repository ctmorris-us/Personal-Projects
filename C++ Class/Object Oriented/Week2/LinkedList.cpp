#include "LinkedList.h"

template <typename T>
const T & LinkedList<T>::operator[] (unsigned index){
  ListNode * head = head_;

  while(index > 0 && head -> Next != nullptr) {
    head = head -> Next;
    index --;
  }
  return head->Data;
}

template <typename T>
void LinkedList<T>::insertAtFront(const T & data){
  ListNode * newNode = new ListNode(data);
  newNode->Next = head_;
  head_ = newNode;
}
