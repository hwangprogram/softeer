import sys

msg = sys.stdin.readline().strip()
pw_key = list(sys.stdin.readline().strip())

alphabet = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
set_key = set(pw_key)
pw_key = list(set_key)
arr = [[] * i for i in range(5)]

for i in range(len(pw_key)):
    r1 = i // 5
    arr[r1].append(pw_key[i])
remain = list(set(alphabet) - set_key)

for i in range(len(remain)):
    r2 = (i + len(pw_key)) // 5
    if r2 == 5:
        break
    arr[r2].append(remain[i])

pair = False
pair_msg = []
for i in range(len(msg)):
    if pair:
        pair = False
        continue
    if not pair and i == len(msg) - 1:
        pair_msg.append(msg[i] + 'X')
    if msg[i] == msg[i+1]:
        if msg[i] == 'X':
            pair_msg.append(msg[i] + 'Q')
        else:
            pair_msg.append(msg[i] + 'X')
    else:
        pair_msg.append(msg[i] + msg[i+1])
        pair = True

for m in pair_msg:
    target = []
    a, b = m[0], m[1]
    for i in (a, b):
        for j in range(5):
            for k in range(5):
                if i == arr[j][k]:
                    target.append([j, k])

    a_pos, b_pos = target[0], target[1]
    if a_pos[0] == b_pos[0]:
        a_pos[1] += 1
        b_pos[1] += 1
        ans = arr[a_pos[0]][a_pos[1]%5] + arr[b_pos[0]][b_pos[1]%5]
    elif a_pos[1] == b_pos[1]:
        a_pos[0] += 1
        b_pos[0] += 1
        ans = arr[a_pos[0]%5][a_pos[1]] + arr[b_pos[0]%5][b_pos[1]]
    else:
        ans = arr[a_pos[0]][b_pos[1]] + arr[b_pos[0]][a_pos[1]]
print(ans)