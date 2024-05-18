"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker
indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to
swap positions. but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes.
or, if anyone has bribed more than two people, print Too chaotic.

Example
q = [1, ,2,3,5, 4, 6, 7, 8]
If person 5 bribes person 4. the queue will look like this: 1, ,2, 3, 5, 4, ,6,7,8. Only 1 bribe is required. Print 1.
q = [4, 1, 2, 3]
Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.
Function Description
Complete the function minimumBribes in the editor below.
minimumBribes has the following parameter(s):
   int q[n]: the positions of the people after all bribes
Returns
   No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than 2 people

Input Format
The first line contains an integer t. the number of test cases.
Each of the next t pairs of lines are as follows:
- The first line contains an integer t. the number of people in the queue
 - The second line has n space-separated integers describing the final state of the queue.
Constraints
   1   1 10
   1<n <105
Subtasks
For 60% score 1 < n < 103
For 100% score 1 < n < 105
Sample Input
                Function
   STDIN
   2
               t = 2
   5
               n II 5
   21534 q = [2, 1, 5, 3, 4]
   5
               n = 5
   25134 q = [2, 5, 1, 3, 4]

"""


def minimumBribes(q):
    # one_brided = 0
    all_brided = 0
    for i in range(len(q)):
        one_brided = 0

        for j in range(i + 1, len(q)):
            if q[i] > q[j]:
                one_brided += 1
                all_brided += 1
            if one_brided > 2:
                print("Too chaotic")
                return
            """if j>=i:
                if q[j]<q[i]:
                    one_brided+=1
                if one_brided>2:
                    print("Too chaotic")
                    return None
            if j<i:
                if q[j]>q[i]:
                    all_brided+=1"""

    print(all_brided)


def minimumBribes2(q):
    # one_brided = 0
    all_brided = 0
    for i in range(len(q)):
        one_brided = 0
        ev = q[i]
        q_new = [p for p in q[i + 1 :] if p < ev]
        if len(q_new) > 2:
            print("Too chaotic")
            return
        all_brided += len(q_new)
        # for j in range(i+1, len(q)):
        """for j in q_new:
            #if q[i]>q[j]:
            if q[i]>j:
                one_brided+=1
                all_brided+=1
            if one_brided>2:
                print("Too chaotic")
                return"""

        """if j>=i:
                if q[j]<q[i]:
                    one_brided+=1
                if one_brided>2:
                    print("Too chaotic")
                    return None
            if j<i:
                if q[j]>q[i]:
                    all_brided+=1"""

    print(all_brided)


def minimumBribesOptimized(q):
    all_brided = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                all_brided += 1


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
