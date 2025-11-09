"""
File: enclosure.py
Description: This module defines the Enclosure class that manages animals' living spaces in the zoo.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal


class Enclosure:
    """
    Represents an animal enclosure in the zoo.

    Each enclosure houses only one type of animal, such as Mammal, Bird, or Reptile.

    Attributes:
        __size (str): The size of the enclosure (e.g., "Large", "Medium").
        __environmental_type (str): The type of environment suitable for the animals (e.g., 'Savannah', 'Aquatic').
        __animal_type (Animal subclass): The class of animal allowed in this enclosure.
        __cleanliness_level (float): The cleanliness level of the enclosure (0 to 100).
        __animals (list): List storing the animals currently in the enclosure.
    """

    def __init__(self, size: str, environmental_type: str, animal_type: type[Animal], cleanliness_level: float = 100) -> None:
        """
        Initialize a new Enclosure instance.

        Args:
            size (str): The size of the enclosure.
            environmental_type (str): The type of environment for the enclosure.
            animal_type (type[Animal]): The Animal subclass (e.g., Mammal, Bird) allowed in this enclosure.
            cleanliness_level (float): Initial cleanliness level (default is 100).
        """
        # Use properties to ensure validation via setters
        self.size = size
        self.environmental_type = environmental_type
        self.animal_type = animal_type
        self.cleanliness_level = cleanliness_level

        # Private list of actual Animal instances inside this enclosure
        self.__animals = []


# ============================ Getters ===============================================================
    # Return the current value of each enclosure attribute
    def get_size(self) -> str:
        """Return the size of the enclosure."""
        return self.__size

    def get_environmental_type(self) -> str:
        """Return the environmental type of the enclosure."""
        return self.__environmental_type

    def get_animal_type(self) -> type[Animal]:
        """Return the allowed animal type for the enclosure."""
        return self.__animal_type

    def get_cleanliness_level(self) -> float:
        """Return the cleanliness level of the enclosure."""
        return self.__cleanliness_level

    def get_animals(self) -> list:
        """
        Return a copy of the animals list to prevent external modification.
        """
        return list(self.__animals)

# ========================== Setters ================================================================
    # Validate and set new values for enclosure attributes
    def set_size(self, new_size: str) -> None:
        """
        Set a new size for the enclosure.

        Raises:
            TypeError: If new_size is not a string.
            ValueError: If new_size is empty.
        """
        # Validation for size type and value
        if not isinstance(new_size, str):
            raise TypeError('Size must be a string.')
        if new_size.strip() == '':
            raise ValueError('Size cannot be empty.')
        self.__size = new_size

    def set_environmental_type(self, new_type: str) -> None:
        """
        Set a new environmental type for the enclosure.

        Raises:
            TypeError: If new_type is not a string.
            ValueError: If new_type is empty.
        """
        # Validation for environment type and value
        if not isinstance(new_type, str):
            raise TypeError('Environmental type must be a string.')
        if new_type.strip() == '':
            raise ValueError('Environmental type cannot be empty.')
        self.__environmental_type = new_type

    def set_animal_type(self, new_type: type[Animal]) -> None:
        """
        Validate and set the allowed animal type for this enclosure.

        Raises:
            TypeError: If new_type is not a type or instance of Animal.
        """
        # Validate that new_type is a class (type object)
        # and that it's a subclass of Animal (Mammal, Bird, or Reptile)
        if not isinstance(new_type, type) or not issubclass(new_type, Animal):
            raise TypeError('animal_type must be a subclass of Animal.')
        # Set the validated animal type
        self.__animal_type = new_type

    def set_cleanliness_level(self, new_level: float) -> None:
        """
        Set a new cleanliness level for the enclosure.

        Raises:
            TypeError: If new_level is not a number.
            ValueError: If new_level is not between 0 and 100.
        """
        # Ensure value is numeric and within range
        if not isinstance(new_level, (int, float)):
            raise TypeError('Cleanliness level must be a number.')
        if not (0 <= new_level <= 100):
            raise ValueError('Cleanliness level must be between 0 and 100.')
        self.__cleanliness_level = new_level

# ============================ Properties ================================================================
    # Define properties to make access cleaner while maintaining encapsulation
    size = property(get_size, set_size)
    environmental_type = property(get_environmental_type, set_environmental_type)
    animal_type = property(get_animal_type, set_animal_type)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animals = property(get_animals)  # Read-only, modify via add/remove methods

# ============================ Methods ====================================================================
    # Methods for managing animals and enclosure maintenance
    def add_animal(self, animal) -> str:
        """
        Add an animal to the enclosure if it matches the allowed type and environment.

        Args:
            animal (Animal): Animal instance to add.

        Raises:
            TypeError: If the object is not an Animal or does not match enclosure type.
            ValueError: If the animal is already in the enclosure or has a mismatched environment.

        Returns:
            str: Confirmation message after adding the animal.
        """
        # Check that input is an Animal instance
        if not isinstance(animal, Animal):
            raise TypeError('Only Animal objects can be added to an enclosure.')

        # Check if animal belongs to the correct subclass (Mammal/Bird/Reptile)
        if not isinstance(animal, self.animal_type):
            raise TypeError(f'This enclosure only accepts {self.animal_type.__name__}s.')

        # Avoid duplicates
        if animal in self.__animals:
            raise ValueError(f'{animal.name} is already in this enclosure.')

        # Ensure the environment matches
        if animal.environment != self.environmental_type:
            raise ValueError(f'{animal.name} cannot be placed in a {self.environmental_type} enclosure.')

        # Passed all checks, add to list
        self.__animals.append(animal)
        return f'{animal.name} the {animal.species} has been added to the enclosure.'

    def remove_animal(self, animal) -> str:
        """
        Remove an animal from the enclosure.

        Args:
            animal (Animal): Animal instance to remove.

        Raises:
            TypeError: If the object is not an Animal.
            ValueError: If the animal is not currently in the enclosure.

        Returns:
            str: Confirmation message after removing the animal.
        """
        # Ensure argument is a valid Animal instance
        if not isinstance(animal, Animal):
            raise TypeError('Only Animal objects can be removed from an enclosure.')

        # Check if the animal actually exists inside
        if animal not in self.__animals:
            raise ValueError(f'{animal.name} is not in this enclosure.')

        # Remove and confirm
        self.__animals.remove(animal)
        return f'{animal.name} the {animal.species} has been removed from the enclosure.'


    def clean_enclosure(self) -> str:
        """
        Cleans the enclosure by resetting cleanliness level to 100.

        Returns:
            str: Confirmation message after cleaning.
        """
        # Record previous cleanliness before cleaning
        previous_level = self.cleanliness_level

        # Check if the enclosure is already clean
        if previous_level == 100:
            return f'The enclosure is already 100% clean.'

        # Reset cleanliness to maximum
        self.cleanliness_level = 100
        return f'Enclosure cleaned. Cleanliness restored from {previous_level}% to 100%.'

    def degrade_cleanliness(self, amount: float = 10) -> str:
        """
        Reduce cleanliness level by a specified amount (simulating daily use).

        Args:
            amount (float): Amount to reduce (default 10%)

        Returns:
            str: Message showing degradation
        """
        # Validate input type
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number.')

        # Validate input range
        if amount < 0 or amount > 100:
            raise ValueError('Amount must be between 0 and 100.')

        previous_level = self.cleanliness_level

        # Check if already at minimum
        if previous_level == 0:
            return 'The enclosure is already at 0% cleanliness (cannot degrade further).'

        # Calculate new cleanliness level
        new_level = self.cleanliness_level - amount

        # If new_level is less than 0, set it to 0
        if new_level < 0:
            self.cleanliness_level = 0
        else:
            # Otherwise, use the calculated value
            self.cleanliness_level = new_level

        return f'Cleanliness degraded from {previous_level}% to {self.cleanliness_level}%.'

    def report_status(self) -> str:
        """
        Generate a detailed status report for the enclosure.

        Returns:
            str: A report containing enclosure type, environment, size, cleanliness,
                 number of animals, and list of animals.
        """
        # Prepare list of animals or show 'no animals' message
        if self.animals:
            animal_list = ', '.join([animal.name for animal in self.animals])
        else:
            animal_list = 'No animals currently in this enclosure.'

        # Combine details into readable format
        return (f'Enclosure type: {self.animal_type.__name__}\n'
                f'Environment: {self.environmental_type}\n'
                f'Size: {self.size}\n'
                f'Cleanliness level: {self.cleanliness_level}\n'
                f'Number of animals: {len(self.animals)}\n'
                f'List of animals: {animal_list}\n')

    def __str__(self) -> str:
        """
        Return a string representation of the enclosure status.

        Returns:
            str: The result of report_status().
        """
        # When print() is called on the object, display full status
        return self.report_status()

