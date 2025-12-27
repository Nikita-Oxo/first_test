nk = input("enter n k: ").split(" ")
a = input("enter numbers: ").split(" ")

n = int(nk[0])
k = int(nk[1])

one_char = []
two_chars = []
three_chars = []
four_chars = []

uvelich = int(0)

for i in range(n):
    chars = int(len(str(a[i])))
    if chars == 1:
        one_char.append(a[i])
        continue
    elif chars == 2:
        two_chars.append(a[i])
        continue
    elif chars == 3:
        three_chars.append(a[i])
        continue
    elif chars == 4:
        four_chars.append(a[i])
        continue

one_char.sort()
two_chars.sort()
three_chars.sort()
four_chars.sort()

for i in range(len(three_chars)):
    if k ==0:break
    uvelich = uvelich+(int(str(f"9{str(one_char[i])[1]}{str(one_char[i])[2]}")) - int(three_chars[i]))
    three_chars[i] = f"9{str(one_char[i])[1]}{str(one_char[i])[2]}"
    k = k-1

for i in range(len(two_chars)):
    if k == 0: break
    uvelich = uvelich + (int(str(f"9{str(two_chars[i])[1]}")) - int(two_chars[i]))
    two_chars[i] = f"9{str(two_chars[i])[1]}"
    k = k-1

for i in range(len(three_chars)):
    if k ==0:break
    uvelich = uvelich+(int(str(f"{str(one_char[i])[0]}9{str(one_char[i])[2]}")) - int(three_chars[i]))
    three_chars[i] = f"{str(one_char[i])[0]}9{str(one_char[i])[2]}"
    k = k-1

for i in range(len(one_char)):
    if k == 0: break
    uvelich = uvelich + (9 - int(one_char[i]))
    one_char[i] = "9"
    k = k - 1
    
for i in range(len(three_chars)):
    if k ==0:break
    uvelich = uvelich+(int(str(f"{str(one_char[i])[0]}{str(one_char[i])[1]}9")) - int(three_chars[i]))
    three_chars[i] = f"{str(one_char[i])[0]}{str(one_char[i])[1]}9"
    k = k-1

for i in range(len(two_chars)):
    if k == 0: break
    uvelich = uvelich + (int(str(f"{str(two_chars[i])[1]}9")) - int(two_chars[i]))
    two_chars[i] = f"{str(two_chars[i])[1]}9"
    k = k-1


print(uvelich)