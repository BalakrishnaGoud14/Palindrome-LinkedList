
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def reverse(head):
    curr=head
    prev=None
    next=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        
    return prev


def isPalindrome(head) :
    if head is None or head.next is None:
        return True
    fast=head
    slow=head
    while fast.next is not None and fast.next.next is not None:
        fast=fast.next.next
        slow=slow.next
    head2=slow.next
    slow.next=None
    head2=reverse(head2)
    firstlist=head2
    secondlist=head
    
    while firstlist:
        if firstlist.data!=secondlist.data:
            return False
        firstlist=firstlist.next
        secondlist=secondlist.next
    firstlist=head
    secondlist=reverse(head2)
    while firstlist.next:
        firstlist=firstlist.next
    firstlist.next=secondlist
    return True
 


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()



#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1










