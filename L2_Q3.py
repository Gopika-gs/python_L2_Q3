string = input("Enter the string  ")
len = len(string)
print("Length of string is(including space)",len)
wlen = len - string.count(" ")
print("Length of string is(without including space)",wlen)