import datetime

class cars:
    brand = 'ford'
    base= int(1995)
    def __init__(self, at1, at2 = 'Henry' ):
        self.owner = at2
        print('im hearrrr') 
        self.name = at1 
        
    
    def __str__(self):
        return f'{self.name} and {self.brand} and hearrrrr'

    def age(self):
        return datetime.datetime.now().year-self.base

firstCar =cars('non','shit!')
firstCar.base = int(input(f'pleas enter your year of production {firstCar.owner} :'))
if (2 == 1):
    print ('and not hearrrr')
firstCar.brand= input('\nenter your car brand:')


