ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait there is not 10 things in that list. let\'s fix that')

stuff = ten_things.split(' ')
more_stuff =['Day', 'Night', 'Song', 'Frisbee', 'Core', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('Adding: ' + next_one)
    stuff.append(next_one)
    print('There \'s %d items now.' % len(stuff))

print('There we go: ' + str(stuff))
print('Let \'s do some things with stuff.')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))