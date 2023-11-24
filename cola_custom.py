class Cola():
    def __init__(self):
        self.array = []

    def push(self,valor_to_input):
        self.array.append(valor_to_input)
    
    def dequeue(self):
        dequeue(self.array)

    def view_cola(self):
        print(self.array)

if __name__ == "__main__":
    cola=Cola()
    for i in range(10):
        cola.push(i)
    cola.view_cola()

    print()

    for _ in range(10):
        cola.dequeue()
    cola.view_cola()