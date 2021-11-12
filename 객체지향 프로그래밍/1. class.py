# class

class Horse: #생성자 (Constructor)
    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xposition = xpos
        self.yposition = ypos
        self.velocity = 0
        

if __name__ == '__main__': # 생성자를 호출하여 각 객체를 생성
    danbi = Horse(5,160,'brown',0,0) #매개변수 목록과 실제전달 인자 순서를 맞게 해야함

    
class Alphabets:
    __str = "" # __str이라는 변수 선언
    def __init__(self,text):
        self.text = text
        Alphabets.__str += text
    def print_class_variable(self):
        print(Alphabets.__str)

if __name__ == '__main__':
    o1 = Alphabets('p')
    o2 = Alphabets('y')
    o3 = Alphabets('t')
    o4 = Alphabets('h')
    o5 = Alphabets('o')
    o6 = Alphabets('n')

    o1.print_class_variable() # o1과 o5는 같은 메소드인 print_class_variable을 호출하지만 같은 결과를 냄
    o5.print_class_variable() # __str변수를 같이 공유하기 때문