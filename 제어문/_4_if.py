#if문
c="sweet"
if c=="sweet":
 print("삼킬듯")
else:
 print("뱉는다")
 
#연산자
x=1
y=7

if(x<7):
    print("true")
else:
    print("false")

# x in s 문
box=['candy','penis','ass']

if 'penis' in box:
    print("오예")
else:
    print("쉣")

# and, or, not문
a=1
b=0

if a and b:
    print("and")
elif a==0:
    print("a=0")
elif b==1:
    print("b=1")
elif not a: #a가 참이면 결과는 거짓이라는 것
    print("not a")
else:
    print("OR")
