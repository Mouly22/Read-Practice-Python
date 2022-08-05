#line 353, 324, 116, 152, 

#ekta class hocche chosmar frame er blueprint, er ei blueprint theke amra infinity number er chosma banaite parbo. So, ekta chosma holo ekta object.
from types import MemberDescriptorType


class Personal_info():
    def __init__(self):
        print('We are writing on the \'init\' method hehe.')
        print('The output of self will be different for different object',self)


#============================================
obj1 = Personal_info()
obj2 = Personal_info()
print('obj1 created', obj1)
print('obj2 created', obj2)

#output:
# We are writing on the 'init' method hehe.
# The output of self will be different for different object <__main__.Personal_info object at 0x100e27b50>
# We are writing on the 'init' method hehe.
# The output of self will be different for different object <__main__.Personal_info object at 0x100f8e230>
# obj1 created <__main__.Personal_info object at 0x100e27b50>
# obj2 created <__main__.Personal_info object at 0x100f8e230>

class Address:
    def __init__(self, name, place):
        self.name = name                  #self basically obj k refer korar jonno use kora hoy, amra self likhe object der k access kori.
        self.place = place
        print(self.place)

#==========================================
obj1 = Address('Mouly', 'Bogura')
obj2 = Address('Moitry', 'Sherpur')
print(obj1.place)
obj1.place = 'Dhaka'
print(obj1.place)
#Output:
# Bogura
# Sherpur
# Bogura
# Dhaka

#ekhon boiler code e evabe change na kore amra method call dite pari.. method call dile amrader boiler code e barbar evabe print dite hbena

class U_Address:
    def __init__(self, name, place):
        self.name = name              #instance variable         
        self.place = place            #instance variable
        print(self.place)
        #print(self.place)
        #self basically obj k refer korar jonno use kora hoy, amra self likhe object der k access kori.

    def details(self):               #instance method
        print(f'Name: {self.name} Place: {self.place}')
        #eta print dilei shudhu hbena.. eta k amader boiler code e jokhon kono obj er reference e call dewa hbe tokhon e shudhu hbe

#==========================================
obj1 = U_Address('Mouly', 'Bogura')
obj2 = U_Address('Moitry', 'Sherpur')
obj1.details()                     #Name: Mouly Place: Bogura
obj2.details()                     #Name: Moitry Place: Sherpur
obj1.place = 'Dhaka'
obj1.details()                     #Name: Mouly Place: Dhaka (automatically method er maddhome shudhu jei obj er jonno call dewa hoilo tar value change hoye gelo)

#output:
# Bogura                        #ekhane bogura keno dhaka update hoilo na? karon amra obj1 er jonno init e ja call dicchi seita method e change kora jabe,  but init e oitai thakbe, update hbena
# Sherpur
# Name: Mouly Place: Bogura
# Name: Moitry Place: Sherpur
# Name: Mouly Place: Dhaka


class Phonebook:
    def __init__(self,name, number):
        self.name = name
        self.number = number

    def add_info(self, sex = 'Male'):
        self.sex = sex

    def show_info(self):
        print(f'Name: {self.name} Sex: {self.sex} Number: {self.number}')

a1 = Phonebook('Nahin', 1245909)
a1.add_info('Female')
a1.show_info()
a1.add_info('Confused')
a2 = Phonebook('Mahim', 2346990)
a2.add_info()
a2.show_info()
print(a1.__dict__)     #.__dict__ diye key:value akare dekha jay
a1.show_info()
#Output:
# Name: Mahim Sex: Male Number: 2346990
# Name: Nahin Sex: Female Number: 1245909
# {'name': 'Nahin', 'number': 1245909, 'sex': 'Confused'}
# Name: Nahin Sex: Confused Number: 1245909


class Cat:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def show(self):
        print(f'{self.color} cat is {self.position}')

c1 = Cat('White', 'sleeping')
c1.show()
c1.position = 'Dancing'
c1.show()

#Output:
# White cat is sleeping
# White cat is Dancing

class Job:
    def __init__(self, name, uni):
        self.name = name
        self.uni = uni 
        self.pyear = 2025
        self.a = ''

    def add_info(self, gender):
        self.gender = gender
        if self.gender == "Female":
            self.a = 'Stand on the right side.'
        elif self.gender == "Male":
            self.a = 'Stand on the left side.'

    def uni_compare(self, val):
        if self.uni == val.uni:                 #Imp****. (Pass by reference)[Ekhane c1 recieve hocche self diye, r c2 recieve hocche val diye!!]
            print('Yup! Same.')
        else:
            print("NO! Next.")

    def show(self):
        print(f"Name: {self.name} University: {self.uni} Passing year: {self.pyear}")
        print(self.a)   
  

c1 = Job('Jamal','BUET')
c2 = Job('Fariha', 'BRACU')
c2.add_info('Female')
c2.show()
c1.uni_compare(c2)                #(main jinish hocche, c2 to arekta object. ami jokhon c2 k pass korchi tar mane ami c2 object er location reference hisebe pass korchi, c2 whole table ta pathaye dicchina.. ami jei location ta pass korchi sei location diye c1 object 'uni_compare' method er maddhome c2 table er sob value access korte parbe.)
#Output:
# Name: Fariha University: BRACU Passing year: 2025
# Stand on the right side.
# NO! Next.


#****Pass by value/Pass by reference****
#Now, what is pass by value? -> When we are basically passing a value rather than a location/reference, it is pass by value. Amra jokhon integer or string pass kori seita pass by value akare jay.
#Pass by Reference -> When we are passing a reference/location, rather than simply a value, it is pass by reference. List k amra pass by reference bisebe pathai.
class Worklife:
    def __init__(self, name, dept, office):
        self.name = name
        self.dept = dept
        self.office = office

    def residence(self, no, plc):
        no += 4
        places1 = plc
        plc[0] = 'Bhola'
        print('Method inside', no)
        print('Method inside',places1)


places = ['Chittagong','Bogura','Dhaka','Sherpur']
c1 = Worklife('Mina','CSE','Gulshan1')
x = 22
c1.residence(x, places)
print('Method outside',x)
print('Method outside', places)            

#OUTPUT:
# Method inside 26
# Method inside ['Bhola', 'Bogura', 'Dhaka', 'Sherpur']
# Method outside 22
# Method outside ['Bhola', 'Bogura', 'Dhaka', 'Sherpur']
#see, for pass by reference, list er vitoreo change hoye gese bhola.

#method overloading:
class Badge:
    def __init__(self, name):
        self.name = name
        self.val = 0

    def calculate(self, *args):
        x = 2
        #print(args)       -> (2, 3, 4, 6, 8, 3) args e output tuple hisebe thake.
        for elm in args:
            x = x * elm
        self.val = x

    def show(self):
        print(f'Name:{self.name}')
        print(f'Amount:{self.val}')


b1 = Badge('mouly')
b1.calculate(2,3,4,6,8,3)
b1.show()


#Operator Overloading te amra obj der plus/minus eisob kore thaki, jeita normal vabe kora possible hoy na tai.
class Operator:
    def __init__(self, one):
        self.one = one
        self.res = ''

    def __add__(self, other):
        self.res = self.one + other.one
        return(self.res)

    def __lt__(self, other):
        if self.one > other.one:
            return('num2 is not big.')
        elif self.one < other.one:
            return('num2 is bigger.')

    def __add__(self, other):
        self.res = self.one + other.one
        return(self.res)

num1 = Operator(10)
num2 = Operator(34)
str1 = Operator('Mou')
str2 = Operator('ly')
print(num1 + num2)       #(num1.__add__num2)
print(num1 < num2)
print(str1 + str2)



class data:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if self.x == other.x:
            return('Both are equal')
        else:
            return("not equal")


val1 = data(30)
val2 = data(30)
print(val1 == val2)

class House:
    def __init__(self, door, window):
        self.door = door
        self.window = window

    def view(self):
        print(f'The house has {self.door} door(s) and {self.window} window(s)')

    def __add__(self, other):
        n_door = self.door + other.door
        n_window = self.window + other.window
        h3 = House(n_door, n_window)
        return h3

h1 = House(2,6)
h2 = House(1,4)
h1.view()
h2.view()
h3 = h1 + h2
h3.view()

class School:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printinfo(self):
        print(f'{self.name} is {self.age} years old.')

b1 = School('Rouja', 5, 'Female')
b1.printinfo()
print(b1.name)
print(b1.gender)         #these are public variables as we can access them from outside of the class.

#However, .__variable makes a 'private' variable and we can access it only within the class but not outside of the class.
class School:
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.gender = gender
    
    def printinfo(self):
        print(self.__name)                 #we can access it from here as it is within the class.
        #print(f'{self.__name} is {self.age} years old.')

b1 = School('Rouja', 5, 'Female')
b1.printinfo()
#print(b1.__name)                  #AttributeError: 'School' object has no attribute '__name'. 
print(b1.gender)                   #we still can access it as it is a public class

#ALSO**,

class School:
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.gender = gender
    
    def __printinfo(self):         
        print(self.__name)               
       

b1 = School('Rouja', 5, 'Female')
#b1.printinfo()
#print(b1.__name)               
print(b1.gender)
#output: AttributeError: 'School' object has no attribute 'printinfo'. so if we make a method private, we also can not access it from outside of the class.
#however, we need to see what exactly happened to this private method.
print(dir(b1))
#output:
#['_School__name', '_School__printinfo', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'gender']
#Here we can see that, python has changed the private method and variable to _class__variable name.
#So, in python, it is pertially possible to achieve private methods and variables.

class Family:
    def __init__(self):
        self.cousins = 'Mouly'
        self.age = 22

    def show_members(self):
        print(f'{self.cousins} is {self.age} years old.')

m1 = Family()
m2 = Family()
m1.show_members()

#==================
class Friends:
    def __init__(self):
        self.obj = Family()

    def showw(self):
        print(self.obj.cousins)

f2 = Friends()
f2.showw()
#===============
#We can use one class as an object of another class like the above.

class School:
    def __init__(self, name, id, age, gender):
        self.name = name
        self.__id = id
        self.age = age
        self.gender = gender
    
    def printinfo(self):
        print(f'{self.name}\'s ID is {self.__id} and she is {self.age} years old.')

    def update_id(self, id):
        if id > 0:
            self.__id = id
        else:
            print('Invalid id. Enter id again.')
    


b1 = School('Rouja', 2001010, 5, 'Female')
b1.printinfo()
#print(b1.__id)        # 'School' object has no attribute '__id' (we are protecting id from the outside of the class.)
b1.__id = 33           #we can not update this id from the outside of the class.
b1.printinfo()         #Rouja's ID is 2001010 and she is 5 years old.
print(b1.__dict__)     #{'name': 'Rouja', '_School__id': 2001010, 'age': 5, 'gender': 'Female', '__id': 33}
b1.update_id(21)
b1.printinfo()         #Rouja's ID is 21 and she is 5 years old.

#There is a set-get method for updating anything in oop.

class School:
    def __init__(self, name, id, age, gender):
        self.name = name
        self.__id = id
        self.age = age
        self.gender = gender
    
    def printinfo(self):
        print(f'{self.name}\'s ID is {self.__id} and she is {self.age} years old.')

    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            print('Invalid id. Enter id again.')
    def get_id(self):
        return(f'ID is {self.__id}')
    


b1 = School('Rouja', 2001010, 5, 'Female')
b2 = School('Fatema',201432, 12, 'female') 
b1.printinfo()        
b1.set_id(34)
b2.set_id(55555)
#print(b1.get_id())
b1.printinfo() 
#print(b2.get_id())
b2.printinfo() 
#ekhane method er through ami id k nilam and access korlam.

#output:
# Rouja's ID is 21 and she is 5 years old.
# Rouja's ID is 2001010 and she is 5 years old.
# Rouja's ID is 34 and she is 5 years old.
# Fatema's ID is 55555 and she is 12 years old.

