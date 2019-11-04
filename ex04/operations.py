import sys

args_len = len(sys.argv)
if (args_len < 2):
    print("Usage: python operations.py")
    print("Example:")
    print("\tpython operations.py 10 3\n")
    sys.exit(0)
if (args_len > 3):
    print("InputError: too many arguments")
    sys.exit(0)
if (sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0):
    print("InputError: only numbers")
    print("Usage: python operations.py")
    print("Example:")
    print("\tpython operations.py 10 3\n")
    sys.exit(0)
a = int(sys.argv[1])
b = int(sys.argv[2])
sum = a + b
diff = a - b
prod = a * b
if (b == 0):
    mod = "ERROR (modulo by zero)"
    quotient = "ERROR (div by zero)"
else:
    mod = a % b
    quotient = a / (b * 1.0)

print('Sum:         ' + str(sum))
print('Difference:  ' + str(diff))
print('Product:     ' + str(prod))
print('Quotient     ' + str(quotient))
print('Remainder:   ' + str(mod))
