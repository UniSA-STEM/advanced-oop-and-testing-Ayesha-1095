"""
File: zoo.py
Description: Manages all animals, enclosures, and staff in the zoo.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from enclosure import Enclosure
from staff import Staff

class Zoo:
    """
    Represents the entire zoo system, responsible for managing
    animals, enclosures, and staff.

    Attributes:
        _name (str): The name of the zoo.
        __animals (list): List of all animals in the zoo.
        __enclosures (list): List of all enclosures in the zoo.
        __staff (list): List of all staff members in the zoo.
    """

# ============================ Constructor ========================================================
    def __init__(self, name: str) -> None:
        """
        Initialize a new Zoo instance.

        Args:
            name (str): The name of the zoo.
        """
        # Use property to ensure validation via setter
        self.name = name

        # Initialize empty lists for zoo entities
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

# ============================ Getters ============================================================
    # Return the current value of each zoo attribute
    def get_name(self) -> str:
        """Return the zoo's name."""
        return self._name

    def get_animals(self) -> list:
        """Return a copy of the animals list."""
        return list(self.__animals)

    def get_enclosures(self) -> list:
        """Return a copy of the enclosures list."""
        return list(self.__enclosures)

    def get_staff(self) -> list:
        """Return a copy of the staff list."""
        return list(self.__staff)

# ============================ Setters ============================================================
    # Validate and set new values for zoo attributes
    def set_name(self, name: str) -> None:
        """
        Set a new name for the zoo.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is empty.
        """
        # Validate type
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        # Validate not empty
        if name.strip() == '':
            raise ValueError('Name cannot be empty.')
        self._name = name

# ============================ Properties =========================================================
    # Define properties for attribute access
    name = property(get_name, set_name)
    animals = property(get_animals)  # Read-only
    enclosures = property(get_enclosures)  # Read-only
    staff = property(get_staff)  # Read-only

# ============================ Animal Management ==================================================
    # Methods for managing animals in the zoo
    def add_animal(self, animal) -> str:
        """
        Adds an animal to the zoo.

        Args:
            animal (Animal): The animal to add to the zoo.

        Raises:
            TypeError: If animal is not an Animal instance.
            ValueError: If animal is already in the zoo.

        Returns:
            str: Confirmation message after adding the animal.
        """
        # Validate that animal is an Animal instance
        if not isinstance(animal, Animal):
            raise TypeError('Only Animal objects can be added to the zoo.')

        # Check for duplicate animals
        if animal in self.__animals:
            raise ValueError(f'{animal.name} the {animal.species} is already in the zoo.')

        # Add animal to zoo
        self.__animals.append(animal)
        return f'{animal.name} the {animal.species} has been added to the zoo.'


    def remove_animal(self, animal: Animal) -> str:
        """
        Removes an animal from the zoo.

        Args:
            animal (Animal): The animal to remove from the zoo.

        Raises:
            TypeError: If animal is not an Animal instance.
            ValueError: If animal is not in the zoo.

        Returns:
            str: Confirmation message after removing the animal.
        """
        # Validate that animal is an Animal instance
        if not isinstance(animal, Animal):
            raise TypeError('Only Animal objects can be removed from the zoo.')

        # Check if animal exists in zoo
        if animal not in self.__animals:
            raise ValueError(f'{animal.name} the {animal.species} is not in the zoo.')

        # Remove animal from zoo
        self.__animals.remove(animal)
        return f'{animal.name} the {animal.species} has been removed from the zoo.'

    def find_animal_by_name(self, name: str) -> Animal:
        """
        Find an animal in the zoo by name.

        Args:
            name (str): The name of the animal to find.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is empty or animal not found.

        Returns:
            Animal: The animal with the matching name.
        """
        # Validate name type
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')

        # Validate name not empty
        if name.strip() == '':
            raise ValueError('Name cannot be empty.')

        # Search for animal by name
        for animal in self.__animals:
            if animal.name.lower() == name.lower():
                return animal

        # Animal not found
        raise ValueError(f'No animal named "{name}" found in the zoo.')

# ============================ Enclosure Management ===============================================
    # Methods for managing enclosures in the zoo
    def add_enclosure(self, enclosure: Enclosure) -> str:
        """Add an enclosure to the zoo."""
        pass

    def remove_enclosure(self, enclosure: Enclosure) -> str:
        """Remove an enclosure from the zoo."""
        pass

# ============================ Staff Management ===================================================
    # Methods for managing staff members in the zoo
    def add_staff(self, staff_member: Staff) -> str:
        """Add a staff member to the zoo."""
        pass

    def remove_staff(self, staff_member: Staff) -> str:
        """Remove a staff member from the zoo."""
        pass
# ============================ Animal-Enclosure Assignment ========================================
    # Methods for assigning animals to appropriate enclosures
    def assign_animal_to_enclosure(self, animal: Animal, enclosure: Enclosure) -> str:
        """Assigns an animal to an appropriate enclosure."""
        pass

# ============================ Reporting ==========================================================
    # Methods for generating reports about the zoo
    def generate_report(self) -> str:
        """Generates a report of the zoo."""
        pass

    def list_animals_with_critical_health(self) -> list:
        """Return a list of the animals critical health."""

    def list_animals_by_species(self, species: str) -> list:
        """Returns a list of animals of a specific species."""
        pass

# ============================ String Method ======================================================
    def __str__(self) -> str:
        """Return a string representation of the zoo."""
        pass
