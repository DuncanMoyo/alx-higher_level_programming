#!/usr/bin/python3

def reverse_alphabet():
    for i in range(ord('z'), ord('a') - 1, -1):
        if (i % 2 == 0):
            print(chr(i), end="")
        else:
            print(chr(i).upper(), end="")

if __name__ == "__main__":
    reverse_alphabet()
