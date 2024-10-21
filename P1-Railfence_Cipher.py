def RailFence(txt):
    return txt[::2] + txt[1::2]

string = input("Enter a string: ")
print(RailFence(string))
