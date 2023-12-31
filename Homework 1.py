# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.
# (приклад у презентації)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name): 
        self.__name = name
        return self.__name
    
    def set_age(self, age): 
        self.__age = age
        return self.__age

person = Person("Mike", 34)

print(person.get_name())
print(person.set_name("John"))

print(person.get_age())
print(person.set_age(27))
