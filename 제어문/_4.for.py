#for문
warrior=['유비','관우','장비','제갈량']
for i in warrior:
    print(i)

i=[(1,2),(3,4),(5,6)]
for (first,last) in i:
    print(first+last)

sum=0    #range가 범위를 뜻함
for a in range(1,5):#(시작숫자, 마지막숫자)=시작숫자-1부터 마지막숫자전까지를 뜻함 EX)(1,5)=0,1,2,3,4
    sum=sum+a
print(sum)

for a in range(2,10):
    for b in range(2,10):
        print(a,"X",b,"=",a*b)
        if b==9:
            print("\n")