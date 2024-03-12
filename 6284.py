import sys

K, P, N = map(int, sys.stdin.readline().split())

print(int((K * pow(P, N, 1000000007))%1000000007))