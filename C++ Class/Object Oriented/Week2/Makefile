CC = clang++
CFLAGS = -c -Wall --std=c++11

hello: Week2.o cube.o LinkedList.o
	$(CC) Week2.o cube.o LinkedList.o -o hello

Week2.o: Week2.cpp
	$(CC) $(CFLAGS) Week2.cpp
cube.o : cube.cpp
	$(CC) $(CFLAGS) cube.cpp

LinkedList.o : LinkedList.cpp
	$(CC) $(CFLAGS) LinkedList.cpp

# List.o : List.cpp
# 	$(CC) $(CFLAGS) List.cpp

clean:
	rm -rf *o
