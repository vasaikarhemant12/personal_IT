p = input("enter the string:")
rev = ''
for i in range(len(p) - 1, -1, -1):
    rev = rev + p[i]
if p == rev:
    print("Given string {} is palindrom".format(p))
else:
    print("Given String {} is not palindrom".format(p))
