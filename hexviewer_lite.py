import sys
import os

if __name__ == '__main__':

    file=None

    if len(sys.argv) < 2:
        file=input("Enter path to file: ").strip()

    if not file or  not os.path.exists(file):
        raise Exception("File not found!")

    print("loading bytes....")

    with open(file,mode="rb") as f:
    # with open(file,encoding='latin-1') as f:

        form = input("enter 1- for Hex and 2- for plain text: ").strip()

        while True:

            data = f.read(1024)

            if not data:
                break

            count = len(data)
            chunksize=40

            res = ""

            if "1" in form:
                for x in range(0, count, chunksize):
                    print(data[x:x + chunksize].hex())

            elif "2" in form:
                for x in range(0,count,chunksize):
                    print(data[x:x+chunksize].decode("latin-1"))

            else:
                print("Invalid Format Choice ",form)


            # print(data.hex(), data.decode("latin-1"))
            res = input("Press H for hex  Enter for next 10 lines or 'q' to quit").strip()

            if res == "q":
                break


