#while문
meeting = 0
while meeting<=3:
    meeting = meeting+1
    print("Trump met MoonJaeAng %d times" %meeting)
    if meeting==3:
        print("Now Trump is very angry")
        break

#while문 조건
president="""
1. Trump
2. Joe
3. MonJaeAng
4. KimJungEun
숫자를 입력하세요:"""

number=0
while number != 4:#4가 아닐때 까지 반복
    print(president)
    nubmer=int(input())
    if(number==3):
        print("Are you seriously?")

#while문 무한루프
while True:
    print("JaeAng")
