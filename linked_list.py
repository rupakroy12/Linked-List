#!/usr/bin/env python
# coding: utf-8

# In[67]:


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:                               #Linked list Class
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):         #insert at beginning
        node = Node(data,self.head)
        self.head = node
    
    def print_linked_list(self):                #print linked list
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        lstr = ''
        while itr:
            lstr+=str(itr.data) + '-->'
            itr=itr.next
        print(lstr.rstrip('-->') )            # rstrip removes the "-->" from the end    
    
    def insert_at_end(self,data):              # insert at end
        if self.head is None:
            print("Linked List is empty")
        else :
            node=Node(data)
            ptr=self.head
        
            while ptr.next:
                ptr=ptr.next
            ptr.next=node
            
    def delete_end(self):                       #delete from  end
        if self.head is None:
            print("Linked List is empty")
            
        else:
            ptr=self.head
            while ptr.next.next:
                ptr=ptr.next
            ptr.next=None
            
            
    def delete_from_front(self):                 #delete node from front
        if self.head is None:
            print("Linked List is Empty")
        else:
            
            self.head=self.head.next
    
    
    def count_nodes(self):                      #count the number of nodes in linked list
        if self.head is None:
            pass
        else:
            count=0
            ptr=self.head
            while ptr.next:
                count+=1
                ptr=ptr.next
            count+=1
        # print(f"Total number of Nodes are : {count}")
        return count
    
     def insert_any_position(self,pos,data):     # insert at any position
        if self.head is None:
            print("Linked List is Empty")
        else:
            ptr = self.head
            count = 0
            while ptr.next:
                if count==pos-1:
                    break
                
                count+=1
                ptr = ptr.next
                
            node = Node(data)
            node.next=ptr.next
            ptr.next = node





    def check_data(self,val):                         #Search whether the particular element is present in linked list or not and return position(s) and count
        if self.head is None:
            pass
        else:
            ptr=self.head
            count=0
            index=-1
            text=''
            while ptr.next:
                index+=1
                if ptr.data==val:
                    text+=' '+str(index)+','
                    count+=1
                ptr=ptr.next

            if ptr.data==val:                           # if the element is present in the last node and check is missed in while loop, so checking the last node manually
                index+=1
                count+=1
                text+=' '+str(index)+','
            

            if text!='':
                text=text.rstrip(',')                             #removes the last ',' from index collections in text string
                print(f"({val}) found at index {text} || Count is : {count}")              
                


#     def delete_by_position(self,pos):
#         if pos > self.count_nodes():
#             print("Position does not exist")
        
#         elif pos == self.count_nodes():
#             delete_end()
#             print("Last element deleted ")

#         else : 
#             itr = self.head
#             while itr.next : 

                



    def reverse(self):                          #reverse order print
        if self.head is None:
            pass
        else :
            ptr = self.head
            #print(rev(ptr,lst=''))            
#             x=(rev(ptr,lst=[]))
#             print(x)
            lst=[]
            rev(ptr,lst)                       # printng as string, the first call to the recursive function rev
            print(lst)
            
            
def rev(ptr,lst):                            # Recursive function...linked List in reverse...globally defined..called by reverse function
        if ptr.next:
            #lst+=str(rev(ptr.next,lst))
            rev(ptr.next,lst)
        
        #lst+=str(ptr.data)+'<--'
        lst.append(ptr.data)       
        return lst

    
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




