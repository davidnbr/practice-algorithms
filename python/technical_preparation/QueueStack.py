"""A queue is an abstract data type that maintains the order in
which elements were added to it. allowing the oldest
 elements to be removed from the front and new elements
 to be added to the rear. This is called a First-In-First-Out
 (FIFO) data structure because the first element added to
the queue (i.e.. the one that has been waiting the longest) is
 always the first one to be removed.
A basic queue has the following operations:
    Enqueue: add a new element to the end of the queue.
    Dequeue: remove the element from the front of the
    queue and return

    
    Input Format
The first line contains a single integer. q. denoting the
number of queries.
 Each line i of the q subsequent lines contains a single
query in the form described in the problem statement
 above. All three queries start with an integer denoting the
query type. but only query 1 is followed by an additional
space-separated value, x. denoting the value to be
enqueued.
Constraints
   1 5 a < 105
   1 < type < 3
   1< | < 109
   It is guaranteed that a valid answer always exists for
   each query of type 3.
Output Format
For each query of type 3."""


class Stack:
    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        self.elements.pop(0)

    def show(self):
        print(self.elements[0])


if __name__ == "__main__":

    s = Stack()

    q = int(input().strip())

    for queries in range(q):
        query = input().rstrip().split()

        action = int(query[0])
        if action == 1:
            s.enqueue(query[1])
        elif action == 2:
            s.dequeue()
        elif action == 3:
            s.show()

"""
Test input:
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""
