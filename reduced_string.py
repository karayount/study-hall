""" Steve has a string S, consisting of N lowercase English letters. In one
operation, he can delete any pair of adjacent letters with the same value. For
example, string "aabccaabcc" would become either "aabaab" or "bccbcc" after 1
operation. Steve wants to reduce S as much as possible. To do this, he will
repeat the above operation as many times as it can be performed. Help Steve out
by finding and printing S's non-reducible form. Note: If the final string is
empty, print "Empty String".
Input format: a single string, S
Output format: if the final string is empty, print "Empty String"; otherwise,
print the final non-reducible string.

Sample Input 1:
aaabccddd

Sample Output 1:
abd

Sample Input 2:
baab

Sample Output 2:
Empty String
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input().strip()

def reduce(string):
    # find unique characters
    chars = set()
    for char in string:
        chars.add(char)

    # if string has only unique characters, or is empty, return
    if len(chars) == len(string):
        return string

    # walk string looking for duplicates
    shortest = string
    for j in range(1, len(string)):
        i = j-1
        if string[i] == string[j]:
            shorter = string[:i] + string[j+1:]
            shortest = reduce(shorter) if len(reduce(shorter)) < len(shorter) else shorter

    # output
    if shortest:
        print shortest
    else:
        print "Empty String"

reduce(s)
