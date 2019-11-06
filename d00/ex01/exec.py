import sys

args_len = len(sys.argv)
if (args_len < 2):
    sys.exit(0)
i = 1
ostr = ""
while (i < args_len):
    ostr += str(sys.argv[i])
    if (i + 1 < args_len):
        ostr += " "
    i += 1
ostr = ostr[::-1]
print(ostr.swapcase())
