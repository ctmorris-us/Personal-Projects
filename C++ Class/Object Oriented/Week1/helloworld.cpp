#include <iostream>
#include "cube.h"
#include "Circle.h"
#include "Shape.h"

#include <vector>
// class Cube {
// private:
//   double length;
// public:
//   double getVolume() {
//     return length*length;
//   }
//   void setLength(double lengthInput) {
//     length = lengthInput;
//   }
// };

Cube *CreateCub(){
  Cube cube;
  cube.setLength(15);
  return &cube;
}

int add(int x, int y)
{
    return x + y;
}

void CubeCall(Cube cube){
  std::cout << "Cube Call" << std::endl;
}

Cube CubeCreate()
{
  Cube cube(3.0);
  return cube;
}

double CubeVolumeStack() {
  Cube hj(3);
  return hj.getVolume();
}

double CubeVolumeHeap(){
  Cube * hjn = new Cube(10);
  Cube * hjn2 = new Cube;
  delete hjn;
}

int main() {

  std::cout << "helloworld\n" << std::endl ;

  Cube c;
  c.setLength(4.0);
  double volume = c.getVolume();

  std::cout << "Helloworld" << volume << std::endl;

  int a = 4;
  int * p = &a;
  int b = *p;

  std::cout << a << " " << p << " " << b << std::endl;

  Cube * cp1 = CreateCub();
  Cube * cp2 = &c;
  double a1 = cp1 -> getVolume();
  double a2 = cp2 -> getVolume();

  std::cout << a1 << " " << a2 << std::endl;

  int num = 42;
  std::cout << "Num:" << num << std::endl;
  std::cout << "Num address:" << &num << std::endl;

  int * pn = &num;

  std::cout << "pn: " << pn << std::endl;
  std::cout << "&pn:" << &pn << std::endl;
  std::cout << "*pn:" << *pn << std::endl;

  *pn = 1;

  std::cout << "pn: " << pn << std::endl;
  std::cout << "&pn:" << &pn << std::endl;
  std::cout << "*pn:" << *pn << std::endl;
  std::cout << "num:" << num << std::endl;

  int * numpointer = new int;

  std::cout << "numpointer:" << numpointer << std::endl;
  std::cout << "&numpointer:" << &numpointer << std::endl;
  std::cout << "*numpointer:" << *numpointer << std::endl;

  *numpointer = 42;
  std::cout << "numpointer:" << numpointer << std::endl;
  std::cout << "&numpointer:" << &numpointer << std::endl;
  std::cout << "*numpointer:" << *numpointer << std::endl;

  Cube * cubeheap = new Cube;
  cubeheap -> setLength(15);
  std::cout << "Volume 15^3" << cubeheap -> getVolume() << std::endl;

  delete cubeheap;
  delete numpointer;

  std::cout << "After deletion" << std::endl;
  std::cout << "numpointer:" << numpointer << std::endl;
  std::cout << "&numpointer:" << &numpointer << std::endl;
  std::cout << "*numpointer:" << *numpointer << std::endl;

  a = *numpointer + 5;

  std::cout << a << std::endl;

  int (*func_pntr)(int, int) =  &add ;

  std::cout << "funcpnt()" << func_pntr(4,5) << std::endl;
  std::cout << "*funcpnter()" << (*func_pntr)(4,5) << std::endl;

  Cube cdefault;
  Cube cnondefault(2);

  std::cout << "Default Cube" << cdefault.getVolume() << std::endl;
  std::cout << "non Default cube" << cnondefault.getVolume() << std::endl;

  CubeCall(cdefault);

  std::cout << "Trying copy constructor again" << std::endl;
  Cube ccopy = CubeCreate();

  std::cout << "New Cube made" << ccopy.getVolume()<< std::endl;

  std::cout << "Trying copy constructor lastime" << std::endl;
  Cube ccopy2 = cdefault;

  int h = 4;
  int &j = h;

  std::cout << "h: " << h << "j: " << j << std::endl;

  j = 8;

  std::cout << "h: " << h << "j: " << j << std::endl;

  h = 6;
  std::cout << "h: " << h << "j: " << j << std::endl;

  // CubeVolumeStack();
  // CubeVolumeHeap();
  // CubeVolumeStack();

  //sint bhj{2};
  int bhj2 = 2;

  for (int i = 0; i < 5; i++){

    std::cout<<i<<std::endl;

  }

  std::vector<int> vint;
  vint.push_back(1);
  vint.push_back(2);

  std::cout << vint[0] << std::endl;

  std::cout << "hi" << std::endl;
  int tempinta(2);

  std::cout << tempinta << std::endl;

  Circle circletest2(2);
  std::cout << "Circle Area" << circletest2.getArea() << std::endl;

  return 0;

}
