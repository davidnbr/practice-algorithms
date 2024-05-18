def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s) // 2 + 1):

        if s[i] != s[-i - 1]:
            new_string = s[:i] + s[i + 1 :]
            if new_string == new_string[::-1]:
                return i

            new_string = s[: -i - 1] + s[len(s) - i :]
            if new_string == new_string[::-1]:
                return len(s) - 1 - i
    return -1


if __name__ == "__main__":
    string = "abbca"
    print(palindromeIndex(string))
    string = "aaab"
    print(palindromeIndex(string))
    string = "baa"
    print(palindromeIndex(string))
    string = "aaa"
    print(palindromeIndex(string))
    string = "abc"
    print(palindromeIndex(string))
    string = "abca"
    print(palindromeIndex(string))
