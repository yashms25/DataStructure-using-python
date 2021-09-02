class priorityQueue:

    def __init__(self):
        self.queue = []

    def insert(self, elem):
        self.queue.append(elem)

    def removeAsc(self):
        if len(self.queue) == 0:
            print("Priority Queue is Empty")
        else:
            m = min(self.queue)
            self.queue.remove(m)
            print(m,"is removed")
            
   
    def removeDsc(self):
        if len(self.queue) == 0:
            print("Priority Queue is Empty")
        else:
            m = max(self.queue)
            self.queue.remove(m)
            print(m,"is removed")

    def show(self):
        if len(self.queue) == 0:
            print("Priority Queue is Empty")
        else:
            print("Priority Queue Contains:",self.queue)

queue=priorityQueue()
while(True):
  print("""1. Insert
2. RemoveAsc
3. RemoveDsc
4. Show
5. Exit""")
  choice=input()
  if(choice=='1'):
    queue.insert(int(input("Enter element to be insert:")))
  elif(choice=='2'):
    queue.removeAsc()
  elif(choice=='3'):
    queue.removeDsc()
  elif(choice=='4'):
    queue.show()
  elif(choice=='5'):
    break
  else:
    print("Invalid Input")
  
