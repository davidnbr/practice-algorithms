"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
 Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the
end of the alphabet. just rotate back to the front of the alphabet. In the case of a
rotation by 3. W. X. y and Z would map to z. a, b and C.
    Original alphabet:
                                      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +3:
                                     defghijklmnopqrstuvwxyzabc
Example
 S = There's-a-starman-waiting-in-the-sky
k 3
The alphabet is rotated by 3. matching the mapping above. The encrypted string is
Wkhuh 'v-d-vwdupdq-zdlwlqj-1q-wkh-vnb.
Note: The cipher only encrypts letters; symbols, such as -.

"""

#!/bin/python3

import os

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]  # 26
    alphabet_upper = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    result = ""
    for letter in s:
        if letter in alphabet:
            letter = alphabet[
                (alphabet.index(letter) + k) - 26 * ((alphabet.index(letter) + k) // 26)]

        elif letter in alphabet_upper:
            letter = alphabet_upper[
                (alphabet_upper.index(letter) + k)
                - 26 * ((alphabet_upper.index(letter) + k) // 26)]

        result += letter
    return result


if __name__ == "__main__":

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
