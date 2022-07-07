#include "cube.h"
#include <iostream>

Cube::Cube(const Cube & obj) {
  length_ = obj.length_;
  // std::cout<< "Copy Constructor" << std::endl;
}

Cube::Cube() {
  length_ = 1.0;
  // std::cout << "Default Constructor" << std::endl;
}

Cube::Cube(double length) {
  length_ = length;
  // std::cout << "Custom Constructor" << std::endl;
}

Cube::~Cube(){
  // std::cout << "Destroying Cube" << std::endl;
}

double Cube::getVolume() const {
  return length_*length_*length_;
}

double Cube::getSurfaceArea() const{
  return 6 * length_ * length_;
}

void Cube::setLength(double length) {
    length_ = length;

}

double Cube::getLength() const {
  return length_;
}

bool Cube::operator== (const Cube & b){
    if (this -> getLength() == b.getLength()) {
      return true;
    }
    return false;
}
