from sys import exit

class Go:

    def __init__(self, Place, Name):
        self.place = Place
        self.name = Name

    def Begin(self):
        if self.place != 'no':
            print('You are going to ' + self.name )
            print('-' * 20)
            print('Now you have reached ' + self.name)
            self.place.working()
            print('-' * 10 + 'Time flies!' + '-----')
            print('Do you want to the next place?')
            print('Yes or No?')
        
            answer = input('>>> ')

            if answer == 'Yes':
                place_next = Map.NextPlace(self.place)
               # print(place_next)
                Go(place_next[0], place_next[1]).Begin()
            else:
                print('Ok, bye!')
                exit(1)
        else:
            print('The place is not exist! Bye...')
            exit(1)

class Lab:

    def working(self):
        print('Now you shoud start working!')
        print('Good luck.')
        
class Canteen:

    def working(self):
        print('Now you begin to eat!')
        print('Take a good while.')
        
class Dormitory:

    def working(self):
        print('You may be tired.')
        print('Now you can take a rest.')

class Map:

    map = {
        'lab': Lab(),
        'canteen': Canteen(),
        'dormitory': Dormitory()
        }

    def __init__(self, Place):
        self.name = Place
        self.place = Map.map.get(self.name, 'no')
        c = Go(self.place, self.name)
        c.Begin()

    def NextPlace(self):
        print('Please input the place you want to:')
        self.place_next = input('>>> ')
        return Map.map.get(self.place_next, 'no'), self.place_next
        
Map('lab')
        
