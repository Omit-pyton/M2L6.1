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
        return name
    
    def set_age(self, age): 
        return age
