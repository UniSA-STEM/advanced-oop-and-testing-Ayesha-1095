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

class Animal(ABC):
    """
    Abstract base class representing a general animal in the zoo.
    It stores basic details such as name, species, age, and dietary needs,
    and defines common behaviours that all animals share.

     Attributes:
        name (str): The animal's name.
        species (str): The species or type of the animal.
        age (int): The age of the animal.
        dietary_needs (str): Description of the animal's diet.
    """
# ============================ Constructor =======================================================

    def __init__(self, name: str, species: str, age: int, dietary_needs: str) -> None:
        """
        Initialize a new Animal instance.

        Args:
            name (str): The animal's name.
            species (str): The type or category of the animal.
            age (int): The age of the animal in years.
            dietary_needs (str): The animal's dietary type (e.g., Carnivore, Herbivore).
        """
        self._name: str = name
        self._species: str = species
        self._age: int = age
        self._dietary_needs: str = dietary_needs
        self.__health_records: list = []    # Stores animal’s health records privately

# ============================ Getters ==========================================================
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

# ============================= Setters =========================================================
    def set_name(self, new_name: str) -> None:
        """
        Set a new name for the animal.

        Raises:
            TypeError: If the name is not a string.
             ValueError: If the name is empty.
        """
        if not isinstance (new_name, str):
            raise TypeError('Name must be a string.')
        self._name = new_name
        if new_name.strip() == "":
            raise ValueError('Name cannot be empty.')
        self._name = new_name

    def set_species(self, new_species: str) -> None:
        """
        Set a new species for the animal.

        Raises:
            TypeError: If the species is not a string.
            ValueError: If the species is empty.
        """
        if not isinstance (new_species, str):
            raise TypeError('Species must be a string.')
        self._species = new_species
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
        if isinstance(new_age, bool) or not isinstance (new_age, int):
            raise TypeError('Age must be an integer (not bool or None).')
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
        if not isinstance (new_diet, str):
            raise TypeError('Dietary needs must be a string.')
        self._dietary_needs = new_diet
        if new_diet.strip() == '':
            raise ValueError('Dietary needs cannot be empty.')
        self._dietary_needs = new_diet

# ============================ Properties ======================================================

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    dietary_needs = property(get_dietary_needs, set_dietary_needs)

# ============================ Abstract Methods ==========================================================
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
    def add_health_record(self, record: str) -> str:
        """
        Add a health record entry for this animal.

        Args:
            record (str): Description of the health update or medical record.

        Returns:
            str: A confirmation message after adding the record.
        """
        self.__health_records.append(record)
        msg = f'Health record added to {self.name}.'
        print(msg)
        return msg

    def display_health_records(self) -> list:
        """
        Display all stored health records for this animal.

        Returns:
            list | str: List of health records, or message if none exist.
        """
        if not self.__health_records:
            msg = f'{self.name} has no health records.'
            print(msg)
            return msg
        else:
            for record in self.__health_records:
                print(record)
            return list(self.__health_records)

# =============================== String Method =================================================
    def __str__(self) -> str:
        """
        Return a formatted string showing the animal’s basic information.

        The output includes animal's name, species, age, dietary_needs.

        Returns:
            str: A formatted string containing the animal details.
        """
        return (f'Name: {self.name}\n'
                f'Species: {self.species}\n'
                f'Age: {self.age}\n'
                f'Dietary needs: {self.dietary_needs}\n')

# ================================ Equal Method ===================================================

    def __eq__(self, other) -> bool:
        """
               Compare two Animal objects based on their attributes.

        Args:
            other (Animal): Another animal to compare.

        Returns:
            bool: True if both animals share the same attributes, False otherwise.
        """
        if not isinstance(other, Animal):
            return False
        return (self.name == other.name and
                self.species == other.species and
                self.age == other.age and
                self.dietary_needs == other.dietary_needs)

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

    def __init__(self, name: str, species: str, age: int, dietary_needs: str,
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
        super().__init__(name, species, age, dietary_needs)
        self._sound: str = sound
        self._hair_type: str = hair_type
        self._blood_type: str = blood_type

# ================================ Getters ============================================================
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
    def set_sound(self, sound: str) -> None:
        """
        Set the sound made by the mammal.

        Raises:
            TypeError: If the sound is not a string.
            ValueError: If the sound is empty.
        """
        if not isinstance (sound, str):
            raise TypeError('Sound must be a string.')
        self._sound = sound
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
        if not isinstance (hair_type, str):
            raise TypeError('Hair type must be a string.')
        self._hair_type = hair_type
        if hair_type.strip() == '':
            raise ValueError('Hair type cannot be empty.')
        self._hair_type = hair_type

# =================================== Properties ======================================================
    sound = property(get_sound, set_sound)
    hair_type = property(get_hair_type, set_hair_type)
    blood_type = property(get_blood_type)

# =================================== Methods =========================================================
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
        if not isinstance(other, Mammal):
            return False
        return (super().__eq__(other) and
                self.sound == other.sound and
                self.hair_type == other.hair_type and
                self.blood_type == other.blood_type)

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


