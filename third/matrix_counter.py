#pragma for matrix couting
a = [[0]*3 for _ in range(3)]


m = 0
for i in range(3):
    for j in range(3):
        m = m+1
        a[i][j] = m
        print(a[i][j], " ", end=" ")
    print("\n")

m = 0
for i in range(3):
    for j in range(3):
        m = m+1
        a[i][j] = int(input(f"select {m} element: "))

for i in range(3):
    for j in range(3):
        print(a[i][j], " ", end = " ")
    print("\n")

resultat = int(0)



for prohod in range(3):
    matrix2x2_1 = int(0)
    matrix2x2_2 = int(0)
    matrix2x2_3 = int(0)
    matrix2x2_4 = int(0)
    for i in range(3):
        for j in range(3):
            if j == prohod:continue
            if i == 0: continue
            if matrix2x2_1 == 0:
                matrix2x2_1 = a[i][j]
                print(f"matrix2x2_1 = {a[i][j]}")
                continue
            if matrix2x2_2 == 0:
                matrix2x2_2 = a[i][j]
                print(f"matrix2x2_2 = {a[i][j]}")
                continue
            if matrix2x2_3 == 0:
                matrix2x2_3 = a[i][j]
                print(f"matrix2x2_3 = {a[i][j]}")
                continue
            if matrix2x2_4 == 0:
                matrix2x2_4 = a[i][j]
                print(f"matrix2x2_4 = {a[i][j]}")
                continue

    resultat = resultat + a[0][prohod] * ((-1)**(prohod)) * ((matrix2x2_1*matrix2x2_4)-(matrix2x2_2*matrix2x2_3))

print(resultat)
