class Parent(object):
    
    def altered(self):
        print('PARENT altered')

class Test(object):

    def altered(self):
        print('Test altered')

class Boy(Parent):

    def altered(self):
        print('Boy altered()')

class Child(Test, Boy):
    
    def altered(self):
        print('Child, before parent altered()')
        super(Child, self).altered()
        (super(Parent, self))
        print('Child, after parent altered()')

dad = Parent()
son = Child()

dad.altered()
son.altered()
