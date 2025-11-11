"""
File: test_staff.py
Description: Test suite for the Staff base class and its subclasses (Zookeeper and Veterinarian).
This module verifies class inheritance, property validation, methods, assignment limits,
string representation, equality checks, and proper exception handling.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from staff import Staff, Zookeeper, Veterinarian
from animal import Animal, Mammal, Reptile, Bird
from enclosure import Enclosure
from health_record import HealthRecord


# ===============================================
#        Staff Base Class Tests
# ===============================================
# Test the Staff abstract base class including inheritance, properties, validation,
# assignment methods, and equality checks.

# ============================ Fixtures ==============================================================
@pytest.fixture
def zookeeper():
    """Fixture to create a default Zookeeper instance for testing."""
    return Zookeeper('John', 101)

@pytest.fixture
def veterinarian():
    """Fixture to create a default Veterinarian instance for testing."""
    return Veterinarian('Dr. Smith', 201)

@pytest.fixture
def sample_lion():
    """Fixture to create a sample Mammal instance for assignment tests."""
    return Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long', 'Warm-blooded')

@pytest.fixture
def sample_tiger():
    """Fixture to create another sample Mammal instance for assignment tests."""
    return Mammal('Raja', 'Tiger', 4, 'Carnivore', 'Savannah', 'Growl', 'Striped', 'Warm-blooded')

@pytest.fixture
def sample_enclosure():
    """Fixture to create a sample Enclosure instance for assignment tests."""
    return Enclosure('Large', 'Savannah', Mammal, 80)

# ============================ Inheritance and Abstract Class Tests ===================================
# Test that Staff is abstract and subclasses inherit correctly

def test_staff_is_abstract():
    """Verify that Staff cannot be instantiated directly since it is abstract."""
    # Attempting to instantiate abstract Staff class should raise TypeError
    with pytest.raises(TypeError):
        Staff('John', 101, 'Worker')

def test_zookeeper_inheritance(zookeeper):
    """Verify that Zookeeper is an instance of Staff."""
    # Check that zookeeper is an instance of Staff
    assert isinstance(zookeeper, Staff)
    # Verify role is set correctly
    assert zookeeper.role == 'Zookeeper'

def test_veterinarian_inheritance(veterinarian):
    """Verify that Veterinarian is an instance of Staff."""
    # Check that veterinarian is an instance of Staff
    assert isinstance(veterinarian, Staff)
    # Verify role is set correctly
    assert veterinarian.role == 'Veterinarian'


# ============================ Property Tests =========================================================
# Test that properties work correctly for both getters and setters

def test_staff_properties(zookeeper):
    """Test getters and valid setters for Staff properties."""
    # Test getters
    assert zookeeper.name == 'John'
    assert zookeeper.staff_id == 101
    assert zookeeper.role == 'Zookeeper'
    assert zookeeper.assigned_animals == []
    assert zookeeper.assigned_enclosures == []

    # Test valid setters
    zookeeper.name = 'Jane'
    assert zookeeper.name == 'Jane'
    zookeeper.role = 'Senior Zookeeper'
    assert zookeeper.role == 'Senior Zookeeper'


def test_staff_id_read_only(zookeeper):
    """Test that staff_id is read-only and cannot be modified."""
    # staff_id should not have a setter
    with pytest.raises(AttributeError):
        zookeeper.staff_id = 999


def test_assigned_lists_read_only(zookeeper, sample_lion):
    """Test that assigned_animals and assigned_enclosures return copies."""
    # Assign an animal
    zookeeper.assign_animal(sample_lion)

    # Get the list
    animals_list = zookeeper.assigned_animals

    # Modifying the returned list should not affect the internal list
    animals_list.append('fake animal')

    # Internal list should still have only one animal
    assert len(zookeeper.assigned_animals) == 1


# ============================ Validation Tests =======================================================
# Test that invalid inputs raise appropriate exceptions

def test_name_validation(zookeeper):
    """Test that invalid name values raise TypeError or ValueError."""
    # Type error: name must be a string
    with pytest.raises(TypeError):
        zookeeper.name = 123

    # Value error: name cannot be empty
    with pytest.raises(ValueError):
        zookeeper.name = ''

    # Value error: name cannot be whitespace
    with pytest.raises(ValueError):
        zookeeper.name = '   '


def test_role_validation(zookeeper):
    """Test that invalid role values raise TypeError or ValueError."""
    # Type error: role must be a string
    with pytest.raises(TypeError):
        zookeeper.role = 456

    # Value error: role cannot be empty
    with pytest.raises(ValueError):
        zookeeper.role = ''

    # Value error: role cannot be whitespace
    with pytest.raises(ValueError):
        zookeeper.role = '   '


# ============================ Assign Animal Tests ====================================================
# Test assigning animals to staff members with various edge cases

def test_assign_animal_valid(zookeeper, sample_lion):
    """Test assigning a valid animal to a staff member."""
    # Assign animal
    msg = zookeeper.assign_animal(sample_lion)

    # Check confirmation message
    assert 'Simba the Lion has been assigned.' in msg

    # Verify animal is in assigned list
    assert sample_lion in zookeeper.assigned_animals
    assert len(zookeeper.assigned_animals) == 1


def test_assign_multiple_animals(zookeeper, sample_lion, sample_tiger):
    """Test assigning multiple animals to a staff member."""
    # Assign first animal
    zookeeper.assign_animal(sample_lion)
    # Assign second animal
    zookeeper.assign_animal(sample_tiger)

    # Verify both animals are assigned
    assert len(zookeeper.assigned_animals) == 2
    assert sample_lion in zookeeper.assigned_animals
    assert sample_tiger in zookeeper.assigned_animals


def test_assign_animal_invalid_type(zookeeper):
    """Test that assigning a non-Animal object raises TypeError."""
    # Type error: must be Animal instance
    with pytest.raises(TypeError):
        zookeeper.assign_animal('not an animal')

    with pytest.raises(TypeError):
        zookeeper.assign_animal(123)


def test_assign_duplicate_animal(zookeeper, sample_lion):
    """Test that assigning the same animal twice raises ValueError."""
    # Assign animal once
    zookeeper.assign_animal(sample_lion)

    # Attempting to assign again should raise ValueError
    with pytest.raises(ValueError):
        zookeeper.assign_animal(sample_lion)


def test_assign_animal_max_limit(zookeeper):
    """Test that assigning more than MAX_ANIMALS_PER_STAFF raises ValueError."""
    # Assign maximum number of animals
    for i in range(Staff.MAX_ANIMALS_PER_STAFF):
        animal = Mammal(f'Animal{i}', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long', 'Warm-blooded')
        zookeeper.assign_animal(animal)

    # Attempting to assign one more should raise ValueError
    extra_animal = Mammal('Extra', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long', 'Warm-blooded')
    with pytest.raises(ValueError):
        zookeeper.assign_animal(extra_animal)


# ============================ Assign Enclosure Tests =================================================
# Test assigning enclosures to staff members with various edge cases

def test_assign_enclosure_valid(zookeeper, sample_enclosure):
    """Test assigning a valid enclosure to a staff member."""
    # Assign enclosure
    msg = zookeeper.assign_enclosure(sample_enclosure)

    # Check confirmation message
    assert 'Savannah enclosure has been assigned.' in msg

    # Verify enclosure is in assigned list
    assert sample_enclosure in zookeeper.assigned_enclosures
    assert len(zookeeper.assigned_enclosures) == 1


def test_assign_multiple_enclosures(zookeeper):
    """Test assigning multiple enclosures to a staff member."""
    # Create two enclosures
    enc1 = Enclosure('Large', 'Savannah', Mammal, 80)
    enc2 = Enclosure('Medium', 'Jungle', Mammal, 90)

    # Assign both enclosures
    zookeeper.assign_enclosure(enc1)
    zookeeper.assign_enclosure(enc2)

    # Verify both are assigned
    assert len(zookeeper.assigned_enclosures) == 2
    assert enc1 in zookeeper.assigned_enclosures
    assert enc2 in zookeeper.assigned_enclosures


def test_assign_enclosure_invalid_type(zookeeper):
    """Test that assigning a non-Enclosure object raises TypeError."""
    # Type error: must be Enclosure instance
    with pytest.raises(TypeError):
        zookeeper.assign_enclosure('not an enclosure')

    with pytest.raises(TypeError):
        zookeeper.assign_enclosure(456)


def test_assign_duplicate_enclosure(zookeeper, sample_enclosure):
    """Test that assigning the same enclosure twice raises ValueError."""
    # Assign enclosure once
    zookeeper.assign_enclosure(sample_enclosure)

    # Attempting to assign again should raise ValueError
    with pytest.raises(ValueError):
        zookeeper.assign_enclosure(sample_enclosure)


def test_assign_enclosure_max_limit(zookeeper):
    """Test that assigning more than MAX_ENCLOSURES_PER_STAFF raises ValueError."""
    # Assign maximum number of enclosures
    for i in range(Staff.MAX_ENCLOSURES_PER_STAFF):
        enclosure = Enclosure('Large', f'Environment{i}', Mammal, 80)
        zookeeper.assign_enclosure(enclosure)

    # Attempting to assign one more should raise ValueError
    extra_enclosure = Enclosure('Large', 'Extra', Mammal, 80)
    with pytest.raises(ValueError):
        zookeeper.assign_enclosure(extra_enclosure)


# ============================ String Method Test =====================================================
# Test that __str__ returns a properly formatted string

def test_staff_str_empty_assignments(zookeeper):
    """Test __str__ output when staff has no assignments."""
    st = str(zookeeper)
    assert 'Staff Name: John' in st
    assert 'Staff ID: 101' in st
    assert 'Role: Zookeeper' in st
    assert 'Assigned Animals: None' in st
    assert 'Assigned Enclosures: None' in st


def test_staff_str_with_assignments(zookeeper, sample_lion, sample_enclosure):
    """Test __str__ output when staff has assignments."""
    # Assign animal and enclosure
    zookeeper.assign_animal(sample_lion)
    zookeeper.assign_enclosure(sample_enclosure)

    st = str(zookeeper)
    assert 'Staff Name: John' in st
    assert 'Staff ID: 101' in st
    assert 'Role: Zookeeper' in st
    assert 'Assigned Animals: Simba (Lion)' in st
    assert 'Assigned Enclosures: Savannah enclosure' in st


# ============================ Equality Tests =========================================================
# Test that __eq__ correctly compares Staff objects by staff_id

def test_staff_equality_same_id():
    """Test that staff with the same ID are considered equal."""
    keeper1 = Zookeeper('John', 101)
    keeper2 = Zookeeper('John', 101)

    # Same staff_id should be equal
    assert keeper1 == keeper2


def test_staff_equality_different_id():
    """Test that staff with different IDs are not equal."""
    keeper1 = Zookeeper('John', 101)
    keeper2 = Zookeeper('Jane', 102)

    # Different staff_id should not be equal
    assert keeper1 != keeper2


def test_staff_equality_different_types():
    """Test that staff equality works across Zookeeper and Veterinarian."""
    keeper = Zookeeper('John', 101)
    vet = Veterinarian('John', 101)

    # Same staff_id, different roles, should still be equal
    assert keeper == vet


def test_staff_equality_with_non_staff(zookeeper):
    """Test that comparing staff with non-Staff object returns False."""
    # Comparing with non-Staff object
    assert zookeeper != 'not a staff'
    assert zookeeper != 101


# ===============================================
#        Zookeeper Tests
# ===============================================
# Test Zookeeper specific methods including feeding animals and cleaning enclosures

# ============================ Initialization Test ====================================================

def test_zookeeper_initialization():
    """Test that Zookeeper initializes with correct role."""
    keeper = Zookeeper('John', 101)
    assert keeper.name == 'John'
    assert keeper.staff_id == 101
    assert keeper.role == 'Zookeeper'


# ============================ Feed Animal Tests ======================================================

def test_feed_animal_valid(zookeeper, sample_lion):
    """Test feeding an assigned animal."""
    # Assign animal first
    zookeeper.assign_animal(sample_lion)

    # Feed the animal
    msg = zookeeper.feed_animal(sample_lion)

    # Check confirmation message
    assert 'John (Zookeeper) feeds Simba the Lion.' in msg


def test_feed_animal_not_assigned(zookeeper, sample_lion):
    """Test that feeding an unassigned animal raises ValueError."""
    # Do not assign the animal

    # Attempting to feed should raise ValueError
    with pytest.raises(ValueError):
        zookeeper.feed_animal(sample_lion)


def test_feed_animal_invalid_type(zookeeper):
    """Test that feeding a non-Animal object raises TypeError."""
    # Type error: must be Animal instance
    with pytest.raises(TypeError):
        zookeeper.feed_animal('not an animal')


# ============================ Clean Enclosure Tests ==================================================

def test_clean_enclosure_valid(zookeeper, sample_enclosure):
    """Test cleaning an assigned enclosure."""
    # Assign enclosure first
    zookeeper.assign_enclosure(sample_enclosure)

    # Clean the enclosure
    msg = zookeeper.clean_enclosure(sample_enclosure)

    # Check confirmation message
    assert 'John (Zookeeper) cleaned the Savannah enclosure' in msg
    # Verify enclosure cleanliness is now 100
    assert sample_enclosure.cleanliness_level == 100


def test_clean_enclosure_not_assigned(zookeeper, sample_enclosure):
    """Test that cleaning an unassigned enclosure raises ValueError."""
    # Do not assign the enclosure

    # Attempting to clean should raise ValueError
    with pytest.raises(ValueError):
        zookeeper.clean_enclosure(sample_enclosure)


def test_clean_enclosure_invalid_type(zookeeper):
    """Test that cleaning a non-Enclosure object raises TypeError."""
    # Type error: must be Enclosure instance
    with pytest.raises(TypeError):
        zookeeper.clean_enclosure('not an enclosure')


# ============================ Perform Duties Test ====================================================

def test_zookeeper_perform_duties_empty(zookeeper):
    """Test perform duties when no animals or enclosures are assigned."""
    duties = zookeeper.perform_duties()

    assert 'John (Zookeeper) performed duties.' in duties
    assert 'Feed Animals: None' in duties
    assert 'Cleaning Enclosures: None' in duties


def test_zookeeper_perform_duties_with_assignments(zookeeper, sample_lion, sample_tiger, sample_enclosure):
    """Test perform duties when animals and enclosures are assigned."""
    # Assign animals and enclosure
    zookeeper.assign_animal(sample_lion)
    zookeeper.assign_animal(sample_tiger)
    zookeeper.assign_enclosure(sample_enclosure)

    duties = zookeeper.perform_duties()

    assert 'John (Zookeeper) performed duties.' in duties
    assert 'Simba (Lion)' in duties
    assert 'Raja (Tiger)' in duties
    assert 'Savannah enclosure' in duties

# ===============================================
#        Veterinarian Tests
# ===============================================
# Test Veterinarian specific methods including health checks and health record updates

# ============================ Initialization Test ====================================================

def test_veterinarian_initialization():
    """Test that Veterinarian initializes with correct role."""
    vet = Veterinarian('Dr. Smith', 201)
    assert vet.name == 'Dr. Smith'
    assert vet.staff_id == 201
    assert vet.role == 'Veterinarian'


# ============================ Conduct Health Check Tests =============================================

def test_conduct_health_check_valid(veterinarian, sample_lion):
    """Test conducting a health check on an assigned animal."""
    # Assign animal first
    veterinarian.assign_animal(sample_lion)

    # Conduct health check
    msg = veterinarian.conduct_health_check(sample_lion)

    # Check confirmation message
    assert 'Dr. Smith (Veterinarian) conducted a health check on Simba the Lion.' in msg


def test_conduct_health_check_not_assigned(veterinarian, sample_lion):
    """Test that checking an unassigned animal raises ValueError."""
    # Do not assign the animal

    # Attempting to check should raise ValueError
    with pytest.raises(ValueError):
        veterinarian.conduct_health_check(sample_lion)


def test_conduct_health_check_invalid_type(veterinarian):
    """Test that checking a non-Animal object raises TypeError."""
    # Type error: must be Animal instance
    with pytest.raises(TypeError):
        veterinarian.conduct_health_check('not an animal')


# ============================ Update Health Record Tests =============================================

def test_update_health_record_valid(veterinarian, sample_lion):
    """Test updating an animal's health record."""
    # Assign animal first
    veterinarian.assign_animal(sample_lion)

    # Create a health record
    record = HealthRecord('Checkup', '2025-11-10', 'low', 'Routine')

    # Update health record
    msg = veterinarian.update_health_record(sample_lion, record)

    # Check confirmation message
    assert 'Dr. Smith (Veterinarian)' in msg
    assert 'Health record added to Simba.' in msg

    # Verify record was added to animal
    records = sample_lion.display_health_records()
    assert len(records) == 1
    assert records[0] == record


def test_update_health_record_animal_not_assigned(veterinarian, sample_lion):
    """Test that updating record for unassigned animal raises ValueError."""
    # Do not assign the animal
    record = HealthRecord('Checkup', '2025-11-10', 'low', 'Routine')

    # Attempting to update should raise ValueError
    with pytest.raises(ValueError):
        veterinarian.update_health_record(sample_lion, record)


def test_update_health_record_invalid_animal_type(veterinarian):
    """Test that updating with non-Animal object raises TypeError."""
    record = HealthRecord('Checkup', '2025-11-10', 'low', 'Routine')

    # Type error: animal must be Animal instance
    with pytest.raises(TypeError):
        veterinarian.update_health_record('not an animal', record)


def test_update_health_record_invalid_record_type(veterinarian, sample_lion):
    """Test that updating with non-HealthRecord object raises TypeError."""
    # Assign animal first
    veterinarian.assign_animal(sample_lion)

    # Type error: record must be HealthRecord instance
    with pytest.raises(TypeError):
        veterinarian.update_health_record(sample_lion, 'not a record')


# ============================ Perform Duties Test ====================================================

def test_veterinarian_perform_duties_empty(veterinarian):
    """Test perform_duties when no animals are assigned."""
    duties = veterinarian.perform_duties()

    assert 'Dr. Smith (Veterinarian) performed duties.' in duties
    assert 'Animals Checked: None' in duties
    assert 'Health Records Updated: None' in duties


def test_veterinarian_perform_duties_with_animals(veterinarian, sample_lion):
    """Test perform_duties when animals are assigned."""
    # Assign animal
    veterinarian.assign_animal(sample_lion)

    duties = veterinarian.perform_duties()

    assert 'Dr. Smith (Veterinarian) performed duties.' in duties
    assert 'Simba (Lion)' in duties
    assert 'Health Records Updated: None' in duties  # No records yet


def test_veterinarian_perform_duties_with_health_records(veterinarian, sample_lion, sample_tiger):
    """Test perform_duties when animals have health records."""
    # Assign animals
    veterinarian.assign_animal(sample_lion)
    veterinarian.assign_animal(sample_tiger)

    # Add health records
    record1 = HealthRecord('Checkup', '2025-11-10', 'low', 'Routine')
    record2 = HealthRecord('Injury', '2025-11-11', 'critical', 'Immediate care')
    veterinarian.update_health_record(sample_lion, record1)
    veterinarian.update_health_record(sample_tiger, record2)

    duties = veterinarian.perform_duties()

    assert 'Dr. Smith (Veterinarian) performed duties.' in duties
    assert 'Simba (Lion)' in duties
    assert 'Raja (Tiger)' in duties
    assert 'Simba: Checkup (low) reported on 2025-11-10' in duties
    assert 'Raja: Injury (critical) reported on 2025-11-11' in duties
