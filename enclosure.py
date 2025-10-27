"""
File: health_record.py
Description:This module defines the Enclosure class that manages animals' living spaces in the zoo.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
class Enclosure:
    """
    Represents an animal enclosure in the zoo.
    Each enclosure houses only one type of animal,
    such as, Mammal, Bird, Reptile.
    """

    def __init__(self, size, environmental_type, cleanliness_level, animal_type):
        self._size = size
        self._environmental_type = environmental_type
        self._cleanliness_level = cleanliness_level
        self._animal_type = animal_type
        self._animals = []    # list to store animal objects

    def add_animal(self, animal):
        """
        Adds an animal to the enclosure if it matches the allowed type.
        """
        pass

    def report_status(self):
        """
        Display their enclosure info and list of animals.
        """
        pass

    def clean_enclosure(self):
        """
        Resets the cleanliness level.
        """
        pass
