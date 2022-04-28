#Node Class
class Node:
    def __init__(self,data):
        #Creating nodes initially reference as None.
        self.data=data  #Assign data
        self.ref=None   #Initialize next as null

#LinkedList Class.
class LinkedList:
    def __init__(self): 
        self.head=None  #Creating empty LinkedList.
    
    def display(self):
        print("******Displaying Linked List******")
        if self.head is None:
            print("Linked list is empty!.")
        else:
            n=self.head
            while n is not None:
                print(n.data)     #Printing Data
                n=n.ref           #Adding reference of next variable.
            print("**********************************")

    def add_begin(self,data):
        new_node=Node(data)    #Created a object for node class and passed data as argument.
        new_node.ref=self.head #Assigning the address of 'head' as new node node reference.
        self.head=new_node     #Making newly inserted node as 'head'.
        print("Element",data,"added at the beginning.")

    def add_between(self,data):
        if(self.head==None):
            self.head==Node(data)   #Assigning new node as head bcz LL is empty.
        else:
            new_node=Node(data)  #Created new node for the value.

            new_ptr=self.head
            length=0
            #Calculating length of the linked list.
            while(new_ptr!=None):
                new_ptr=new_ptr.ref
                length+=1
            
            #Counting the number of the node after which the new node is going to insert.
            if(length%2==0):
                count=length/2
            else:
                (length+1)/2    
            
            new_ptr=self.head

            #Moving pointer to the node after which the new node need to be inserted.
            while(count>1):
                count-=1
                new_ptr=new_ptr.ref
            #Inserting the new node and adjusting links.
            new_node.ref=new_ptr.ref
            new_ptr.ref=new_node

            
    def add_end(self,data):    #Created a object for node class and passed data as argument.
        new_node=Node(data)
        if self.head is None:
            print("Linked list is empty")
            self.head=new_node  #Assigning new node as head bcz LL is empty.
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref         #Assigning next node with reference.
            n.ref=new_node      #Assigning Last node reference to newly added last node address.
            print("Element",data,"added at the ending.")



ll=LinkedList()
ll.add_begin(10)
ll.display()

ll.add_end(100)
ll.display()

ll.add_between(5)
ll.display()

