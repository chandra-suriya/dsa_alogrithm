n=int(input())

left = 0
right = n
data  = 0

while(left<=right):
    val = (left+right)//2
    if (val * (val + 1) // 2) >= n:
        data = val

        right = val-1
    else:
        left = val+1

print(data)
n= int(input())
k=1
z=0
while(True):
    if(n>0):
        z+=1
    else:
        break
    n-=k
    k*=2
print(z)



