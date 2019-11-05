import sys


list_words = []
i = 1
args_len = len(sys.argv)
if (args_len > 3):
    print("ERROR")
    sys.exit(0)

th = sys.argv[args_len - 1]
if (th.isdigit == 0):
    print("ERROR")
    sys.exit(0)

str = sys.argv[1]
total = sum((letter.isalpha() + letter.isspace()) for letter in str)
if (total != len(str)):
    print("ERROR")
    sys.exit(0)
words = str.split()
for word in words:
    if(len(word) > int(th)):
        list_words.append(word)
print(list_words)
