"""
File: test_animal.py
Description: This module tests the Animal hierarchy, including the Mammal, Reptile, and Bird subclasses.
It verifies class inheritance, property validation, methods, string representation, equality checks,
and proper exception handling for invalid inputs.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""


import pytest
from animal import Animal, Mammal, Reptile, Bird
from health_record import HealthRecord

# ===============================================
#        Animal and Mammal Tests
# ===============================================
# Test the Mammal subclass including inheritance, methods, properties, edge cases, health records,
# string representation, and equality checks.

# ==== Fixture for Mammal ====
# This fixture creates a default Mammal instance 'Simba' to be used in multiple tests.
@pytest.fixture
def lion():
    """Fixture to create a default Mammal instance for testing."""
    return Mammal('Simba','Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long and thick', 'Warm-blooded')

# ==== Inheritance and Abstract Class Tests ====
# These tests ensure:
#   - Mammal correctly inherits from the Animal base class.
#   - Animal cannot be instantiated directly since it is abstract
def test_mammal_inheritance(lion):
    """Verify that Mammal is an instance of Animal and Animal cannot be instantiated directly."""
    # Check that 'lion' is an instance of Animal
    assert isinstance(lion, Animal)
    # Attempting to instantiate abstract Animal class should raise TypeError
    with pytest.raises(TypeError):
        Animal('Simba', 'Lion', 5, 'Carnivore', 'Savannah')

# ==== Method Tests ====
# Tests the behavior of the primary actions of an animal: eat, sleep, make_sound
def test_mammal_methods(lion):
    """Test that eat, sleep, and make_sound return correct behavior strings."""
    assert lion.eat() == 'Simba the Lion is eating Carnivore.'
    assert lion.sleep() == 'Simba the Lion is sleeping.'
    assert lion.make_sound() == 'Simba Roar!'

# ==== Property Getter and Setter Tests ====
# Tests that properties can be retrieved (getters) and updated with valid values (setters)
def test_mammal_properties(lion):
    """Test getters and valid setters for Mammal properties."""
    # Testing getters
    assert lion.name == 'Simba'
    assert lion.species == 'Lion'
    assert lion.age == 5
    assert lion.dietary_needs == 'Carnivore'
    assert lion.environment == 'Savannah'
    assert lion.sound == 'Roar'
    assert lion.hair_type == 'Long and thick'
    assert lion.blood_type == 'Warm-blooded'


    # Testing valid setters
    lion.name = 'Leo'
    assert lion.name == 'Leo'
    lion.age = 6
    assert lion.age == 6
    lion.dietary_needs = 'Meat'
    assert lion.dietary_needs == 'Meat'
    lion.environment = 'Jungle'
    assert lion.environment == 'Jungle'
    lion.sound = 'Meow'
    assert lion.sound == 'Meow'
    lion.hair_type = 'Short'
    assert lion.hair_type == 'Short'

# ==== Edge Case and Invalid Input Tests ====
# Ensures that inappropriate types or invalid values raise exceptions
def test_mammal_edge_setters(lion):
    """Test that invalid types and empty/whitespace strings raise TypeError or ValueError."""
    # Type errors
    with pytest.raises(TypeError):
        lion.name = 123
    with pytest.raises(TypeError):
        lion.species = 123
    with pytest.raises(TypeError):
        lion.age = 'Six'
    with pytest.raises(TypeError):
        lion.age = True
    with pytest.raises(TypeError):
        lion.age = False
    with pytest.raises(TypeError):
        lion.dietary_needs = 110
    with pytest.raises(TypeError):
        lion.environment = 109
    with pytest.raises(TypeError):
        lion.sound = 2
    with pytest.raises(TypeError):
        lion.hair_type = 123

    # Value errors: negative age, empty or whitespace strings
    with pytest.raises(ValueError):
        lion.age = -2
    with pytest.raises(ValueError):
        lion.name = ''
    with pytest.raises(ValueError):
        lion.name = '    '
    with pytest.raises(ValueError):
        lion.species = ''
    with pytest.raises(ValueError):
        lion.species = '   '
    with pytest.raises(ValueError):
        lion.dietary_needs = ''
    with pytest.raises(ValueError):
        lion.dietary_needs = '   '
    with pytest.raises(ValueError):
        lion.environment = ''
    with pytest.raises(ValueError):
        lion.environment = '   '
    with pytest.raises(ValueError):
        lion.sound = ''
    with pytest.raises(ValueError):
        lion.sound = '   '
    with pytest.raises(ValueError):
        lion.hair_type = ''
    with pytest.raises(ValueError):
        lion.hair_type = '   '

# ==== Health Related Method Tests ====
# These tests cover the Animal class methods related to health records:
#   - add_health_record()
#   - display_health_records()
#   - has_critical_health_issues()
#   - can_be_moved()
# They check valid additions, type safety, duplicate handling, and critical health logic.

def test_add_health_record(lion):
    """Test adding a single HealthRecord to an animal."""
    rec = HealthRecord('Vaccinated', '2025-11-09', 'Low', 'Routine check')
    msg = lion.add_health_record(rec)
    # Confirm addition message
    assert 'Health record added to Simba.' in msg
    # Ensure record is present
    records = lion.display_health_records()
    assert isinstance(records, list)
    assert len(records) == 1
    assert records[0] == rec

def test_add_multiple_health_records(lion):
    """Test adding multiple HealthRecord objects to an animal."""
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Follow-up')
    rec2 = HealthRecord('Surgery', '2025-11-10', 'Critical', 'Immediate attention')
    lion.add_health_record(rec1)
    lion.add_health_record(rec2)
    records = lion.display_health_records()
    assert len(records) == 2
    assert rec1 in records
    assert rec2 in records

def test_add_invalid_health_record(lion):
    """Adding an invalid health record type should raise TypeError."""
    with pytest.raises(TypeError):
        lion.add_health_record(123)  # Not a HealthRecord instance

def test_duplicate_health_record(lion):
    """Adding the same HealthRecord twice should return a duplicate message."""
    rec = HealthRecord('Vaccinated', '2025-11-09', 'Low', 'Routine check')
    msg1 = lion.add_health_record(rec)
    msg2 = lion.add_health_record(rec)  # Duplicate
    assert 'Health record added to Simba.' in msg1
    assert 'Record already exists for Simba' in msg2

def test_has_critical_health_issues(lion):
    """Check has_critical_health_issues detects critical records correctly."""
    # No records → not critical
    assert lion.has_critical_health_issues() is False

    # Add non-critical record
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Low', 'Routine check')
    lion.add_health_record(rec1)
    assert lion.has_critical_health_issues() is False

    # Add critical record
    rec2 = HealthRecord('Surgery', '2025-11-10', 'Critical', 'Immediate attention')
    lion.add_health_record(rec2)
    assert lion.has_critical_health_issues() is True

def test_can_be_moved(lion):
    """Verify can_be_moved returns False if there are critical health issues."""
    # Initially no records, safe to move
    assert lion.can_be_moved() is True

    # Add non-critical record, still safe
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Routine check')
    lion.add_health_record(rec1)
    assert lion.can_be_moved() is True

    # Add critical record, cannot move
    rec2 = HealthRecord('Injury', '2025-11-10', 'Critical', 'Immediate attention')
    lion.add_health_record(rec2)
    assert lion.can_be_moved() is False

def test_display_health_records_empty(lion):
    """Display health records returns message if there are no records."""
    records = lion.display_health_records()
    assert isinstance(records, list)
    assert records == []

def test_display_health_records_nonempty(lion):
    """Display health records returns a list of HealthRecord objects when present."""
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Routine check')
    rec2 = HealthRecord('Vaccinated', '2025-11-09', 'Low', 'Routine check')
    lion.add_health_record(rec1)
    lion.add_health_record(rec2)
    records = lion.display_health_records()
    assert isinstance(records, list)
    assert all(isinstance(r, HealthRecord) for r in records)
    assert rec1 in records
    assert rec2 in records

# ==== String Method Test ====
# Test that __str__ returns a formatted string containing all attributes
def test_mammal_str(lion):
    """Test that __str__ returns a properly formatted string with all Mammal details."""
    st = str(lion)
    assert 'Name: Simba' in st
    assert 'Species: Lion' in st
    assert 'Age: 5' in st
    assert 'Dietary needs: Carnivore' in st
    assert 'Environment: Savannah' in st
    assert 'Sound: Roar' in st
    assert 'Hair type: Long and thick' in st
    assert 'Blood type: Warm-blooded' in st

# ==== Equality Tests ====
# Test that __eq__ correctly identifies identical and different Mammal instances
def test_mammal_equality():
    """Test __eq__ method for comparing two Mammals and differences in attributes."""
    lion1 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long and thick', 'Warm-blooded')
    lion2 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long and thick', 'Warm-blooded')
    lion3 = Mammal('Leo', 'Lion', 4, 'Carnivore', 'Jungle', 'Roar', 'Short', 'Warm-blooded')
    assert lion1 == lion2
    assert lion1 != lion3

def test_mammal_equality_with_different_type(lion):
    """Test that __eq__ returns False when comparing with non-Mammal object."""
    assert lion != 'not a mammal'

# ===============================================
#        Reptile Tests
# ===============================================
# Test the Reptile subclass, including methods, properties, edge cases, health records,
# string representation, and equality checks.

# ==== Fixture for Reptile ====
# Provides a default Reptile instance for tests
@pytest.fixture
def snake():
    """Fixture to create a default Reptile instance for testing."""
    return Reptile('Python', 'Snake', 4, 'Carnivore', 'Jungle','Hiss', 'Scaly', 'Cold-blooded', True)

# ==== Method Tests ====
# Tests primary animal actions for Reptile
def test_reptile_methods(snake):
    """Test eat, sleep, and make_sound for Reptile."""
    assert snake.eat() == 'Python the Snake is eating Carnivore.'
    assert snake.sleep() == 'Python the Snake is sleeping.'
    assert snake.make_sound() == 'Python Hiss!'

# ==== Property Getter and Setter Tests ====
# Checks that all properties can be retrieved and updated correctly
def test_reptile_properties(snake):
    """Test getters and valid setters for Reptile properties."""
    # Test getters
    assert snake.name == 'Python'
    assert snake.species == 'Snake'
    assert snake.age == 4
    assert snake.dietary_needs == 'Carnivore'
    assert snake.environment == 'Jungle'
    assert snake.sound == 'Hiss'
    assert snake.skin_type == 'Scaly'
    assert snake.blood_type == 'Cold-blooded'
    assert snake.is_venomous == True

    # Test setters
    snake.name = 'Kobra'
    assert snake.name == 'Kobra'
    snake.age = 5
    assert snake.age == 5
    snake.dietary_needs = 'Meat'
    assert snake.dietary_needs == 'Meat'
    snake.environment = 'Grasslands'
    assert snake.environment == 'Grasslands'
    snake.sound = 'Sss'
    assert snake.sound == 'Sss'
    snake.skin_type = 'Smooth'
    assert snake.skin_type == 'Smooth'
    snake.is_venomous = False
    assert snake.is_venomous == False


# ==== Edge Case and Invalid Input Tests ====
# Verifies that invalid types and empty/whitespace strings raise appropriate exceptions
def test_reptile_edge_setters(snake):
    """Test that invalid types and empty/whitespace strings raise TypeError or ValueError for Reptile."""

    # Type errors
    with pytest.raises(TypeError):
        snake.name = 123
    with pytest.raises(TypeError):
        snake.species = 123
    with pytest.raises(TypeError):
        snake.age = 'Four'
    with pytest.raises(TypeError):
        snake.age = True
    with pytest.raises(TypeError):
        snake.age = False
    with pytest.raises(TypeError):
        snake.dietary_needs = 99
    with pytest.raises(TypeError):
        snake.environment = 10
    with pytest.raises(TypeError):
        snake.sound = 1
    with pytest.raises(TypeError):
        snake.skin_type = 45
    with pytest.raises(TypeError):
        snake.is_venomous = 'Yes'  # must be bool

    # Value errors
    with pytest.raises(ValueError):
        snake.age = -1
    with pytest.raises(ValueError):
        snake.name = ''
    with pytest.raises(ValueError):
        snake.name = '   '
    with pytest.raises(ValueError):
        snake.species = ''
    with pytest.raises(ValueError):
        snake.species = '   '
    with pytest.raises(ValueError):
        snake.dietary_needs = ''
    with pytest.raises(ValueError):
        snake.dietary_needs = '   '
    with pytest.raises(ValueError):
        snake.environment = ''
    with pytest.raises(ValueError):
        snake.environment = '   '
    with pytest.raises(ValueError):
        snake.sound = ''
    with pytest.raises(ValueError):
        snake.sound = '   '
    with pytest.raises(ValueError):
        snake.skin_type = ''
    with pytest.raises(ValueError):
        snake.skin_type = '   '

# ==== Reptile Health Record Tests ====
# These tests cover the Reptile class methods related to health records:
#   - add_health_record()
#   - display_health_records()
#   - has_critical_health_issues()
#   - can_be_moved()
# They check valid additions, type safety, duplicate handling, and critical health logic.

def test_add_health_record_reptile(snake):
    """Test adding a single HealthRecord to a Reptile."""
    rec = HealthRecord('Shedding', '2025-11-09', 'Low', 'Routine check')
    msg = snake.add_health_record(rec)
    # Confirm addition message
    assert msg == 'Health record added to Python.'
    # Ensure record is present
    records = snake.display_health_records()
    assert isinstance(records, list)
    assert len(records) == 1
    assert records[0] == rec

def test_add_multiple_health_records_reptile(snake):
    """Test adding multiple HealthRecord objects to a Reptile."""
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Follow-up')
    rec2 = HealthRecord('Injury', '2025-11-10', 'Critical', 'Immediate attention')
    snake.add_health_record(rec1)
    snake.add_health_record(rec2)
    records = snake.display_health_records()
    assert len(records) == 2
    assert rec1 in records
    assert rec2 in records

def test_add_invalid_health_record_reptile(snake):
    """Adding an invalid health record type should raise TypeError."""
    with pytest.raises(TypeError):
        snake.add_health_record(123)  # Not a HealthRecord instance

def test_duplicate_health_record_reptile(snake):
    """Adding the same HealthRecord twice should return a duplicate message."""
    rec = HealthRecord('Shedding', '2025-11-09', 'Low', 'Routine check')
    msg1 = snake.add_health_record(rec)
    msg2 = snake.add_health_record(rec)  # Duplicate
    assert msg1 == 'Health record added to Python.'
    assert msg2 == 'Record already exists for Python.'

def test_has_critical_health_issues_reptile(snake):
    """Check has_critical_health_issues detects critical records correctly."""
    # No records → not critical
    assert snake.has_critical_health_issues() is False

    # Add non-critical record
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Routine check')
    snake.add_health_record(rec1)
    assert snake.has_critical_health_issues() is False

    # Add critical record
    rec2 = HealthRecord('Injury', '2025-11-10', 'Critical', 'Immediate attention')
    snake.add_health_record(rec2)
    assert snake.has_critical_health_issues() is True

def test_can_be_moved_reptile(snake):
    """Verify can_be_moved returns False if there are critical health issues."""
    # Initially no records, safe to move
    assert snake.can_be_moved() is True

    # Add non-critical record, still safe
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Low', 'Routine check')
    snake.add_health_record(rec1)
    assert snake.can_be_moved() is True

    # Add critical record, cannot move
    rec2 = HealthRecord('Surgery', '2025-11-10', 'Critical', 'Immediate attention')
    snake.add_health_record(rec2)
    assert snake.can_be_moved() is False

def test_display_health_records_empty_reptile(snake):
    """Display health records returns message if there are no records."""
    records = snake.display_health_records()
    assert isinstance(records, list)
    assert records == []

def test_display_health_records_nonempty_reptile(snake):
    """Display health records returns a list of HealthRecord objects when present."""
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Medium', 'Routine check')
    rec2 = HealthRecord('Shedding', '2025-11-09', 'Low', 'Routine check')
    snake.add_health_record(rec1)
    snake.add_health_record(rec2)
    records = snake.display_health_records()
    assert isinstance(records, list)
    assert all(isinstance(r, HealthRecord) for r in records)
    assert rec1 in records
    assert rec2 in records

# ==== String Method Tests ====
# Checks that __str__ returns a properly formatted description
def test_reptile_str(snake):
    """Test __str__ output for Reptile."""
    st = str(snake)
    assert 'Name: Python' in st
    assert 'Species: Snake' in st
    assert 'Age: 4' in st
    assert 'Dietary needs: Carnivore' in st
    assert 'Environment: Jungle' in st
    assert 'Sound: Hiss' in st
    assert 'Skin type: Scaly' in st
    assert 'Blood type: Cold-blooded' in st
    assert 'Is Venomous: True' in st

# ==== Equality Tests ====
# Verifies __eq__ behavior for identical and different Reptiles, and non-Reptile comparisons
def test_reptile_equality():
    """Test __eq__ for Reptile objects."""
    r1 = Reptile('Python', 'Snake', 4, 'Carnivore', 'Jungle', 'Hiss', 'Scaly', 'Cold-blooded', True)
    r2 = Reptile('Python', 'Snake', 4, 'Carnivore', 'Jungle', 'Hiss', 'Scaly', 'Cold-blooded', True)
    r3 = Reptile('Kobra', 'Snake', 3, 'Carnivore', 'Grasslands', 'Sss', 'Smooth', 'Cold-blooded', False)
    assert r1 == r2
    assert r1 != r3

def test_reptile_equality_with_different_type(snake):
    """Ensure Reptile __eq__ returns False when compared to non-Reptile object."""
    assert snake != 'not a reptile'

# ===============================================
#        Bird Tests
# ===============================================
# Test the Bird subclass, including methods, properties, edge cases, health records,
# string representation, and equality checks.

# ==== Fixture for Bird ====
# Provides a default Bird instance for testing
@pytest.fixture
def parrot():
    """Fixture to create a default Bird instance for testing."""
    return Bird('Polly', 'Parrot', 2, 'Seeds', 'Tropical', 'Squawk', 'Colorful', 'Warm-blooded', True)


# ==== Method Tests ====
# Checks primary actions for Bird
def test_bird_methods(parrot):
    """Test eat, sleep, and make_sound for Bird."""
    assert parrot.eat() == 'Polly the Parrot is eating Seeds.'
    assert parrot.sleep() == 'Polly the Parrot is sleeping.'
    assert parrot.make_sound() == 'Polly Squawk!'


# ==== Property Getters and Setter Tests ====
# Checks that all properties can be retrieved and updated correctly
def test_bird_properties(parrot):
    """Test getters and valid setters for Bird properties."""
    # Test getters
    assert parrot.name == 'Polly'
    assert parrot.species == 'Parrot'
    assert parrot.age == 2
    assert parrot.dietary_needs == 'Seeds'
    assert parrot.environment == 'Tropical'
    assert parrot.sound == 'Squawk'
    assert parrot.feather_type == 'Colorful'
    assert parrot.blood_type == 'Warm-blooded'
    assert parrot.can_fly == True

    # Test setters
    parrot.name = 'Kiwi'
    assert parrot.name == 'Kiwi'
    parrot.age = 3
    assert parrot.age == 3
    parrot.dietary_needs = 'Vegetables'
    assert parrot.dietary_needs == 'Vegetables'
    parrot.environment = 'Cage'
    assert parrot.environment == 'Cage'
    parrot.sound = 'Chirp'
    assert parrot.sound == 'Chirp'
    parrot.feather_type = 'Green'
    assert parrot.feather_type == 'Green'
    parrot.can_fly = False
    assert parrot.can_fly == False


# ==== Edge Case and invalid input Tests ====
# Verifies that invalid types and empty/whitespace strings raise appropriate exceptions
def test_bird_edge_setters(parrot):
    """Test that invalid types and empty/whitespace strings raise TypeError or ValueError for Bird."""
    # Type errors
    with pytest.raises(TypeError):
        parrot.name = 123
    with pytest.raises(TypeError):
        parrot.species = 123
    with pytest.raises(TypeError):
        parrot.age = 'Two'
    with pytest.raises(TypeError):
        parrot.age = True
    with pytest.raises(TypeError):
        parrot.age = False
    with pytest.raises(TypeError):
        parrot.dietary_needs = 99
    with pytest.raises(TypeError):
        parrot.environment = 10
    with pytest.raises(TypeError):
        parrot.sound = 1
    with pytest.raises(TypeError):
        parrot.feather_type = 45
    with pytest.raises(TypeError):
        parrot.can_fly = 'Yes'  # must be bool

    # Value errors / invalid values
    with pytest.raises(ValueError):
        parrot.age = -1
    with pytest.raises(ValueError):
        parrot.name = ''
    with pytest.raises(ValueError):
        parrot.name = '   '
    with pytest.raises(ValueError):
        parrot.species = ''
    with pytest.raises(ValueError):
        parrot.species = '   '
    with pytest.raises(ValueError):
        parrot.dietary_needs = ''
    with pytest.raises(ValueError):
        parrot.dietary_needs = '   '
    with pytest.raises(ValueError):
        parrot.environment = ''
    with pytest.raises(ValueError):
        parrot.environment = '   '
    with pytest.raises(ValueError):
        parrot.sound = ''
    with pytest.raises(ValueError):
        parrot.sound = '   '
    with pytest.raises(ValueError):
        parrot.feather_type = ''
    with pytest.raises(ValueError):
        parrot.feather_type = '   '


# ==== Health Record Tests ====
# These tests cover the Bird class methods related to health records:
#   - add_health_record()
#   - display_health_records()
#   - has_critical_health_issues()
#   - can_be_moved()
# They check valid additions, type safety, duplicate handling, and critical health logic.
def test_add_health_record_bird(parrot):
    """Test adding a single HealthRecord to a Bird."""
    rec = HealthRecord('Wing Check', '2025-11-09', 'Low', 'Routine check')
    msg = parrot.add_health_record(rec)
    assert msg == 'Health record added to Polly.'
    records = parrot.display_health_records()
    assert isinstance(records, list)
    assert len(records) == 1
    assert records[0] == rec

def test_add_multiple_health_records_bird(parrot):
    """Test adding multiple HealthRecord objects to a Bird."""
    rec1 = HealthRecord('Beak Trim', '2025-11-09', 'Medium', 'Follow-up')
    rec2 = HealthRecord('Wing Injury', '2025-11-10', 'Critical', 'Immediate attention')
    parrot.add_health_record(rec1)
    parrot.add_health_record(rec2)
    records = parrot.display_health_records()
    assert len(records) == 2
    assert rec1 in records
    assert rec2 in records

def test_add_invalid_health_record_bird(parrot):
    """Adding an invalid health record type should raise TypeError for Bird."""
    with pytest.raises(TypeError):
        parrot.add_health_record(123)

def test_duplicate_health_record_bird(parrot):
    """Adding the same HealthRecord twice should return a duplicate message for Bird."""
    rec = HealthRecord('Wing Check', '2025-11-09', 'Low', 'Routine check')
    msg1 = parrot.add_health_record(rec)
    msg2 = parrot.add_health_record(rec)
    assert msg1 == 'Health record added to Polly.'
    assert msg2 == 'Record already exists for Polly.'

def test_has_critical_health_issues_bird(parrot):
    """Check has_critical_health_issues detects critical records correctly for Bird."""
    assert parrot.has_critical_health_issues() is False
    rec1 = HealthRecord('Routine Check', '2025-11-09', 'Low', 'Checkup')
    parrot.add_health_record(rec1)
    assert parrot.has_critical_health_issues() is False
    rec2 = HealthRecord('Wing Fracture', '2025-11-10', 'Critical', 'Immediate attention')
    parrot.add_health_record(rec2)
    assert parrot.has_critical_health_issues() is True

def test_can_be_moved_bird(parrot):
    """Verify can_be_moved returns False if Bird has critical health issues."""
    assert parrot.can_be_moved() is True
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Low', 'Routine')
    parrot.add_health_record(rec1)
    assert parrot.can_be_moved() is True
    rec2 = HealthRecord('Injury', '2025-11-10', 'Critical', 'Immediate')
    parrot.add_health_record(rec2)
    assert parrot.can_be_moved() is False

def test_display_health_records_empty_bird(parrot):
    """Display health records returns message if Bird has no records."""
    records = parrot.display_health_records()
    assert isinstance(records, list)
    assert records == []

def test_display_health_records_nonempty_bird(parrot):
    """Display health records returns a list of HealthRecord objects for Bird."""
    rec1 = HealthRecord('Checkup', '2025-11-09', 'Low', 'Routine')
    rec2 = HealthRecord('Wing Check', '2025-11-09', 'Medium', 'Follow-up')
    parrot.add_health_record(rec1)
    parrot.add_health_record(rec2)
    records = parrot.display_health_records()
    assert isinstance(records, list)
    assert all(isinstance(r, HealthRecord) for r in records)
    assert rec1 in records
    assert rec2 in records


# ==== String Method Tests ====
# Checks that __str__ returns a properly formatted description
def test_bird_str(parrot):
    """Test __str__ output for Bird."""
    st = str(parrot)
    assert 'Name: Polly' in st
    assert 'Species: Parrot' in st
    assert 'Age: 2' in st
    assert 'Dietary needs: Seeds' in st
    assert 'Environment: Tropical' in st
    assert 'Sound: Squawk' in st
    assert 'Feather type: Colorful' in st
    assert 'Blood type: Warm-blooded' in st
    assert 'Can Fly: True' in st


# ==== Equality Tests ====
# Verifies __eq__ behavior for identical and different Birds, and non-Bird comparisons
def test_bird_equality():
    """Test __eq__ for Bird objects."""
    b1 = Bird('Polly', 'Parrot', 2, 'Seeds', 'Tropical', 'Squawk', 'Colorful', 'Warm-blooded', True)
    b2 = Bird('Polly', 'Parrot', 2, 'Seeds', 'Tropical', 'Squawk', 'Colorful', 'Warm-blooded', True)
    b3 = Bird('Kiwi', 'Parrot', 1, 'Seeds', 'Cage', 'Chirp', 'Green', 'Warm-blooded', False)
    assert b1 == b2
    assert b1 != b3



def test_bird_equality_with_different_type(parrot):
    """Ensure Bird __eq__ returns False when compared to non-Bird object."""
    assert parrot != 'not a bird'