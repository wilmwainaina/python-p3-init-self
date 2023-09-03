#!/usr/bin/env python3

class Dog:
     def __init__(self, name ,breed="None"):
       self.name="Fido"
       self.breed="Mutt" if breed is None else breed
       print(f"{name} is born!")

     def bark(self):
        print("Woof!")


fido = Dog("Fido")
# Fido is born!

snoopy = Dog("Snoopy")
# Snoopy is born!
    