#!/usr/bin/env python
# coding: utf-8

# In[67]:


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        lstr = ''
        while itr:
            lstr+=str(itr.data) + '-->'
            itr=itr.next
        print(lstr)      

    def reverse(self):
        if self.head is None:
            pass
        else :
            ptr = self.head
            lst=''
            rev(ptr,lst)   

            
def rev(ptr,lst):                            # recursive function ....linked List in reverse 
        if ptr.next:
            rev(ptr.next,lst)
        print(ptr.data) 
        
    
    
if __name__=="__main__" :
    ll=LinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(85)
    ll.insert_at_beginning('Ram')
    ll.insert_at_beginning("Shyam")
    
    print("<<----Printing From front-------->>")
    ll.print()
    print("\n<<-------Printing in REVERSE----->>")
    ll.reverse()
    
    
    


# In[ ]:




