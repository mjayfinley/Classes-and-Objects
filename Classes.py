class Person(object):
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}!")
        self.greeting_count += 1

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, other_person):
        self.friends.append(other_person.name)

    def num_friends(self):
        print(f"{self.name} has {len(self.friends)} friends!")

    def __repr__(self):
        print(f"Person's info: {self.name,self.email,self.phone}.")

    #Bonus - num_unique_people_greeted
    # for loop counting unique greets

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

#jordan.friends.append(sonny)
#sonny.friends.append(jordan)

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
sonny.print_contact_info()
jordan.add_friend(sonny)
jordan.num_friends()
print(f"Sonny has greeted: {sonny.greeting_count} times!")
sonny.__repr__()

#print(jordan.friends)




class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)


car = Vehicle('Nissan','Leaf',2015)

print(car.make, car.model, car.year)
car.print_info()
