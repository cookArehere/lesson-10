class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.lastname}, and my age {self.age}.")

if __name__ == '__main__':
   """
   Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. 
Make another method called talk() which makes prints a greeting from the person containing, 
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
   """

a = Person("Nike", "Rolton", 26)
b = Person("Melis", "Fox", 23)
a.talk()
b.talk()






