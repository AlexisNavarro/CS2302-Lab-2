# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:26:02 2019

@author: Alexis
"""
import random


class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        

        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
        
def IsEmpty(L):  
    return L.head == None     
  
      
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
     
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
    
def copy(L):
    temp = L.head
    list2 = Node (0)
    list2.head = temp
    while temp is not None:
        temp = temp.next
        list2.next = temp
    return list2
   

def IsSorted(L):
    if L.head == None or L.head.next == None:
        print('sorted')
        return True
    temp = L.head
    while temp is not None:
        if temp.item > temp.next.item:
            print('not sorted')
            return False
    return True
def Concate(L1,L2):
    if IsEmpty(L1):
        return L2
    elif IsEmpty(L2):
        return L1
    L1.tail.next = L2.head
    L1.tail = L2.tail
    return L1


#------------------------------------------------------------------------------
#BUBBLE SORT ALGORITHM
def bubble_Sort(L):
    change = True
    while change:
        t = L.head
        change = False
        while t.next is not None:
            if t.item > t.next.item:
                temp=t.item
                t.item = t.next.item
                t.next.item=temp
                change = True
            t=t.next
            
            
#------------------------------------------------------------------------------            
#MERGE SORT ALGORITHM   
def merge_Sort(L):
    #n log n runtime
    count=0
    if L == None or L.next == None:
        return L
    
    middle = split(L)
    nextMiddle = middle.next
    
    middle.next = None
    left = merge_Sort(L)
    right = merge_Sort(nextMiddle)
    
    sortedList= sorted_Merge(left, right, count)
    return sortedList


def split(L):
    fast = L.next
    slow = L
    while fast != None:
        fast = fast.next
        if fast != None:
            slow = slow.next
            fast = fast.next
    return slow
    
    
def sorted_Merge(leftSide, rightSide, count):
   Result = None
   if leftSide == None:
       return rightSide
   
   if rightSide == None:
       return leftSide
   
   if leftSide.item <= rightSide.item:
       Result = leftSide
       Result.next = sorted_Merge(leftSide.next, rightSide, count+1)
   else:
       Result = rightSide
       Result.next = sorted_Merge(leftSide, rightSide.next, count +1)

   return Result


#------------------------------------------------------------------------------

#QUICK SORT ALGORITM
def quick_Sort(L):
    if IsEmpty(L):
        return L
    
    piv = L.head.item
    temp = L.head.next
    leftSide = List()
    rightSide = List()
    
    while temp!=None:
        if temp.item < piv:
            Append(leftSide,temp.item)
            temp = temp.next
        else:
            Append(rightSide,temp.item)
            temp = temp.next
            
    newLeft = quick_Sort(leftSide)
    newRight = quick_Sort(rightSide)
    
    Append(newLeft,piv)
    
    return Concate(newLeft,newRight)
        
    
    
    
#------------------------------------------------------------------------------  
def GetLength(L):
    temp = L.head
    count = 0
    while temp is not None:
        count+=1
        temp = temp.next
    return count
           

def ElementAt(L, mid):
    current = L.head 
    count = 0 
  
    while (current): 
        if (count == mid): 
            return current.item 
        count += 1
        current = current.next
    return 0; 
        
    
def Median(L):
    C = copy(L)
    element= ElementAt(C,GetLength(C)//2)
    print('Sorted Value of middle element is %d' %element)


#------------------------------------------------------------------------------
# MAIN
L = List()
print(IsEmpty(L))
for i in range(5):
   t = random.randint(1,5)
   Append(L,t)

#leftSide= List()  tried to make them global variables for merge and quick sort
#rightSide= List()
Print(L)

#UNCOMMENT TO TEST THE SORTINGS

#bubble_Sort(L)
#L.head=merge_Sort(L.head)
#L=quick_Sort(L)
Median(L)

Print(L)
