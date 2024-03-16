'''
softeer 6255 플레이페어 암호

- 첫 줄에 메시지로 변환할 암호 키가 주어진다.
- 두번째 줄에 메시지를 변환시켜줄 키가 주어진다.
- 받은 키를 바탕으로 암호화 판을 만든다. (5x5 크기) 
    - 이 때 키에서 중복된 알파벳이 있다면, 그 알파벳을 빼고 저장한다.
    - 암호 암호화 판에 남은 자리가 있다면 아직까지 등장하지 않은 알파벳으로 채운다.
- 암호화판이 전부 채워진 후 암호화를 시작한다.
    - 메시지를 두 글자씩 확인하며 순회한다.
    - 두 글자중 앞의 값과 뒤의 값이 같은 알파벳이라면(쌍이라면)
      두 글자 사이에 'X' (쌍이 'XX'인 경우 'Q')를 두 글자 사이에 삽입한다.
    - 이렇게 해서 만들어진 최종 문자열의 마지막에 한글자가 남는다면, 추가로 'X'를 삽입한다.
      마지막 글자가 'X'인 경우도 예외적으로 허용한다 ('XX' 가능)
- 문자의 암호화를 시작한다.
    1. 만약, 두 글자가 표에서 같은 행에 존재한다면, 암호화 판에서 오른쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화한다.
    2. 만약, 같은 행에 존재하지 않으며,같은 열에 존재한다면, 암호화 판에서 아래쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화한다.
    3. 만약, 구 글자가 다른 행, 다른 열에 있다면 서로 위치의 행에 자신 위치의 열에 있는 문자로 암호화한다.
- 암호화된 문자를 출력한다. 
'''

import sys

# 메시지
message = sys.stdin.readline().strip()
# 암호 키
key = sys.stdin.readline().strip()

# 암호화 판을 만든다 5x5 행렬 (중복제거, 순서유지)
password = [[0]*5 for _ in range(5)]

# 조건문을 간단하게 만들어줄 중복제거한 리스트
set_key = list(set(key))

# 알파벳 행렬
alphabet = [i for i in 'ABCDEFGHIKLMNOPQRSTUVWXYZ']

# 중복 제거 로직: 해당 문자 추가하면서 그 문자가 암호화 판 내에 있다면 추가하지 않는다
# 구현: 변수 하나를 만들어서 중복된 문자가 있다면 -1씩 해주고, 그 자리에 다음 문자를 넣음
dup = 0     # 중복제거용 변수
last_pos = tuple()  # 마지막 위치 확인용 튜플
for i in range(len(key)):
    # 중복된 문자가 있다면
    for j in range(5):
        if key[i] in password[j]:
            dup += 1
            break
    # 없다면
    else:
        password[(i-dup)//5][(i-dup)%5] = key[i]
    last_pos = ((i-dup)//5, (i-dup)%5)


# 암호화 판의 나머지 부분 채우기
# 로직: 알파벳 리스트 순회하며 password 내에 없는 알파벳이라면 암호화 판의 마지막 부분부터 채우기
i, j = last_pos[0], last_pos[1]

for alpha in alphabet:

    if alpha not in set_key:
        j += 1

        if i == 5:
            break
        elif j == 5:
            i += 1
            j = 0

        password[i][j] = alpha

# 메시지를 순회하며 앞 글자와 뒤 글자가 같은 글자라면, 'X' or 'Q'를 추가하여 문자열 저장
# 변경한 짝들을 채울 리스트
pair_msg = []

# 2계단씩 건너뛰어야 하므로

for i in range(1, len(message), 2):
    pass
    # if pair:
    #     prev += 1
    #     pair = False
    #
    # i -= prev
    #
    # if
    #
    # if not pair and message[i] != message[i-1]:
    #     pair_msg.append(message[i - 1] + message[i])
    # # 앞, 뒤 같은 글자
    # if not pair and message[i] == message[i-1]:
    #     pair = True
    #     # 'XX' 페어인 경우
    #     if message[i-1] == 'X':
    #         pair_msg.append(message[i-1] + 'Q')
    #     # 그 외 페어인 경우
    #     else:
    #         pair_msg.append(message[i-1] + 'X')

print(pair_msg)