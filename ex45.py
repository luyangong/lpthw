from sys import exit

class Go:

    def __init__(self, Place):
        self.place = Place

    def Begin(self):
        if self.place != None:
            print('You are going to ' + self.place.name)
            print('-' * 20)
            print('Now you have reached ' + self.place.name)
            self.place.working()
            print('-' * 10 + 'Time flies!' + '-----')
            print('Do you want to go to the next place?')
            print('Yes or No?')
        
            answer = input('>>> ')

            if answer == 'Yes':
                place_next = Map.NextPlace(self.place)
                if place_next != self.place:
                    Go(place_next).Begin()
                else:
                    print('You are here already!Bye...')
                    exit(1)
            else:
                print('Ok, bye!')
                exit(1)
        else:
            print('The place is not exist! Bye...')
            exit(1)

class Lab:
    name = 'lab'
    def working(self):
        print('Now you shoud start working!')
        print('Good luck.')
        
class Canteen:
    name = 'canteen'
    def working(self):
        print('Now you begin to eat!')
        print('Take a good while.')
        
class Dormitory:
    name = 'dormitory'
    def working(self):
        print('You may be tired.')
        print('Now you can take a rest.')

class Map:

    map = {
        'lab': Lab(),
        'canteen': Canteen(),
        'dormitory': Dormitory()
        }

    def __init__(self, place):
        self.place = place
    
    def FirstPlace(self):
        return Map.map.get(self.place)

    def NextPlace(self):
        print('Please input the place you want to:')
        self.place_next = input('>>> ')
        return Map.map.get(self.place_next)
        
if __name__ == '__main__':
    print('Please input your place...')
    place_now = input('>>> ')
    a_map = Map(place_now).FirstPlace()
    Go(a_map).Begin()

