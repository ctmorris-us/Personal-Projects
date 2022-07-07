#pragma once

class Cube{
  public:
    Cube();
    Cube(double length);
    Cube(const Cube & obj);
    ~Cube();
    double getVolume();
    double getSurfaceArea();
    void setLength(double length);

  private:
    double length_;
};
