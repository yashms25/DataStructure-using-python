
class circularQueue:

    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.rear = self.front = size -1
    
    def insert(self, elem):
      self.rear = (self.rear+1) % self.size
      if self.rear == self.front:
        print("Circular Queue is Full")
        self.rear-=1
      else:
        self.queue[self.rear]=elem

    def remove(self):
      if self.rear == self.front:
        print("Circular Queue is Empty")
      else:
        self.front = (self.front+1) % self.size
        return self.queue[self.front]

    def show(self):
        if self.rear == self.front:
           print("Circular queue is Empty")
        else:
          if self.front<=self.rear:
            print("Circular queue Contains:")
            for i in range(self.front+1 , self.rear + 1):
                print(self.queue[i], end=" ")
            print()
          else:
            print("Circular queue Contains:")
            for i in range(self.front+1 , self.size):
                print(self.queue[i], end=" ")
            for i in range(self.rear + 1):
                print(self.queue[i], end=" ")
            print()
size=int(input("Enter size of Circular queue:"))
queue=circularQueue(size)
while(True):
  print("""1. Insert
2. Remove
3. Show
4. Exit""")
  choice=input()
  if(choice=='1'):
    queue.insert(int(input("Enter element to be insert:")))
  elif(choice=='2'):
    queue.remove()
  elif(choice=='3'):
    queue.show()
  elif(choice=='4'):
    break
  else:
    print("Invalid Input")
  
