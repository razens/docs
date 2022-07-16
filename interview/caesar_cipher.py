"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example


The alphabet is rotated by , matching the mapping above. The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Input Format

The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.

Constraints

1 <= n <= 100
0 <= k <= 100


 is a valid ASCII string without any spaces.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

"""

# !/bin/python3

import math
import os
import random
import re
import sys
import unittest


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = []
    while k >= 26:
        k = k - 26
    for letter in s:
        if not is_lowercase_letter(letter) and not is_uppercase_letter(letter):
            result.append(letter)
            continue
        elif is_lowercase_letter(letter):
            index = ord(letter) + k
            while index > 122:
                index = index - 26
            ciphered_letter = chr(index)
            result.append(ciphered_letter)
        elif is_uppercase_letter(letter):
            index = ord(letter) + k
            while index > 90:
                index = index - 26
            ciphered_letter = chr(index)
            result.append(ciphered_letter)
    return "".join(result)


def is_uppercase_letter(letter) -> bool:
    return 65 <= ord(letter) <= 90


def is_lowercase_letter(letter) -> bool:
    return 97 <= ord(letter) <= 122


class TestCaesarCipher(unittest.TestCase):
    def test_1(self):
        result = caesarCipher('abcdef', 1)
        self.assertEqual(result, 'bcdefg')

    def test_2(self):
        result = caesarCipher('abcdefghijklmnopqrstuvwxyz', 3)
        self.assertEqual(result, 'defghijklmnopqrstuvwxyzabc')

    def test_3(self):
        result = caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5)
        self.assertEqual(result, 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # s = input()
    # k = int(input().strip())
    # result = caesarCipher(s, k)
    # fptr.write(result + '\n')
    # fptr.close()
    unittest.main()
