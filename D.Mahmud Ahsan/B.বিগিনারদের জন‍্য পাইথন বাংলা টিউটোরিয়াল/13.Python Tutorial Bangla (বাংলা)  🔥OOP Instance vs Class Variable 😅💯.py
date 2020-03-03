# Class variable and Instance variable Details
class Alien:
    legs = 5 # class variable

    def __init__(self, name):
        self.name = name # instance variable




## Instantiation
alien1 = Alien("Maven")
alien2 = Alien("Woven")


print(alien1.name, alien2.name) #accessing instance variable
print(alien1.legs, alien2.legs)# accessing class variable

# Alien.legs = 10
# print(alien1.legs, alien2.legs)

alien1.legs = 99
print(alien1.legs, alien2.legs)
