#pragma once

template <typename T>
class LinkedList{
public:
  const T & operator[] (unsigned index);
  void insertAtFront(const T & data);
  LinkedList() : head_(nullptr) { }
private:
  class ListNode{
  public:
    const T & Data;
    ListNode * Next;
    ListNode(const T & data) : Data(data), Next(nullptr) {}
  };
  ListNode * head_;
};
