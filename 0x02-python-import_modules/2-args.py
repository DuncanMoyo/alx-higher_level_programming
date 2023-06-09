#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    if leng == 0:
        print("0 arguments.")
    elif leng == 1:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print(f"{leng} arguments:")

        for i in range(1, leng + 1):
            print("{}: {}".format(i, sys.argv[i]))
