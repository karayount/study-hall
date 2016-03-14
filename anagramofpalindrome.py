"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?
    In order to be a palindrome, all letters must have a pair or there can be a
    single lone letter for the center of an odd length word. Keeping count of
    instances of each letter, if there's at most one letter with an odd count,
    the word is an anagram of a palindrome."""


    chr_count = {}
    for chr in word:
        if chr in chr_count:
            chr_count[chr] += 1
        else:
            chr_count[chr] = 1
    odds = 0
    for chr in chr_count:
        if chr_count[chr] % 2 == 1:
            odds += 1
        if odds > 1:
            return False

    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
