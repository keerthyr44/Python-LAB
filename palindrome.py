def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("hello"))  
print(is_palindrome("racecar"))  
