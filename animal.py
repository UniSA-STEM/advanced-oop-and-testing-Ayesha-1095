"""
File: animal.py
Description:This module defines the main Animal class and its subclasses (Mammal, Reptile, and Bird)
for the zoo management system. Each class represents different types of animals and
their common behaviours.
Author: Ayesha Siddiqa
ID: 110100110
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
class Animal:
    """
    The Animal class is the base class for all animals in the zoo.
    It stores basic details like name, species, age, and diet, and
    includes common actions that all animals can do.
    """
    def __init__(self, name, species, age, dietary_needs):
        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs

    def eat(self):
        """Represents a general eating action for an animal."""
        pass
    def sleep(self):
        """Represents a general sleeping action for an animal."""
        pass
    def make_sound(self):
        """Represents the sound made by an animal."""
        pass
    def __str__(self):
        """Returns a simple string with the animal's information."""
        pass
    def __eq__(self, other):
        """Checks if two animals are the same based on their attributes."""
        pass

class Mammal(Animal):
    """
    Represents mammals in the zoo. Mammals have hair, warm blood, and usually
    give birth to live young. This class extends Animal with extra attributes
    like hair type, blood type, and gestation period.
    """

    def __init__(self, name, species, age, dietary_needs, hair_type, blood_type, gestation_period):
        super().__init__(name, species, age, dietary_needs)
        self._hair_type = hair_type
        self._blood_type = blood_type
        self._gestation_period = gestation_period

    def eat(self):
        """Shows how a mammal eats."""
        pass
    def sleep(self):
        """Shows how a mammal sleeps."""
        pass
    def make_sound(self):
        """Shows the sound a mammal makes."""
        pass
    def __str__(self):
        """Returns details about the mammal."""
        pass
    def __eq__(self, other):
        """Compares two mammals based on their details."""
        pass

class Reptile(Animal):
    """
    Represents reptiles in the zoo. Reptiles are cold-blooded and
    usually have scales. This class adds skin type, blood type,
    and whether the reptile is venomous or not.
    """
    def __init__(self, name, species, age, dietary_needs, skin_type, blood_type, is_venomous):
        super().__init__(name, species, age, dietary_needs)
        self._skin_type = skin_type
        self._blood_type = blood_type
        self._is_venomous = False

    def eat(self):
        """Shows how a reptile eats."""
        pass
    def sleep(self):
        """Shows how a reptile sleeps."""
        pass
    def make_sound(self):
        """Shows the sound a reptile makes."""
        pass
    def __str__(self):
        """Returns details about the reptile."""
        pass
    def __eq__(self, other):
        """Compares two reptiles based on their details."""
        pass
class Bird(Animal):
    """
    Represents birds in the zoo. Birds have feathers and most can fly.
    This class adds feather type, blood type, and whether the bird can fly.
    """

    def __init__(self, name, species, age, dietary_needs, feather_type, blood_type, can_fly):
        super().__init__(name, species, age, dietary_needs)
        self._feather_type = feather_type
        self._blood_type = blood_type
        self._can_fly = False
    def eat(self):
        """Shows how a bird eats."""
        pass
    def sleep(self):
        """Shows how a bird sleeps."""
        pass
    def make_sound(self):
        """Shows the sound a bird makes."""
        pass
    def __str__(self):
        """Returns details about the bird."""
        pass
    def __eq__(self, other):
        """Compares two bird based on their details."""
        pass
