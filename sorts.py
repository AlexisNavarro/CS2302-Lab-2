# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:26:02 2019

@author: Alexis Navarro
CS 2302
Lab #2 
Dr.Fuentes
#Purpose: By using Linked Lists I needed to implement various sortings in order to show my abilities with using sorting and recursion in liked lists
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
#O(n^2) runtime
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
#O(n log(n)) runtime
def merge_Sort(L):
    #n log n runtime
    if L == None or L.next == None:
        return L
    
    middle = split(L) #Split  the list by the middle position
    nextMiddle = middle.next# to declare the position after the middle, in order for the right side of the list to be stored
    
    middle.next = None
    
    left = merge_Sort(L) #merge_sort is used recursively to create the left side of the list
    
    right = merge_Sort(nextMiddle) # the right is declared everything after the middle of the original list
    
    sortedList= sorted_Merge(left, right)# Merge both the lists on its own specific merge
    return sortedList


def split(L):
    fast = L.next
    slow = L
    while fast != None: # moves fast by two 
        fast = fast.next
        if fast != None:
            slow = slow.next#moves slow by one until it gets to the middle position
            fast = fast.next
    return slow
    
    
def sorted_Merge(leftSide, rightSide):
   Result = None
   if leftSide == None:
       return rightSide
   
   if rightSide == None:
       return leftSide
   
   if leftSide.item <= rightSide.item:# compares the values of the left and right side
       Result = leftSide
       Result.next = sorted_Merge(leftSide.next, rightSide)
   else:
       Result = rightSide
       Result.next = sorted_Merge(leftSide, rightSide.next)

   return Result #returns a merge sort list


#------------------------------------------------------------------------------
#QUICK SORT ALGORITM
#O(n log(n)) runtime
def quick_Sort(L):
    if IsEmpty(L):
        return L
    #needed the empty lists to get the leftSide of the Pivot and the Right Side of the Pivot
    leftSide = List()
    rightSide = List()
    
    
    piv = L.head.item # the Pivot points at the first value this time but can be changed on where to point, but will require to change the temp also
    temp = L.head.next
    
    while temp!=None:
        if piv > temp.item:#compare the items of the temp linked list to the first value of the pivot and adds the specific values to either the left or right side lists
            Append(leftSide,temp.item)# add the new values to the leftside of the list
            temp = temp.next
        else:
            Append(rightSide,temp.item)
            temp = temp.next
            
    newLeft = quick_Sort(leftSide) # recurse the method again in order to sort until everything is in order
    newRight = quick_Sort(rightSide)
    
    Append(newLeft,piv)
    
    return Concate(newLeft,newRight) # merge both left and right to create a new sorted list. Can't use the same merge as sorted_Merge
        
    
    
    
#------------------------------------------------------------------------------ 
#Modified Quick sort

def modified_quickSort(L, n):
    if IsEmpty(L):
        return L
    Print(L)
    left_Side = List()
    right_Side= List()
    piv = L.head.item
    temp = L.head.next
    
    while temp is not None:
        if piv>temp.item:
            Append(left_Side,temp.item)
            temp = temp.next
        else:
            
            Append(right_Side,temp.item)
            temp = temp.next
            
    #to get big O
    #if my n is the pivot
    if n== GetLength(left_Side):
        return piv
    
    #if my n is in the left side of my list
    elif n >= GetLength(left_Side):
        #n = n - GetLength(left_Side)-1
        return modified_quickSort(right_Side, n)
    
    #if my n is in the right side of my list
    elif n <= GetLength(left_Side):
        return modified_quickSort(left_Side,n)
    
    
    
#------------------------------------------------------------------------------  
def GetLength(L): # finds the length of the list
    temp = L.head
    count = 0
    while temp is not None:
        count+=1
        temp = temp.next
    return count
           

def ElementAt(L, mid): # gives the element of the list where the middle is positioned at
    current = L.head 
    count = 0 
  
    while (current): 
        if (count == mid): 
            return current.item 
        count += 1
        current = current.next
    return 0; 
        
    
def Median(L):# method to find the middle value of the list
    C = copy(L) # creates a copy to make sure to not affect the original list
    element= ElementAt(C,GetLength(C)//2)
    print('Sorted Value of middle element is %d' %element)
    
def Median2(L):
    C = copy(L)
    element= modified_quickSort(C,GetLength(C)//2)
    print('Sorted Value of middle element is ', element)
    return C


#------------------------------------------------------------------------------
# MAIN
L = List()
#print(IsEmpty(L))
for i in range(5):
   t = random.randint(1,5)
   Append(L,t)

#leftSide= List()  tried to make them global variables for merge and quick sort
#rightSide= List()
#Print(L)

#UNCOMMENT TO TEST THE SORTINGS

#bubble_Sort(L)
#L.head=merge_Sort(L.head)
#L=quick_Sort(L)
#Median(L)
#Print(L)

Median2(L)

