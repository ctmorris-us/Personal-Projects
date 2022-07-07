CC = clang++
CFLAGS = -c -Wall --std=c++11

hello: helloworld.o cube.o Circle.o Shape.o
	$(CC) helloworld.o cube.o  Shape.o Circle.o -o hello

hellworld.o: helloworld.cpp
	$(CC) $(CFLAGS) helloworld.cpp

cube.o: cube.cpp
	$(CC) $(CFLAGS) cube.cpp

Circle.o: Circle.cpp
	$(CC) $(CFLAGS) Circle.cpp

Shape.o: Shape.cpp
	$(CC) $(CFLAGS) Shape.cpp


clean:
	rm -rf *o
