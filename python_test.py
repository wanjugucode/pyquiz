x=[100,110,120,130,140,150]
y=[i*5 for i in x]
print(y)


def divisible_by_three(n):
    for g in range(1,n):
        if g%3==0:
            print(g)
        
            
divisible_by_three(30)


def flatten_list(*args):
    for j in args:
        return j
flatten_list( [[1,2],[3,4],[5,6]])

# def smallest(*args):
#     for y in args:
#        if y <y.value:
#            return y
# smallest(3,6,8,2,4,1,5,7)

# def remove_duplicate(*x):
#     m=set(x)
#     return m
# remove_duplicate( 'a','b','a','e','d','b','c','e','f','g','h')


def divisible_by_seven():
    for i in range(100,200):
       if i %7==0:
           return i
divisible_by_seven()

# def greet():
#     students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}],
#     for student in students:
#         print(student)



class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        A= self.length*self.width
        return A
    def perimeter(self):
        i=(self.length+self.width)
        P=i*2
        return P
    
