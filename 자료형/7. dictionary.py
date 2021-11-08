# dictionary

dic = {1 : "Netflix", 2 : "drama", 3 : "Squid Game", 4 : "Myname"}

print(dic[1])
print(dic[2], dic[4])

print(dic.keys()) #dictionary안에 있는 키들을 출력
print(0 in dic.keys()) #dictionary안에 0이라는 키가 있는지 출력
print(dic.values()) #dictionary 안에 있는 값들을 출력
print(dic.items()) #dictionary 안에있는 값들을 키와 함께 출력