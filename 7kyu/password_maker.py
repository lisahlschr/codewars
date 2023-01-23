# One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password by extracting the first letter of each word.

# Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

#     instead of including i or I put the number 1 in the password;
#     instead of including o or O put the number 0 in the password;
#     instead of including s or S put the number 5 in the password.

# Examples:

# "Give me liberty or give me death"  --> "Gml0gmd"
# "Keep Calm and Carry On"            --> "KCaC0"

#My Solution:
def make_password(phrase):
    phrase = phrase.split()
    new_word = ""
    for word in phrase:
        new_word += word[0]
    new_word = new_word.replace("o", "0")
    new_word = new_word.replace("O", "0")
    new_word = new_word.replace("i", "1")
    new_word = new_word.replace("I", "1")
    new_word = new_word.replace("i", "1")
    new_word = new_word.replace("s", "5")
    new_word = new_word.replace("S", "5")
    return new_word
