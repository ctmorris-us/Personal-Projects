#include <iostream>
#include "cube.h"
#include "LinkedList.h"
#include "List.h"
#include <vector>

void TestFoo(int * a){
  std::cout << a << std::endl;
}

void TestGoo(int & a){
  std::cout << a << std::endl;
}

int main() {

//Testing Arrays

int ArrayInt[5] = {1,2,3,4,5};
std::cout << ArrayInt[0] << std::endl;

// Calculate Offset between values in Array
std::cout << "Size of int" << sizeof(int) << std::endl;
int Offset =  (long) & (ArrayInt[2]) - (long) & (ArrayInt[0]) ;
std::cout << "Size of offset" << Offset << std::endl;
std::cout << "With long " << (long) & (ArrayInt[2]) << std::endl;
std::cout << "Without long " <<  & (ArrayInt[2]) << std::endl;

Cube CubeArray[3] = {Cube(2), Cube(3), Cube(4)};
std::cout << "size of cube " << sizeof(Cube) << std::endl;
int CubeOffset = (long) & (CubeArray[1]) - (long) & (CubeArray[0]);

std::vector<Cube> cubeVector{Cube(1), Cube(2), Cube(3)};
std::cout << "Capacity" << cubeVector.capacity() << std::endl;
std::cout << "Size" << cubeVector.size() << std::endl;
cubeVector.push_back(Cube(4));
std::cout << "Capacity after push" << cubeVector.capacity() << std::endl;
std::cout << "Size after push" << cubeVector.size() << std::endl;

std::cout << "Cube whatever" << cubeVector[1].getVolume() << std::endl;
if (cubeVector[1] == Cube(2)) {
  std::cout << "Test is found cube" << std::endl;
}

std::cout<<"Test Function Input"<<std::endl;
int tempb = 3;
int * tempa = &tempb;
TestFoo(tempa);

std::cout<<"Test Function Input Again"<<std::endl;
TestGoo(tempb);

// Cube TargetCube = Cube(2);
// for (unsigned i = 0; i < cubeVector.size(); i++ ){
//   if (cubeVector[i] == TargetCube) {
//     std::cout << "Found Cube" << std::endl;
//   }
// }
const int itema = 9;
const int itemb = 3;
LinkedList<int> TestLinkedListInt;
List<int> TestListInt;

TestListInt.insertAtFront(itema);
TestListInt.insertAtFront(itemb);
std::cout << TestListInt[0] << TestListInt[1] << std::endl;
// TestLinkedListInt.insertAtFront(itema);
// std::cout << TestLinkedListInt[0] <<std::endl;
return 0;
}
