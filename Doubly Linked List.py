class Node:  
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
   
    def __init__(self):
      self.first = self.last = self.current = self.follow = self.ahead = self.new = None

    def insert(self,data):
       new = Node(data)
       if not self.first:
         self.first = self.last = new
         new.next = None
         new.prev = None
       else:
         self.last.next = new
         new.prev = self.last
         self.last = new
         new.next = None
    
    def insertBefore(self):
      if self.first == None:
        print("Linked List is Empty")
      else:
        data = int(input("Enter element to be insert:"))
        elem = int(input("Enter number before which insertion should be done:"))
        new = Node(data)
        self.current = self.first
        self.follow = None
        while(self.current.data != elem and self.current ):
          self.current = self.current.next
          if not self.current:
            break       
        if not self.current:
          print("Element not Found")
        else:
          self.follow = self.current.prev
          if self.current == self.first:
            new.next = self.first
            self.first.prev = new
            self.first = new
            new.prev = None
          else:
            self.follow.next = new
            new.prev = self.follow
            new.next = self.current
            self.current.prev = new
    
    def insertAfter(self):
      if self.first == None:
        print("Linked List is Empty")
      else:
        data = int(input("Enter element to be insert:"))
        elem = int(input("Enter number after which insertion should be done:"))
        new = Node(data)
        self.current = self.first
        while(self.current.data != elem and self.current ):
          self.current = self.current.next
          if not self.current:
            break
        if not self.current:
          print("Element not Found")
        else:
          self.ahead = self.current.next
          if self.current == self.last:
            self.current.next = new          
            new.prev = self.current
            self.last = new
            new.next = None
          else:
            self.current.next = new
            new.prev = self.current
            new.next = self.ahead
            self.ahead.prev = new
    
    def delete(self):
       if self.first == None:
         print("Linked List is Empty")
       else:
         elem = int(input("Enter element to be delete:"))
         self.current = self.first
         self.follow = None
         while(self.current.data != elem and self.current ):
           self.current = self.current.next
           if not self.current:
             break
         if not self.current:
           print("Element not Found")
         else:
           self.follow = self.current.prev
           self.ahead = self.current.next
           if self.current == self.first and self.current == self.last:
             self.first = None
           elif(self.current == self.first):
             self.first = self.first.next
             self.first.prev = None
           elif(self.current == self.last):
             self.last = self.follow
             self.last.next = None
           else:
             self.follow.next = self.ahead
             self.ahead.prev = self.follow
   
    def traverseForward(self):
        if self.first == None:
          print("Linked List is Empty")
        else:
          print("Linked list Contains:")
          self.current = self.first
          while(self.current):
            print(self.current.data,end=" ")
            self.current = self.current.next
          print()
          
    def traverseBackward(self):
        if self.first == None:
          print("Linked List is Empty")
        else:
          print("Linked list Contains:")
          self.current = self.last
          while(self.current):
            print(self.current.data,end=" ")
            self.current = self.current.prev
          print()
          
    def search(self):
      if self.first == None:
          print("Linked List is Empty")
      else:
        self.current = self.first
        elem = int(input("Enter element to be search:"))
        while(self.current.data != elem and self.current ):
          self.current = self.current.next
          if not self.current:
            break
        if not self.current:
          print("Element not Found")
        else:
          print("Element Found")
          
#Initialise Linked list        
linklist = LinkedList()
while(True):
  print("""1. Insert
2. InsertBefore
3. InsertAfter
4. Delete
5. TraverseForward
6. TraverseBackward
7. Search
8. Exit""")
  choice=input()
  if(choice=='1'):
    linklist.insert(int(input("Enter element to be insert:")))
  elif(choice=='2'):
    linklist.insertBefore()
  elif(choice=='3'):
    linklist.insertAfter()
  elif(choice=='4'):
    linklist.delete()
  elif(choice=='5'):
    linklist.traverseForward()
  elif(choice=='6'):
    linklist.traverseBackward()
  elif(choice=='7'):
    linklist.search()
  elif(choice=='8'):
    break
  else:
    print("Invalid Input")

         
        
