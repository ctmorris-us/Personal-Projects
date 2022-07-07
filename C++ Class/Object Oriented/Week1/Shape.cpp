#include "Shape.h"
#include <iostream>

Shape::Shape() : Shape(1) {
  // Inhereits from base class with intial width 1
  std::cout<< "Test" << std::endl;
}

Shape::Shape(double width) : width_(width){
  // Calls Shapes private width function which assigns width to width_
  std::cout<< "Test" << std::endl;
}

double Shape::getWidth() {
  return width_;
}
