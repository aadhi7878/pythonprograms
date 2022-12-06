bits=input("enter bits")
n=len(bits)
sbits='0111110'
ebits='0111110'
ans=""
i=0
count=0
while(i<n):
    if bits[i]=='1':
        count+=1
        ans+=bits[i]
        
    else:
        count=0
        ans+=bits[i]

    if count==5:
        ans+='0'
    i+=1

ans='0111110'+ans+'0111110'
print(ans)
fans=ans.removeprefix('0111110')
fans=fans.removesuffix('0111110')
fans=fans.replace('111110','11111')
print(fans)


