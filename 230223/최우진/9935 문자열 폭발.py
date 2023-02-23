S = input()
bomb = input()

ST = []
bomb_len = len(bomb)

for i in range(len(S)):
    ST.append(S[i])
    if ''.join(ST[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            ST.pop()

if ST:
    print(''.join(ST))
else:
    print('FRULA')