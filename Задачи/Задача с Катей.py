n = int(input("n: "))
t = int(input("t: "))
f = str(input("floors: ")).split(" ")
p = int(input("people: "))

c = len(f)

if (p - int(f[0]) > t) or (int(f[c-1])-p>t):
    if int(f[c-1])-p > p - int(f[0]):
        print(f"t = {(p - int(f[0]))*2+int(f[c-1])-p}")
    else: print(f"t = {(int(f[c-1])-p)*2+p - int(f[0])}")
else: print(f"t = {int(f[c-1]) - int(f[0])}")