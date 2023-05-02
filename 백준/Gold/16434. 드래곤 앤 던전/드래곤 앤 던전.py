import sys
import math
n,a = map(int,input().split())

dungun = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

left =1
right = int(1e18)
answer=int(1e18)+1

while left<=right:
    mid = (left+right)//2
    hp_temp = mid
    atk_tmp = a
    for i in range(len(dungun)):
        t, d, h = dungun[i]
        if t==1:
            damage = (math.ceil(h/atk_tmp)-1) * d
            hp_temp-=damage
            if hp_temp<=0:
                break
        else:
            atk_tmp+=d
            hp_temp+=h
            if hp_temp>mid:
                hp_temp=mid

    if hp_temp >0:
        answer = min(answer,mid)
        right=mid-1
    else:
        left=mid+1





print(answer)