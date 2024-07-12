import sys
import os


def get_chunk(ls,n):

    for x in range(0,n):
        yield ls[x::n]

if __name__ == '__main__':

    file=None

    if len(sys.argv) < 2:
        file=input("Enter path to file: ").strip()

    if not file or  not os.path.exists(file):
        raise Exception("File not found!")

    print("loading bytes....")

    data = open(file,mode="rb").read()

    count = len(data)

    print(count)

    chunksize=40

    form=input("Enter 1- for Hex or 2 - for Plain Text").strip()

    res=""

    lc=0
    for x in range(0, count, chunksize):
        print(data[x:x + chunksize].hex())
        lc+=1
        if lc >=10:
            res=input("Press Enter to Continue or 'q' to quit: ")
            if res == "q":
                exit(0)
            lc=0







