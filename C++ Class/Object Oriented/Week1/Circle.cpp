#include "Circle.h"
#include "Shape.h"
#include <iostream>

Circle::Circle(double radius) : Shape(radius) {
  //Nothing
  std::cout<< "Test" << std::endl;
}

double Circle::getArea() {
  return getWidth()*2.14;
}
