import datetime

class cars:
    brand = 'ford'
    base= int(1995)
    def __init__(self, at1, at2 = 'Henry' ):
        self.owner = at2 
        self.name = at1 
    
    def __str__(self):
        return f'{self.name} and {self.brand}'

    def age(self):
        return datetime.datetime.now().year-self.base

firstCar =cars('mustang','erfan')
firstCar.base = int(input(f'pleas enter your year of production {firstCar.owner} :'))
print(f'The age of car is:{firstCar.age()} !!')

firstCar.brand= input('\nenter your car brand:')
print(firstCar)
