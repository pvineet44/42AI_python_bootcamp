import sys

args_len = len(sys.argv)
if (args_len > 2):
    print("ERROR")
    sys.exit(0)
n = int(sys.argv[1])
if (n == 0):
    print("I 'm Zero.")
elif (n % 2 == 0):
    print("I 'm Even.")
else:
    print("I 'm Odd.")
