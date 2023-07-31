# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.
# (приклад у презентації)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_name(self):
        return self._name

    def _get_age(self):
        return self._age
