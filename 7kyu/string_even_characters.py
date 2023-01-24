# Return a string's even characters.
# Write a function that returns a sequence (index begins with 1) of all the even characters from a string.
# If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".

# For example:

# "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
# "a"             --> "invalid string"


# My Solution:
def even_chars(st):
    if len(st) <2 or len(st) >100:
        return "invalid string"
    else:
        n = 2
        return [st[i] for i in range(1, len(st), n)]
