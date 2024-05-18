"""
Implement a simple text editor. The editor initially contains an empty string. S. Perform
                                                                                             operations of the following 4 types:
 1. append(W) - Append string W to the end of S.
 2. delete(k) - Delete the last k characters of S.
 3. print(k) - Print the kth character of S.
 4. undo() - Undo the last (not previously undone) operation of type 1 or 2. reverting S to the state it was in prior to that operation.
 Example
 S = 'abcde'
 ops = I'1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']

operation
 index
         S
                ops[index] explanation
3
         abcde
                 1 fg
                            append fg
         abcdefg 3 6
                            print the 6th letter - f
         abcdefg 2 5
                            delete the last 5 letters
         ab
                4
                            undo the last operation, index 2
                            print the 7th characgter - g
         abcdefg 3 7
 4 5 6
         abcdefg 4
                            undo the last operation, index 0
         abcde
                3 4
                            print the 4th character - d
The results should be printed as:
 f
 g d

 Input Format
The first line contains an integer. Q. denoting the number of operations.
 Each line i of the 0 subsequent lines (where 0 <i < Q defines an operation to be performed. Each operation starts with a single
integer. t (where t E {1, 2, 3, 4}). denoting a type of operation as defined in the Problem Statement above. If the operation requires an
argument. t is followed by its space-separated argument. For example. if t = 1 and W = "abcd". line i will be 1 abcd.
Constraints
1<Q<106
1<k<|S|
 The sum of the lengths of all W in the input < 106
 The sum of k over all delete operations < 2 . 10
 All input characters are lowercase English letters.
 It is guaranteed that the sequence of operations given as input is possible to perform.

 Output Format
 Each operation of type 3 must print the 1th character on a new line.
Sample Input
   STDIN    Function
   8        Q = 8
   1 abc    ops[0] = '1 abc '
   3 3      ops[1] = '3 3'
   2 3
   1 ху
   3 2
   4 
   4 
   3 1

Sample Output:
c
y
a


"""


# Solution
class Text:
    def __init__(self):
        self.text = []
        self.state = []

    def appendd(self, w):  # Type 1
        self.state.append([1, len(w)])
        self.text.extend(w)  # append elements from an iterable w to the end of the list
        # print(f"type 1: state: {self.state}, text: {self.text}")

    def delete(self, k):  # Type 2
        self.state.append([2, self.text[-k:]])
        del self.text[-k:]
        # self.text = self.text[:-k]
        # print(f"type 2: state: {self.state}, text: {self.text}")

    def printt(self, k):
        print(self.text[k - 1])
        # print(f"type 3: text: {self.text}")

    def undo(self):
        # last_state = self.state[-1]
        last_state = (
            self.state.pop()
        )  # remove and return the last element from the list and save it to a variable
        if last_state[0] == 1:
            # self.text = self.text[:-last_state[1]]
            del self.text[-last_state[1] :]
        else:
            self.text.extend(
                last_state[1]
            )  # append elements from an iterable w to the end of the list
        # self.state = self.state[:-1]
        # print(f"type 4: state: {self.state}, text: {self.text}")


if __name__ == "__main__":
    t = Text()
    dic = {1: t.appendd, 2: t.delete, 3: t.printt, 4: t.undo}
    itr = int(input().strip())

    for q in range(itr):
        user_in = input().rstrip().split()
        user_in[0] = int(user_in[0])

        if user_in[0] in dic:
            if len(user_in) > 1:
                if user_in[0] > 1:
                    user_in[1] = int(user_in[1])
                dic[user_in[0]](user_in[1])
            else:
                dic[user_in[0]]()
