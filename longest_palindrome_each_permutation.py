def find_each_longest_palindrome(s, n):
    for i in range(n):
        substring = create_substring(s, n, i)
        longest = find_max_palindrome_length(substring)
        print longest


def create_substring(string, length, index):
    start = string[index:]
    end = string[:index]
    substring = start + end
    return substring


def find_max_palindrome_length(string):
    max = len(string)
    max_pal = 1
    i = 0
    while i < max and (max-i) > max_pal:
        last = max
        while i < last and (last-i) > max_pal:
            if is_palindrome(string[i:last]):
                length = last-i
                if length > max_pal:
                    max_pal = length
            last -= 1
        i += 1
    return max_pal


def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


find_each_longest_palindrome("aaaaabbbbaaaa", 13)
find_each_longest_palindrome("cacbbba", 7)