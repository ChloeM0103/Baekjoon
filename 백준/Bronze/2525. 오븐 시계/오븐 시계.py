A, B= map(int,input().split())
C = int(input())
if B+C<60:
    H = A
    M= B+C
elif B+C==60:
    H = A+1
    M = 0
elif B+C>60:
    H = A + (B+C)//60
    M = (B + C)%60
if H >= 24:
    H = H%24
print (H,M)