N = int(input("Enter N: "))

razrez = int(0)   #сколько разрезов мы сделали
how_now = int(1)  #сколько кусочков сейчас уже есть

if N%2 == 0:pass
if N%2 == 1:
    razrez = razrez+1
    N = N-1

while True:
    if how_now == N:break
    if (how_now<N)and(how_now*2 < N):
        razrez = razrez+1
        how_now = how_now*2
    if (how_now<N)and(how_now*2 > N):
        razrez = razrez+1
        how_now = how_now+ (N-how_now)


print(f"Answer: {razrez}")