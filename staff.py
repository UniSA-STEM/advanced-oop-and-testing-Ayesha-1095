"""
File: staff.py
Description:This module defines the Staff base class and its subclasses (Zookeeper and Veterinarian)
for managing zoo operations like feeding, cleaning, and health checks.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from animal import Animal, Mammal
from enclosure import Enclosure
from health_record import HealthRecord


class Staff(ABC):
    """
    Abstract base class for zoo staff members.

    This class should not be instantiated directly; only subclasses like
    Zookeeper or Veterinarian should be used.

    Attributes:
        _name (str): Staff member's name.
        __staff_id (int): Unique staff ID (private).
        _role (str): Staff role, e.g., 'Zookeeper' or 'Veterinarian'.
        _assigned_animals (list): List of Animal instances assigned to the staff member.
        _assigned_enclosures (list): List of Enclosure instances assigned to the staff member.
    """
# ====================== Class level constants ================================================
    # Maximum number of animals a staff member can manage
    MAX_ANIMALS_PER_STAFF = 20
    # Maximum number of enclosures a staff member can manage
    MAX_ENCLOSURES_PER_STAFF = 10

# ========================= Constructor ===================================================
    def __init__(self, name: str, staff_id: int, role: str):
        """
        Initialize a new staff member.

        Args:
            name (str): Staff member's name.
            staff_id (int): Unique staff ID.
            role (str): Role of the staff member.
        """
        # Basic staff information
        self.name = name
        self.__staff_id = staff_id
        self.role = role

        # Containers for assigned responsibilities
        self._assigned_animals = []
        self._assigned_enclosures = []
# ======================= Getters =====================================================
    # Return the current value of each staff attribute
    def get_name(self) -> str:
        """Return the staff member's name."""
        return self._name

    def get_staff_id(self) -> int:
        """Return the staff member's unique ID."""
        return self.__staff_id

    def get_role(self) -> str:
        """Return the staff member's role."""
        return self._role

    def get_assigned_animals(self) -> list[Animal]:
        """Return a copy of the list of assigned animals."""
        return list(self._assigned_animals)

    def get_assigned_enclosures(self) -> list[Enclosure]:
        """Return a copy of the list of assigned enclosures."""
        return list(self._assigned_enclosures)

# ====================== Setters =======================================================
    # Validate and set new values for staff attributes
    def set_name(self, name: str) -> None:
        """
        Set a new name for the staff member.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is empty.
        """
        # Validate type
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        # Validate not empty
        if name.strip() == '':
            raise ValueError('Name cannot be an empty string.')
        self._name = name

    def set_role(self, role: str) -> None:
        """
         Set a new role for the staff member.

        Raises:
            TypeError: If role is not a string.
            ValueError: If role is empty.
        """
        # Validate type
        if not isinstance(role, str):
            raise TypeError('Role must be a string.')
        # Validate not empty
        if role.strip() == '':
            raise ValueError('Role cannot be an empty string.')
        self._role = role

# ====================== Properties ======================================================
    # Define properties for attribute access
    name = property(get_name, set_name)
    staff_id = property(get_staff_id)    # Read only
    role = property(get_role, set_role)
    assigned_animals = property(get_assigned_animals)  # Read only copy
    assigned_enclosures = property(get_assigned_enclosures) # Read only copy

# ====================== Methods ===========================================================
    # Methods for assigning animals and enclosures to staff members
    def assign_animal(self, animal: Animal) -> str:
        """
        Assigns an Animal instance to the staff member.

        Args:
            animal (Animal): The animal to assign.

        Raises:
            TypeError: If the argument is not an Animal instance.
            ValueError: If the animal is already assigned.

        Returns:
            str: Confirmation message after assignment
        """
        # Ensure only Animal instances are assigned
        if not isinstance(animal, Animal):
            raise TypeError('Animal must be an Animal instance.')

        # Avoid duplicate assignment
        if animal in self._assigned_animals:
            raise ValueError(f'{animal.name} the {animal.species} is already assigned.')

        # Enforce maximum animals limit
        if len(self._assigned_animals) >= self.MAX_ANIMALS_PER_STAFF:
            raise ValueError('Cannot assign more animals to this staff member.')

        # Assign the animal
        self._assigned_animals.append(animal)
        return f'{animal.name} the {animal.species} has been assigned.'

    def assign_enclosure(self, enclosure: Enclosure) -> str:
        """
        Assigns an Enclosure instance to the staff member.

        Args:
            enclosure (Enclosure): The enclosure to assign.

        Raises:
            TypeError: If the argument is not an Enclosure instance.
            ValueError: If the enclosure is already assigned.

        Returns:
            str: Confirmation message after assignment.
        """
        # Ensure only Enclosure instances are assigned
        if not isinstance(enclosure, Enclosure):
            raise TypeError('Enclosure must be an Enclosure instance.')

        # Avoid duplicate assignment
        if enclosure in self._assigned_enclosures:
            raise ValueError(f'{enclosure.environmental_type} enclosure is already assigned.')

        # Ensure maximum enclosure limit
        if len(self._assigned_enclosures) >= self.MAX_ENCLOSURES_PER_STAFF:
            raise ValueError('Cannot assign more enclosures to this staff member.')

        # Assign the enclosure
        self._assigned_enclosures.append(enclosure)
        return f'{enclosure.environmental_type} enclosure has been assigned.'

# ================================ Abstract Method ===============================================
    # This method must be implemented by all subclasses
    @abstractmethod
    def perform_duties(self) -> str:
        """
        Abstract method that must be implemented by subclasses.
        Each staff subclass defines its role-specific duties (feeding, cleaning, health checks, etc.)
        """
        pass
# =============================== String Method ==================================================
    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the staff member.

        Returns:
            - Name
            - Staff ID
            - Role
            - List of assigned animals (or 'None')
            - List of assigned enclosures (or 'None')
        """
        # Generate human-readable summary of staff and assignments
        animal_list = ', '.join([f'{a.name} ({a.species})' for a in self._assigned_animals]) \
                    if self._assigned_animals else 'None'
        enclosure_list = ', '.join([f'{e.environmental_type} enclosure' for e in self._assigned_enclosures]) \
                    if self._assigned_enclosures else 'None'

        return (f'Staff Name: {self._name}\n'
                f'Staff ID: {self.__staff_id}\n'
                f'Role: {self._role}\n'
                f'Assigned Animals: {animal_list}\n'
                f'Assigned Enclosures: {enclosure_list}\n')

# ====================== Equality =========================================================
    def __eq__(self, other) -> bool:
        """
        Compare staff objects by their unique staff_id.

        Args:
            other (Staff): Another staff object to compare.

        Returns:
            bool: True if both staff members have the same ID, False otherwise.
        """
        # Compare staff objects using unique ID
        if not isinstance(other, Staff):
            return False
        return self.__staff_id == other.__staff_id



class Zookeeper(Staff):
    """
    Represents a zookeeper responsible for feeding animals and cleaning enclosures.
    Zookeepers make sure animals are fed on time and that their enclosures are kept clean.
    """

    def __init__(self, name: str, staff_id: int):
        """
        Initializes a Zookeeper object by calling the parent Staff class constructor.

        Args:
            name (str): The name of the zookeeper.
            staff_id (int): Unique ID assigned to the zookeeper.
        """
        # Call the parent class constructor and set the role to "Zookeeper"
        super().__init__(name, staff_id, role='Zookeeper')

    def feed_animal(self, animal: Animal) -> str:
        """
        Feeds an assigned animal.

        Args:
            animal (Animal): The animal to feed.

        Raises:
            TypeError: If the argument is not an Animal instance.
            ValueError: If the animal is not assigned to this staff member.

        Returns:
            str: Confirmation message indicating the feeding action.
        """
        # Make sure the argument is a valid Animal instance
        if not isinstance(animal, Animal):
            raise TypeError('Animal must be an Animal instance.')

        # Check if this animal is assigned to this zookeeper
        if animal not in self._assigned_animals:
            raise ValueError(f'{animal.name} the {animal.species} is not assigned to {self.name}.')

        # Return a message confirming the feeding action
        return f'{self.name} ({self.role}) feeds {animal.name} the {animal.species}.'

    def clean_enclosure(self, enclosure: Enclosure) -> str:
        """
        Cleans an assigned enclosure by calling the enclosure's clean method.

        Args:
            enclosure (Enclosure): The enclosure to clean.

        Raises:
            TypeError: If the argument is not an Enclosure instance.
            ValueError: If the enclosure is not assigned to this staff member.

        Returns:
            str: Confirmation message indicating the cleaning action.
        """
        # Make sure the argument is a valid Enclosure instance
        if not isinstance(enclosure, Enclosure):
            raise TypeError('Enclosure must be an Enclosure instance.')

        # Check if this enclosure is assigned to this zookeeper
        if enclosure not in self._assigned_enclosures:
            raise ValueError(f'{enclosure.environmental_type} enclosure is not assigned to {self.name}.')
        # Clean the enclosure by calling the clean enclosure method from enclosure class
        cleaning_result = enclosure.clean_enclosure()

        # Return a message confirming the cleaning action
        return f'{self.name} ({self.role}) cleaned the {enclosure.environmental_type} enclosure {cleaning_result}.'

    def perform_duties(self) -> str:
        """
        Performs the daily duties of a zookeeper, including feeding animals
        and cleaning enclosures.

        Returns:
            str: Summary of performed duties.
        """
        # Prepare a readable list of animals and enclosures handled by the zookeeper
        fed_animals = ', '.join([f'{a.name} ({a.species})' for a in self._assigned_animals]) \
            if self._assigned_animals else 'None'

        clean_enclosures = ', '.join([f'{e.environmental_type} enclosure' for e in self._assigned_enclosures]) \
            if self._assigned_enclosures else 'None'

        # Return a summary of tasks completed
        return (f"{self.name} ({self.role}) performed duties.\n"
                f"Feed Animals: {fed_animals}\n"
                f"Cleaning Enclosures: {clean_enclosures}\n")



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

    def perform_duties(self):
        pass
