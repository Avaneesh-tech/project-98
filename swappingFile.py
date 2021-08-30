
def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open("sample1.txt") as a:
    data_a = a.read()

	with open("sample2.txt") as b:
    data_b = b.read()

    with open("sample1.txt") as a:
    a.write(data_b)

    with open("sample2.txt") as b:
    b.write(data_a)

swapFileData()