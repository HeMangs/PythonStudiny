# List

number = [456,343,234,1,23]
number2 = [77,81,549,152,45]
AD = ["caesar", "caitlyn", "jaya", "vane"]

print(number)
print(AD)

number.sort() #오름차순 정렬
number2.reverse() #순서를 거꾸로함

del number2[1] #2번쨰 원소를 지움
number2.append(111) #()안에있는 값을 추가

print(number)
print(number2)

value = [number, number2, AD] #리스트안에 리스트 넣기
print(value)