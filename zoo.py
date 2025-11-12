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
        """
        Adds an enclosure to the zoo.

        Args:
            enclosure (Enclosure): The enclosure to add to the zoo.

        Raises:
            TypeError: If enclosure is not an Enclosure instance.
            ValueError: If enclosure is already in the zoo.

        Returns:
            str: Confirmation message after adding the enclosure.
        """
        # Validate that enclosure is an Enclosure instance
        if not isinstance(enclosure, Enclosure):
            raise TypeError('Only Enclosure objects can be added to the zoo.')

        # Check for duplicate enclosures
        if enclosure in self.__enclosures:
            raise ValueError(f'{enclosure.environmental_type} enclosure is already in the zoo.')

        # Add enclosure to zoo
        self.__enclosures.append(enclosure)
        return f'{enclosure.environmental_type} enclosure has been added to the zoo.'

    def remove_enclosure(self, enclosure: Enclosure) -> str:
        """
        Removes an enclosure from the zoo.

        Args:
            enclosure (Enclosure): The enclosure to remove from the zoo.

        Raises:
            TypeError: If enclosure is not an Enclosure instance.
            ValueError: If enclosure is not in the zoo or still contains animals.

        Returns:
            str: Confirmation message after removing the enclosure.
        """
        # Validate that enclosure is an Enclosure instance
        if not isinstance(enclosure, Enclosure):
            raise TypeError('Only Enclosure objects can be removed from the zoo.')

        # Check if enclosure exists in zoo
        if enclosure not in self.__enclosures:
            raise ValueError(f'{enclosure.environmental_type} enclosure is not in the zoo.')

        # Check if enclosure still has animals
        if len(enclosure.animals) > 0:
            raise ValueError(f'Cannot remove enclosure: it still contains {len(enclosure.animals)} animal(s).')

        # Remove enclosure from zoo
        self.__enclosures.remove(enclosure)
        return f'{enclosure.environmental_type} enclosure has been removed from the zoo.'

# ============================ Staff Management ===================================================
    # Methods for managing staff members in the zoo
    def add_staff(self, staff_member: Staff) -> str:
        """
        Adds a staff member to the zoo.

        Args:
            staff_member (Staff): The staff member to add to the zoo.

        Raises:
            TypeError: If staff_member is not a Staff instance.
            ValueError: If staff member is already in the zoo.

        Returns:
            str: Confirmation message after adding the staff member.
        """
        # Validate that staff_member is a Staff instance
        if not isinstance(staff_member, Staff):
            raise TypeError('Only Staff objects can be added to the zoo.')

        # Check for duplicate staff (by staff_id using __eq__)
        if staff_member in self.__staff:
            raise ValueError(f'{staff_member.name} (ID: {staff_member.staff_id}) is already in the zoo.')

        # Add staff member to zoo
        self.__staff.append(staff_member)
        return f'{staff_member.name} ({staff_member.role}) has been added to the zoo staff.'

    def remove_staff(self, staff_member: Staff) -> str:
        """
        Removes a staff member from the zoo.

        Args:
            staff_member (Staff): The staff member to remove from the zoo.

        Raises:
            TypeError: If staff_member is not a Staff instance.
            ValueError: If staff member is not in the zoo.

        Returns:
            str: Confirmation message after removing the staff member.
        """
        # Validate that staff_member is a Staff instance
        if not isinstance(staff_member, Staff):
            raise TypeError('Only Staff objects can be removed from the zoo.')

        # Check if staff member exists in zoo
        if staff_member not in self.__staff:
            raise ValueError(f'{staff_member.name} is not in the zoo staff.')

        # Remove staff member from zoo
        self.__staff.remove(staff_member)
        return f'{staff_member.name} ({staff_member.role}) has been removed from the zoo staff.'

# ============================ Animal Enclosure Assignment ========================================
    # Methods for assigning animals to appropriate enclosures
    def assign_animal_to_enclosure(self, animal: Animal, enclosure: Enclosure) -> str:
        """
        Assigns an animal to an appropriate enclosure.

        This method ensures that:
        - The animal is in the zoo
        - The enclosure is in the zoo
        - The animal matches the enclosure type
        - The animal's environment matches the enclosure

        Args:
            animal (Animal): The animal to assign.
            enclosure (Enclosure): The enclosure to assign the animal to.

        Raises:
            TypeError: If animal or enclosure are not the correct type.
            ValueError: If animal or enclosure are not in the zoo, or assignment fails.

        Returns:
            str: Confirmation message after assignment.
        """
        # Validate types
        if not isinstance(animal, Animal):
            raise TypeError('animal must be an Animal instance.')
        if not isinstance(enclosure, Enclosure):
            raise TypeError('enclosure must be an Enclosure instance.')

        # Check if animal is in zoo
        if animal not in self.__animals:
            raise ValueError(f'{animal.name} is not in the zoo. Add the animal first.')

        # Check if enclosure is in zoo
        if enclosure not in self.__enclosures:
            raise ValueError(f'{enclosure.environmental_type} enclosure is not in the zoo. Add the enclosure first.')

        # Check if animal can be moved (no critical health issues)
        if not animal.can_be_moved():
            raise ValueError(f'{animal.name} has critical health issues and cannot be moved.')

        # Attempt to add animal to enclosure (enclosure validates type and environment)
        result = enclosure.add_animal(animal)

        # Return confirmation
        return f'{animal.name} assigned to {enclosure.environmental_type} enclosure. {result}'

    # ============================ Reporting ==========================================================
    # Methods for generating reports about the zoo
    def generate_report(self) -> str:
        """
        Generates a comprehensive summary of the zoo including
        animals, enclosures, and staff.

        Returns:
            str: A detailed report of the zoo's current state.
        """
        # Build report header
        report = f'{"=" * 60}\n'
        report += f'{self.name} - Zoo Report\n'
        report += f'{"=" * 60}\n\n'

        # Animals section
        report += f'ANIMALS ({len(self.__animals)}):\n'
        report += '-' * 60 + '\n'
        if self.__animals:
            for animal in self.__animals:
                report += f'  - {animal.name} ({animal.species}), Age: {animal.age}, '
                report += f'Diet: {animal.dietary_needs}, Environment: {animal.environment}\n'
                # Check for critical health issues
                if animal.has_critical_health_issues():
                    report += f'    !!  CRITICAL HEALTH ISSUES - Cannot be moved\n'
        else:
            report += '  No animals in the zoo.\n'
        report += '\n'

        # Enclosures section
        report += f'ENCLOSURES ({len(self.__enclosures)}):\n'
        report += '-' * 60 + '\n'
        if self.__enclosures:
            for enclosure in self.__enclosures:
                report += f'  - {enclosure.environmental_type} ({enclosure.size}), '
                report += f'Type: {enclosure.animal_type.__name__}, '
                report += f'Cleanliness: {enclosure.cleanliness_level}%, '
                report += f'Animals: {len(enclosure.animals)}\n'
        else:
            report += '  No enclosures in the zoo.\n'
        report += '\n'

        # Staff section
        report += f'STAFF ({len(self.__staff)}):\n'
        report += '-' * 60 + '\n'
        if self.__staff:
            for staff_member in self.__staff:
                report += f'  - {staff_member.name} (ID: {staff_member.staff_id}), '
                report += f'Role: {staff_member.role}, '
                report += f'Animals: {len(staff_member.assigned_animals)}, '
                report += f'Enclosures: {len(staff_member.assigned_enclosures)}\n'
        else:
            report += '  No staff members in the zoo.\n'

        report += '\n' + '=' * 60 + '\n'
        return report

    def list_animals_with_critical_health(self) -> list:
        """
        Returns a list of animals with critical health issues.

        Returns:
            list: List of Animal objects with critical health issues.
        """
        # Filter animals with critical health issues
        critical_animals = [animal for animal in self.__animals if animal.has_critical_health_issues()]
        return critical_animals

    def list_animals_by_species(self, species: str) -> list:
        """
        Returns a list of animals of a specific species.

        Args:
            species (str): The species to filter by.

        Raises:
            TypeError: If species is not a string.
            ValueError: If species is empty.

        Returns:
            list: List of Animal objects of the specified species.
        """
        # Validate species type
        if not isinstance(species, str):
            raise TypeError('Species must be a string.')

        # Validate species not empty
        if species.strip() == '':
            raise ValueError('Species cannot be empty.')

        # Filter animals by species (case-insensitive)
        animals_by_species = [animal for animal in self.__animals
                              if animal.species.lower() == species.lower()]
        return animals_by_species

    # ============================ String Method ======================================================
    def __str__(self) -> str:
        """
        Return a string representation of the zoo.

        Returns:
            str: The result of generate_report().
        """
        # Return comprehensive zoo report
        return self.generate_report()
