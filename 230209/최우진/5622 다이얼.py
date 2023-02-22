word = list(input())
a = {'A': 2, 'B': 2, 'C': 2}
b = {'D': 3, 'E': 3, 'F': 3}
c = {'G': 4, 'H': 4, 'I': 4}
d = {'J': 5, 'K': 5, 'L': 5}
e = {'M': 6, 'N': 6, 'O': 6}
f = {'P': 7, 'Q': 7, 'R': 7, 'S': 7}
g = {'T': 8, 'U': 8, 'V': 8}
h = {'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

lis = []
for i in word:
    if i == 'A' or i == 'B' or i == 'C':
        lis.append(a[i])
    elif i == 'D' or i == 'E' or i == 'F':
        lis.append(b[i])
    elif i == 'G' or i == 'H' or i == 'I':
        lis.append(c[i])
    elif i == 'J' or i == 'K' or i == 'L':
        lis.append(d[i])
    elif i == 'M' or i == 'N' or i == 'O':
        lis.append(e[i])
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        lis.append(f[i])
    elif i == 'T' or i == 'U' or i == 'V':
        lis.append(g[i])
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        lis.append(h[i])

sumV = 0
for j in lis:
    sumV += j

print(sumV+len(lis))