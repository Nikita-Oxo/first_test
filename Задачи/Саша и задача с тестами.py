lr = input("Enter l r: ").split(" ")
l = int(lr[0])
r = int(lr[1])
tests = []
test = int(0)
x = int(1)
mnoj = str(11)

while True:
    if x == 10:
        x=int(1)
        mnoj = f"{mnoj}1"
        continue
    test = x * int(mnoj)

    if l<test<r:
        tests.append(test)
    x = x+1

    if test>r:break


# print(tests)
print(len(tests))