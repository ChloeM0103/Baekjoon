H , M = map(int,input().split())
if M >= 45:
    print(H , M-45)
else:
    if H == 0:
        print(24 -1 , M+60-45)
    else:
        print(H-1 , M+60-45)
