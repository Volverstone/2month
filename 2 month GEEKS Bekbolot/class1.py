class Hello:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  (f'{self.name}\n'
                 f'{self.age}')


class Hi(Hello):
    def __init__(self, name, age):
        super().__init__(name, age)




person = Hi('Erzhan', 17)
print(person)