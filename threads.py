import threading
import os

def print_cube(num):
	# function to print cube of given num
    print("Cube: {}" .format(num * num * num))
    print(os.getpid())

def print_square(num):
	# function to print square of given num
    print("Square: {}" .format(num * num))
    print(os.getpid())

if __name__ =="__main__":
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(5,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done!")