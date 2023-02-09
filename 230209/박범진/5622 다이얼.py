N = input()
count = 0
for i in range(len(N)):
    if N[i] == 'A' or N[i] == 'B' or N[i] == 'C':
        count += 3
    elif N[i] == 'D' or N[i] == 'E' or N[i] == 'F':
        count += 4
    elif N[i] == 'G' or N[i] == 'H' or N[i] == 'I':
        count += 5
    elif N[i] == 'J' or N[i] == 'K' or N[i] == 'L':
        count += 6
    elif N[i] == 'M' or N[i] == 'N' or N[i] == 'O':
        count += 7
    elif N[i] == 'P' or N[i] == 'Q' or N[i] == 'R' or N[i] == 'S':
        count += 8
    elif N[i] == 'T' or N[i] == 'U' or N[i] == 'V':
        count += 9
    elif N[i] == 'W' or N[i] == 'X' or N[i] == 'Y' or N[i] == 'Z':
        count += 10
print(count)