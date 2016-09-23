class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


a = Student()
a.birth = 1987
print(a.age)
print(a.birth)
a.age = 22
print(a.age)