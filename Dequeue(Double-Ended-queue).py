
class Deque:
    def __init__(self):
        self.queue= []

    def addRear(self, elem):
        self.queue.append(elem)

    def addFront(self, elem):
        self.queue.insert(0, elem)

    def removeFront(self):
        if len(self.queue) == 0:
           print("Dequeue Is Empty")
        else:
           self.queue.pop(0)

    def removeRear(self):
        if len(self.queue) == 0:
           print("Dequeue Is Empty")
        else:
           self.queue.pop()
        
    def show(self):
      if len(self.queue) == 0:
           print("Dequeue Is Empty")
      else:
          print("Dequeue Contains:")
          print(self.queue)


queue=Deque()
while(True):
  print("""1. InsertRear
2. InsertFront
3. RemoveRear
4. RemoveFront
5. Show
6. Exit""")
  choice=input()
  if(choice=='1'):
    queue.addRear(int(input("Enter element to be insert:")))
  elif(choice=='2'):
    queue.addFront(int(input("Enter element to be insert:")))
  elif(choice=='3'):
    queue.removeRear()
  elif(choice=='4'):
    queue.removeFront()
  elif(choice=='5'):
    queue.show()
  elif(choice=='6'):
    break
  else:
    print("Invalid Input")
