#pragma once

class Cube{
  public:
    Cube();
    Cube(double length);
    Cube(const Cube & obj);
    ~Cube();
    void setLength(double length);
    double getVolume() const;
    double getSurfaceArea() const;
    double getLength() const;
    bool operator== (const Cube &b);

  private:
    double length_;
};
