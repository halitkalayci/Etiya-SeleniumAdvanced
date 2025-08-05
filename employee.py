class Employee():
    def __init__(self, name):
        self.__name = name

    # Encapsulation uygulanmış bir alanın setter-getter methodları olur.
    # write-only read-only
    def set_name(self,name):
        if len(name) < 2:
            return
        self.__name = name
    def get_name(self):
        return self.__name

# Encapsulation
emp = Employee("Halit")
emp.set_name("Enes")
print(emp.get_name())
