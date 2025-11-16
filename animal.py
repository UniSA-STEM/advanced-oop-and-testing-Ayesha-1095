"""
File: animal.py
Description: This module defines the main Animal class and its subclasses (Mammal, Reptile, and Bird)
for the zoo management system. Each class represents different types of animals and
their common behaviours.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from health_record import HealthRecord

class Animal(ABC):
    """
    Abstract base class representing a general animal in the zoo.
    It stores basic details such as name, species, age, and dietary needs,
    and defines common behaviours that all animals share.

     Attributes:
        _name (str): The animal's name.
        _species (str): The species or type of the animal.
        _age (int): The age of the animal.
        _dietary_needs (str): Description of the animal's diet.
        _environment (str): The type of environment suitable for the animals  (e.g., aquatic, savannah).
        __health_records (list): List storing the animal's health records privately.
    """
# ============================ Constructor =======================================================

    def __init__(self, name: str, species: str, age: int, dietary_needs: str, environment: str) -> None:
        """
        Initialize a new Animal instance.

        Args:
            name (str): The animal's name.
            species (str): The type or category of the animal.
            age (int): The age of the animal.
            dietary_needs (str): The animal's dietary type (e.g., Carnivore, Herbivore).
            environment (str): The type of environment suitable for the animal (e.g., Savannah, Aquatic).
        """
        # Use properties to ensure validation via setters
        self.name = name
        self.species = species
        self.age = age
        self.dietary_needs = dietary_needs
        self.environment = environment

        # Initialize empty list to store health records
        self.__health_records = []

# ============================ Getters ==========================================================
    # Return the current value of each attribute
    def get_name(self) -> str:
        """Return the animal's name."""
        return self._name

    def get_species(self) -> str:
        """Return the animal's species."""
        return self._species

    def get_age(self) -> int:
        """Return the animal's age."""
        return self._age

    def get_dietary_needs(self) -> str:
        """Return the animal's dietary needs."""
        return self._dietary_needs

    def get_environment(self) -> str:
        """Return the animal's environment."""
        return self._environment

# ============================= Setters =========================================================
    # Validate and set new values for attributes
    def set_name(self, new_name: str) -> None:
        """
        Set a new name for the animal.

        Raises:
            TypeError: If the name is not a string.
            ValueError: If the name is empty.
        """
        # Validate type
        if not isinstance (new_name, str):
            raise TypeError('Name must be a string.')
        # Validate not empty
        if new_name.strip() == '':
            raise ValueError('Name cannot be empty.')
        self._name = new_name

    def set_species(self, new_species: str) -> None:
        """
        Set a new species for the animal.

        Raises:
            TypeError: If the species is not a string.
            ValueError: If the species is empty.
        """
        # Validate type
        if not isinstance (new_species, str):
            raise TypeError('Species must be a string.')
        # Validate not empty
        if new_species.strip() == '':
            raise ValueError('Species cannot be empty.')
        self._species = new_species

    def set_age(self, new_age: int) -> None:
        """
        Set a new age for the animal.

        Raises:
            TypeError: If age is not an integer (or is a boolean / None).
            ValueError: If age is negative.
        """
        # Check for bool first because in Python, bool is a subclass of int
        # isinstance(True, int) returns True, so we must exclude bools explicitly
        if isinstance(new_age, bool) or not isinstance (new_age, int):
            raise TypeError('Age must be an integer (not bool or None).')

        # Ensure age is not negative
        if new_age < 0:
            raise ValueError('Age cannot be negative.')
        self._age = new_age

    def set_dietary_needs(self, new_diet: str) -> None:
        """
        Set the dietary needs for the animal.

        Raises:
            TypeError: If the dietary needs are not a string.
            ValueError: If the dietary needs are empty.
        """
        # Validate type
        if not isinstance (new_diet, str):
            raise TypeError('Dietary needs must be a string.')
        # Validate not empty
        if new_diet.strip() == '':
            raise ValueError('Dietary needs cannot be empty.')
        self._dietary_needs = new_diet

    def set_environment(self, new_env: str) -> None:
        """
        Set a new environment for the animal.

        Raises:
            TypeError: If the environment is not a string.
            ValueError: If the environment is empty.
        """
        # Validate type
        if not isinstance(new_env, str):
            raise TypeError('Environment must be a string.')
        # Validate not empty
        if new_env.strip() == '':
            raise ValueError('Environment cannot be empty.')
        self._environment = new_env

# ============================ Properties ======================================================
    # Create Python properties for attribute access
    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    dietary_needs = property(get_dietary_needs, set_dietary_needs)
    environment = property(get_environment, set_environment)

# ============================ Abstract Methods ==========================================================
    # These methods must be implemented by all subclasses (Mammal, Reptile, Bird)
    @abstractmethod
    def eat(self) -> str:
        """Each animal subclass must define its eating behavior."""
        pass

    @abstractmethod
    def sleep(self) -> str:
        """Each animal subclass must define its sleeping behavior."""
        pass

    @abstractmethod
    def make_sound(self) -> str:
        """Each animal subclass must define its sound behavior."""
        pass

# ============================== Health Records ============================================================
    def add_health_record(self, record) -> str:
        """
        Add a HealthRecord instance to this animal's health records.

        This method ensures that only unique health records are added
        by comparing the record's description, date reported, and severity level.

        Args:
            record (HealthRecord): A HealthRecord object representing a medical record.

        Raises:
            TypeError: If 'record' is not an instance of HealthRecord.

        Returns:
            str: Confirmation message after adding the record, or a notice
                 if the record already exists.
        """
        # Ensure the provided object is a HealthRecord instance
        if not isinstance(record, HealthRecord):
            raise TypeError('Record must be a HealthRecord instance.')

        # Prevent duplicate records using __eq__
        if record in self.__health_records:
            return f'Record already exists for {self.name}.'

        # Add the record to the internal list
        self.__health_records.append(record)
        return f'Health record added to {self.name}.'

    def display_health_records(self) -> list:
        """
        Display all health records for this animal.

        Returns:
            list: A list of HealthRecord objects. Empty list if none exist.
        """
        # Returns empty list [] if no records
        return list(self.__health_records)

    def has_critical_health_issues(self) -> bool:
        """
        Check if the animal has any critical health issues.

        Returns:
            bool: True if any health record is critical, False otherwise.
        """
        # Loop through all health records
        for record in self.__health_records:
            # Check if any record is marked as critical using HealthRecord's is_critical() method
            if record.is_critical():
                return True  # Found at least one critical issue
        return False   # No critical issues found

    def can_be_moved(self) -> bool:
        """
        Determine if the animal can be safely moved to another enclosure.
        Animals with critical health issues should not be moved.

        Returns:
            bool: True if animal can be moved, False if under critical treatment.
        """
        # Animal can be moved only if it has no critical health issues
        return not self.has_critical_health_issues()


# =============================== String Method =================================================
    def __str__(self) -> str:
        """
        Return a formatted string showing the animal’s basic information.

        The output includes animal's name, species, age, dietary_needs.

        Returns:
            str: A formatted string containing the animal details.
        """
        # Format and return all animal attributes as a readable string
        return (f'Name: {self.name}\n'
                f'Species: {self.species}\n'
                f'Age: {self.age}\n'
                f'Dietary needs: {self.dietary_needs}\n'
                f'Environment: {self.environment}\n')

# ================================ Equal Method ===================================================

    def __eq__(self, other) -> bool:
        """
               Compare two Animal objects based on their attributes.

        Args:
            other (Animal): Another animal to compare.

        Returns:
            bool: True if both animals share the same attributes, False otherwise.
        """
        # Check if comparing with another Animal instance
        if not isinstance(other, Animal):
            return False
        # Compare all attributes
        return (self.name == other.name and
                self.species == other.species and
                self.age == other.age and
                self.dietary_needs == other.dietary_needs and
                self.environment == other.environment)

class Mammal(Animal):
    """
    Represents mammals in the zoo. Mammals have hair, warm blood, and usually
    give birth to live young. This class extends Animal with extra attributes
    like sound, hair type, and blood type.

    Attributes:
        sound (str): Sound made by the mammal.
        hair_type (str): Description of hair or fur type.
        blood_type (str): Type of blood temperature regulation (e.g., warm-blooded).
    """

    def __init__(self, name: str, species: str, age: int, dietary_needs: str, environment: str,
                 sound: str, hair_type: str, blood_type: str) -> None:
        """
        Initialize a Mammal object.

        Args:
            name (str): Mammal’s name.
            species (str): Type or species of the mammal.
            age (int): Age of the mammal.
            dietary_needs (str): Mammal’s diet type.
            sound (str): Sound made by the mammal.
            hair_type (str): Description of hair or fur type.
            blood_type (str): Type of blood temperature regulation (e.g., warm-blooded).
        """
        # Initialize parent Animal class with common attributes
        super().__init__(name, species, age, dietary_needs, environment)

        # Initialize Mammal specific attributes using properties
        self.sound: str = sound
        self.hair_type: str = hair_type

        # Blood type is read-only (no setter)
        self._blood_type: str = blood_type

# ================================ Getters ============================================================
    # Return the current value of each Mammal specific attribute
    def get_sound(self) -> str:
        """Return the sound made by the mammal."""
        return self._sound

    def get_hair_type(self) -> str:
        """Return the type of hair or fur the mammal has."""
        return self._hair_type

    def get_blood_type(self) -> str:
        """Return the mammal’s blood type (e.g., warm-blooded)."""
        return self._blood_type

# ================================== Setters ===========================================================
    # Validate and set new values for Mammal specific attributes
    def set_sound(self, sound: str) -> None:
        """
        Set the sound made by the mammal.

        Raises:
            TypeError: If the sound is not a string.
            ValueError: If the sound is empty.
        """
        # Validate type
        if not isinstance (sound, str):
            raise TypeError('Sound must be a string.')
        # Validate not empty
        if sound.strip() == '':
            raise ValueError('Sound cannot be empty.')
        self._sound = sound

    def set_hair_type(self, hair_type: str) -> None:
        """
        Set the hair type for the mammal.

        Raises:
            TypeError: If the hair type is not a string.
            ValueError: If the hair type is empty.
        """
        # Validate type
        if not isinstance (hair_type, str):
            raise TypeError('Hair type must be a string.')
        # Validate not empty
        if hair_type.strip() == '':
            raise ValueError('Hair type cannot be empty.')
        self._hair_type = hair_type

    # Note: blood_type does not have a setter, implying it is fixed after instantiation.
# =================================== Properties ======================================================
    # Define properties for Mammal specific attributes
    sound = property(get_sound, set_sound)
    hair_type = property(get_hair_type, set_hair_type)
    blood_type = property(get_blood_type)

# =================================== Methods =========================================================
    # Implementation of abstract methods from Animal base class
    def eat(self) -> str:
        """Return a message describing how the mammal eats."""
        return f'{self.name} the {self.species} is eating {self.dietary_needs}.'

    def sleep(self) -> str:
        """Return a message describing that the  mammal is sleeping."""
        return f'{self.name} the {self.species} is sleeping.'

    def make_sound(self) -> str:
        """Return a message describing the sound the mammal makes."""
        return f'{self.name} {self.sound}!'

# =================================== String Method ===============================================
    def __str__(self) -> str:
        """
        Return a formatted string with all mammal details.

        The output includes general animal information from the base class
        as well as mammal-specific attributes such as hair type, and blood type.

        Returns:
            str: A formatted string containing the mammal's complete details.
        """
        # Call parent __str__ and append Mammal specific attributes
        return (super().__str__() +
                f'Sound: {self.sound}\n'
                f'Hair type: {self.hair_type}\n'
                f'Blood type: {self.blood_type}\n')

# =================================== Equal Method =================================================
    def __eq__(self, other) -> bool:
        """
        Compare two mammals based on both their Animal and Mammal attributes.

        Args:
            other (Mammal): Another mammal to compare.

        Returns:
            bool: True if both mammals share the same attributes.
        """
        # Check type first
        if not isinstance(other, Mammal):
            return False
        # Compare parent attributes AND Mammal specific attributes
        return (super().__eq__(other) and
                self.sound == other.sound and
                self.hair_type == other.hair_type and
                self.blood_type == other.blood_type)

class Reptile(Animal):
    """
    Represents reptiles in the zoo. Reptiles are cold-blooded and usually
    have scales. This class extends Animal with extra attributes like
    sound, skin type, blood type, and whether the reptile is venomous.

    Attributes:
        sound (str): Sound made by the reptile.
        skin_type (str): Description of the reptile's skin.
        blood_type (str): Blood temperature type (e.g., cold-blooded).
        is_venomous (bool): Indicates if the reptile is venomous.
    """

    def __init__(self, name: str, species: str, age: int, dietary_needs: str, environment: str,
                 sound: str, skin_type: str, blood_type: str, is_venomous: bool) -> None:
        """
        Initialize a Reptile object.

        Args:
            name (str): The reptile's name.
            species (str): Type or species of the reptile.
            age (int): Age of the reptile.
            dietary_needs (str): Diet type of the reptile.
            sound (str): Sound made by the reptile.
            skin_type (str): Description of the reptile's skin.
            blood_type (str): Blood temperature type (e.g., cold-blooded).
            is_venomous (bool): Whether the reptile is venomous.
        """
        # Initialize parent Animal class with common attributes
        super().__init__(name, species, age, dietary_needs, environment)

        # Initialize Reptile specific attributes using properties
        self.sound: str = sound
        self.skin_type: str = skin_type
        self._blood_type: str = blood_type  # Blood type is read only (no setter)
        self.is_venomous: bool = is_venomous

    # =================================== Getters ===========================================================================
    # Return the current value of each Reptile specific attribute
    def get_sound(self) -> str:
        """Return the sound made by the reptile."""
        return self._sound

    def get_skin_type(self) -> str:
        """Return the skin type of the reptile."""
        return self._skin_type

    def get_blood_type(self) -> str:
        """Return the reptile blood type."""
        return self._blood_type

    def get_is_venomous(self) -> bool:
        """Return whether the reptile is venomous."""
        return self._is_venomous

    # ==================================== Setters =========================================================================
    # Validate and set new values for Reptile specific attributes
    def set_sound(self, sound: str) -> None:
        """
        Set the sound made by the reptile.

        Raises:
            TypeError: If the sound is not a string.
            ValueError: If the sound is an empty string.
        """
        # Validate type
        if not isinstance(sound, str):
            raise TypeError('Sound must be a string.')
        # Validate not empty
        if sound.strip() == '':
            raise ValueError('Sound cannot be empty.')
        self._sound = sound

    def set_skin_type(self, skin_type: str) -> None:
        """
        Set the skin type for the reptile.

        Raises:
            TypeError: If the skin type is not a string.
            ValueError: If the skin type is an empty string.
        """
        # Validate type
        if not isinstance(skin_type, str):
            raise TypeError('Skin type must be a string.')
        # Validate not empty
        if skin_type.strip() == '':
            raise ValueError('Skin type cannot be empty.')
        self._skin_type = skin_type

    def set_is_venomous(self, is_venomous: bool) -> None:
        """
        Set the is_venomous flag for the reptile.

        Raises:
            TypeError: If is_venomous is not a boolean.
        """
        # Validate type
        if not isinstance(is_venomous, bool):
            raise TypeError('Is Venomous must be a boolean (True/False).')
        self._is_venomous = is_venomous

    # =================================== Properties ==============================================
    # Define properties for Reptile specific attributes
    sound = property(get_sound, set_sound)
    skin_type = property(get_skin_type, set_skin_type)
    blood_type = property(get_blood_type)
    is_venomous = property(get_is_venomous, set_is_venomous)

    # =================================== Methods ==================================================
    # Implementation of abstract methods
    def eat(self) -> str:
        """Return a message describing how the reptile eats."""
        return f'{self.name} the {self.species} is eating {self.dietary_needs}.'

    def sleep(self) -> str:
        """Return a message describing that reptile is sleeping."""
        return f'{self.name} the {self.species} is sleeping.'

    def make_sound(self) -> str:
        """Return a message describing the sound the reptile makes.."""
        return f'{self.name} {self.sound}!'

    # ==================================== String Method ============================================
    def __str__(self) -> str:
        """
        Return a formatted string with all reptile details.

        The output includes general animal information from the base class
        as well as reptile-specific attributes such as skin type, blood type,
        and venom status.

        Returns:
            str: A formatted string containing the reptile's complete details.
        """
        # Call parent __str__ and append Reptile specific attributes
        return (super().__str__() +
                f'Sound: {self.sound}\n'
                f'Skin type: {self.skin_type}\n'
                f'Blood type: {self.blood_type}\n'
                f'Is Venomous: {self.is_venomous}\n')

    # ====================================== Equal Method =============================================
    def __eq__(self, other) -> bool:
        """
        Compare two reptiles based on both their Animal and Reptile attributes.

        Args:
            other (Reptile): Another reptile to compare.

        Returns:
            bool: True if both reptiles share the same attributes.
        """
        # Check type first
        if not isinstance(other, Reptile):
            return False
        # Compare parent attributes AND Reptile specific attributes
        return (super().__eq__(other) and
                self.sound == other.sound and
                self.skin_type == other.skin_type and
                self.blood_type == other.blood_type and
                self.is_venomous == other.is_venomous)


class Bird(Animal):
    """
    Represents birds in the zoo. Birds have feathers and most can fly.
    This class extends Animal with extra attributes like sound, feather type,
    blood type, and the ability to fly.

    Attributes:
        sound (str): Sound made by the bird.
        feather_type (str): Description of the bird's feathers.
        blood_type (str): Blood temperature type (e.g., warm-blooded).
        can_fly (bool): Indicates if the bird can fly.
    """

    def __init__(self, name: str, species: str, age: int, dietary_needs: str, environment: str,
                 sound: str, feather_type: str, blood_type: str, can_fly: bool) -> None:
        """
        Initialize a Bird object.

        Args:
            name (str): The bird's name.
            species (str): Type or species of the bird.
            age (int): Age of the bird.
            dietary_needs (str): Diet type of the bird.
            sound (str): Sound made by the bird.
            feather_type (str): Description of the bird's feathers.
            blood_type (str): Blood temperature type (e.g., warm-blooded).
            can_fly (bool): Indicates if the bird can fly.
        """
        # Initialize parent Animal class with common attributes
        super().__init__(name, species, age, dietary_needs, environment)

        # Initialize Bird specific attributes using properties
        self.sound: str = sound
        self.feather_type: str = feather_type
        self._blood_type: str = blood_type    # Blood type is read-only (no setter)
        self.can_fly: bool = can_fly

    # ===================================== Getters =========================================================
    # Return the current value of each Bird specific attribute
    def get_sound(self) -> str:
        """Return the sound made by the bird."""
        return self._sound

    def get_feather_type(self) -> str:
        """Return the feather type of the bird."""
        return self._feather_type

    def get_blood_type(self) -> str:
        """Return the bird blood type."""
        return self._blood_type

    def get_can_fly(self) -> bool:
        """Return the bird can_fly."""
        return self._can_fly

    # ===================================== Setters ============================================================
    # Validate and set new values for Bird specific attributes
    def set_sound(self, sound: str) -> None:
        """
        Set the sound made by the bird.

        Raises:
            TypeError: If the sound is not a string.
            ValueError: If the sound is an empty string.
        """
        # Validate type
        if not isinstance(sound, str):
            raise TypeError('Sound must be a string.')
        # Validate not empty
        if sound.strip() == '':
            raise ValueError('Sound cannot be empty.')
        self._sound = sound

    def set_feather_type(self, feather_type: str) -> None:
        """
        Set the feather type of the bird.

        Raises:
            TypeError: If the feather type is not a string.
            ValueError: If the feather type is an empty string.
        """
        # Validate type
        if not isinstance(feather_type, str):
            raise TypeError('Feather type must be a string.')
        # Validate not empty
        if feather_type.strip() == '':
            raise ValueError('Feather type cannot be empty.')
        self._feather_type = feather_type

    def set_can_fly(self, can_fly: bool) -> None:
        """
        Set the can_fly flag for the bird.

        Raises:
            TypeError: If can_fly is not a boolean.
        """
        # Validate type
        if not isinstance(can_fly, bool):
            raise TypeError('Can fly must be a boolean (True/False).')
        self._can_fly = can_fly

    # ================================== Properties =====================================================
    # Define properties for Bird specific attributes
    sound = property(get_sound, set_sound)
    feather_type = property(get_feather_type, set_feather_type)
    blood_type = property(get_blood_type)   # Read-only (no setter)
    can_fly = property(get_can_fly, set_can_fly)

    # ================================== Methods =========================================================
    # Implementation of abstract methods from Animal base class
    def eat(self) -> str:
        """Return a message describing how the bird eats."""
        return f'{self.name} the {self.species} is eating {self.dietary_needs}.'

    def sleep(self) -> str:
        """Return a message describing how the bird sleeps."""
        return f'{self.name} the {self.species} is sleeping.'

    def make_sound(self) -> str:
        """Return a message describing how the bird makes sounds."""
        return f'{self.name} {self.sound}!'

    def __str__(self) -> str:
        """
        Return a formatted string with all bird details.

        The output includes general animal information from the base class
        as well as bird-specific attributes such as feather type, blood type,
        and if the bird can fly.

        Returns:
            str: A formatted string containing the bird's complete details.
        """
        # Call parent __str__ and append Bird specific attributes
        return (super().__str__() +
                f'Sound: {self.sound}\n'
                f'Feather type: {self.feather_type}\n'
                f'Blood type: {self.blood_type}\n'
                f'Can Fly: {self.can_fly}\n')

    def __eq__(self, other) -> bool:
        """
        Compare two birds based on both their Animal and Bird attributes.

        Args:
            other (Bird): Another bird to compare.

        Returns:
            bool: True if both birds share the same attributes.
        """
        # Check type first
        if not isinstance(other, Bird):
            return False
        # Compare parent attributes and Bird specific attributes
        return (super().__eq__(other) and
                self.sound == other.sound and
                self.feather_type == other.feather_type and
                self.blood_type == other.blood_type and
                self.can_fly == other.can_fly)
