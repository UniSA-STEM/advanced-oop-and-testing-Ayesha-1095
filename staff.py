"""
File: staff.py
Description:This module defines the Staff base class and its subclasses (Zookeeper and Veterinarian)
for managing zoo operations like feeding, cleaning, and health checks.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
class Staff:
    """
    Base class for zoo staff members.
    """
    def __init__(self, name, staff_id, role):
        self._name = name
        self._staff_id = staff_id
        self._role = role
        self._assigned_animals = []
        self._assigned_enclosures = []

    def assign_animal(self, animal):
        """Assigns an animal to the staff member."""
        pass

    def assign_enclosure(self, enclosure):
        """Assigns an enclosure to the staff member."""
        pass

    def __str__(self):
        """Returns staff member details."""
        pass

class Zookeeper(Staff):
    """
    Represents a zookeeper responsible for feeding animals and cleaning enclosures.
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, role = 'Zookeeper')

    def feed_animal(self, animal):
        """Feeds the assigned animal."""
        pass

    def clean_enclosure(self, enclosure):
        """ Cleans the assigned enclosure."""
        pass


class Veterinarian(Staff):
    """
    Represents a veterinarian responsible for animal health care and checks.
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, role = 'Veterinarian')

    def conduct_health_check(self, animal):
        """
        Conducts a health check on the given animal.
        """
        pass
    def update_health_record(self, animal, record):
        """
        Updates the animal's health record with new notes or treatment.
        """
        pass
