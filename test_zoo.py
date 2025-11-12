"""
File: test_zoo.py
Description: Test suite for the Zoo class.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from zoo import Zoo
from animal import Mammal, Bird
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord


# ============================ Fixtures ===============================================================
@pytest.fixture
def zoo():
    """Fixture to create a default Zoo instance for testing."""
    return Zoo('Taronga Zoo')


@pytest.fixture
def sample_lion():
    """Fixture to create a sample Mammal for testing."""
    return Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Golden', 'Warm-blooded')


@pytest.fixture
def sample_tiger():
    """Fixture to create another sample Mammal for testing."""
    return Mammal('Luna', 'Tiger', 4, 'Carnivore', 'Savannah', 'Growl', 'Striped', 'Warm-blooded')


@pytest.fixture
def sample_parrot():
    """Fixture to create a sample Bird for testing."""
    return Bird('Polly', 'Parrot', 2, 'Seeds', 'Tropical', 'Squawk', 'Colorful', 'Warm-blooded', True)


@pytest.fixture
def sample_enclosure():
    """Fixture to create a sample Enclosure for testing."""
    return Enclosure('Large', 'Savannah', Mammal, 80)


@pytest.fixture
def sample_zookeeper():
    """Fixture to create a sample Zookeeper for testing."""
    return Zookeeper('John', 101)


@pytest.fixture
def sample_vet():
    """Fixture to create a sample Veterinarian for testing."""
    return Veterinarian('Dr. Smith', 201)


# ===============================================
#        Initialization & Properties Tests
# ===============================================
# Test Zoo class initialization, properties, and validation

# ============================ Initialization Tests ===============================================
# Test that the Zoo initializes correctly with given parameters

def test_zoo_initialization(zoo):
    """Test that Zoo initializes correctly with given name."""
    assert zoo.name == 'Taronga Zoo'
    assert zoo.animals == []
    assert zoo.enclosures == []
    assert zoo.staff == []


def test_zoo_initialization_with_different_names():
    """Test Zoo initialization with different Australian zoo names."""
    zoo1 = Zoo('Sydney Zoo')
    assert zoo1.name == 'Sydney Zoo'

    zoo2 = Zoo('Global Wildlife')
    assert zoo2.name == 'Global Wildlife'

    zoo3 = Zoo('Australia Zoo')
    assert zoo3.name == 'Australia Zoo'


# ============================ Property Getter Tests ==============================================
# Test that property getters return correct values

def test_zoo_name_getter(zoo):
    """Test that name property getter works correctly."""
    assert zoo.name == 'Taronga Zoo'


def test_zoo_animals_getter(zoo):
    """Test that animals property returns empty list initially."""
    assert isinstance(zoo.animals, list)
    assert zoo.animals == []


def test_zoo_enclosures_getter(zoo):
    """Test that enclosures property returns empty list initially."""
    assert isinstance(zoo.enclosures, list)
    assert zoo.enclosures == []


def test_zoo_staff_getter(zoo):
    """Test that staff property returns empty list initially."""
    assert isinstance(zoo.staff, list)
    assert zoo.staff == []


# ============================ Property Setter Tests ==============================================
# Test that property setters work correctly with valid values

def test_zoo_name_setter(zoo):
    """Test that name property setter works with valid values."""
    # Test setter with valid value
    zoo.name = 'Wildlife Sydney Zoo'
    assert zoo.name == 'Wildlife Sydney Zoo'

    # Test setter with another valid value
    zoo.name = 'Featherdale Wildlife Park'
    assert zoo.name == 'Featherdale Wildlife Park'


# ============================ Read-Only Property Tests ===========================================
# Test that animals, enclosures, and staff properties return copies (read-only)

def test_zoo_animals_property_returns_copy(zoo, sample_lion):
    """Test that animals property returns a copy (read-only)."""
    # Manually add to internal list for testing
    zoo._Zoo__animals.append(sample_lion)

    # Get the list
    animals_list = zoo.animals

    # Modify the returned list
    animals_list.append('fake animal')

    # Internal list should be unchanged
    assert len(zoo.animals) == 1
    assert 'fake animal' not in zoo.animals


def test_zoo_enclosures_property_returns_copy(zoo, sample_enclosure):
    """Test that enclosures property returns a copy (read-only)."""
    # Manually add to internal list for testing
    zoo._Zoo__enclosures.append(sample_enclosure)

    # Get the list
    enclosures_list = zoo.enclosures

    # Modify the returned list
    enclosures_list.append('fake enclosure')

    # Internal list should be unchanged
    assert len(zoo.enclosures) == 1
    assert 'fake enclosure' not in zoo.enclosures


def test_zoo_staff_property_returns_copy(zoo, sample_zookeeper):
    """Test that staff property returns a copy (read-only)."""
    # Manually add to internal list for testing
    zoo._Zoo__staff.append(sample_zookeeper)

    # Get the list
    staff_list = zoo.staff

    # Modify the returned list
    staff_list.append('fake staff')

    # Internal list should be unchanged
    assert len(zoo.staff) == 1
    assert 'fake staff' not in zoo.staff


# ============================ Validation Tests ===================================================
# Test that invalid inputs raise appropriate exceptions

def test_zoo_name_validation_type(zoo):
    """Test that invalid name type raises TypeError."""
    # Type error: name must be a string
    with pytest.raises(TypeError):
        zoo.name = 123

    with pytest.raises(TypeError):
        zoo.name = None

    with pytest.raises(TypeError):
        zoo.name = ['Sydney Zoo']


def test_zoo_name_validation_empty(zoo):
    """Test that empty name raises ValueError."""
    # Value error: name cannot be empty
    with pytest.raises(ValueError):
        zoo.name = ''

    # Value error: name cannot be whitespace
    with pytest.raises(ValueError):
        zoo.name = '   '


def test_zoo_initialization_invalid_name():
    """Test that initializing with invalid name raises appropriate error."""
    # Type error: name must be a string
    with pytest.raises(TypeError):
        Zoo(123)

    with pytest.raises(TypeError):
        Zoo(None)

    # Value error: name cannot be empty
    with pytest.raises(ValueError):
        Zoo('')

    with pytest.raises(ValueError):
        Zoo('   ')


# ===============================================
#        Animal Management Tests
# ===============================================
# Test adding, removing, and finding animals in the zoo

# ============================ Add Animal Tests ===================================================
# Test adding animals to the zoo with various scenarios

def test_add_animal_valid(zoo, sample_lion):
    """Test adding a valid animal to the zoo."""
    msg = zoo.add_animal(sample_lion)

    # Check confirmation message
    assert 'Simba the Lion has been added to the zoo.' in msg

    # Verify animal is in zoo
    assert sample_lion in zoo.animals
    assert len(zoo.animals) == 1


def test_add_multiple_animals(zoo, sample_lion, sample_tiger, sample_parrot):
    """Test adding multiple different animals to the zoo."""
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)
    zoo.add_animal(sample_parrot)

    # Verify all animals are in zoo
    assert len(zoo.animals) == 3
    assert sample_lion in zoo.animals
    assert sample_tiger in zoo.animals
    assert sample_parrot in zoo.animals


def test_add_animal_confirms_correct_name(zoo, sample_tiger):
    """Test that adding tiger Luna returns correct confirmation."""
    msg = zoo.add_animal(sample_tiger)

    # Check that Luna is mentioned in confirmation
    assert 'Luna the Tiger has been added to the zoo.' in msg


def test_add_animal_invalid_type(zoo):
    """Test that adding a non-Animal object raises TypeError."""
    # Type error: must be Animal instance
    with pytest.raises(TypeError):
        zoo.add_animal('not an animal')

    with pytest.raises(TypeError):
        zoo.add_animal(123)

    with pytest.raises(TypeError):
        zoo.add_animal(None)


def test_add_duplicate_animal(zoo, sample_lion):
    """Test that adding the same animal twice raises ValueError."""
    # Add animal once
    zoo.add_animal(sample_lion)

    # Attempting to add again should raise ValueError
    with pytest.raises(ValueError):
        zoo.add_animal(sample_lion)


# ============================ Remove Animal Tests ================================================
# Test removing animals from the zoo

def test_remove_animal_valid(zoo, sample_lion):
    """Test removing an animal from the zoo."""
    # Add animal first
    zoo.add_animal(sample_lion)

    # Remove animal
    msg = zoo.remove_animal(sample_lion)

    # Check confirmation message
    assert 'Simba the Lion has been removed from the zoo.' in msg

    # Verify animal is not in zoo
    assert sample_lion not in zoo.animals
    assert len(zoo.animals) == 0


def test_remove_animal_from_multiple(zoo, sample_lion, sample_tiger):
    """Test removing one animal when multiple animals exist."""
    # Add multiple animals
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    # Remove one animal
    zoo.remove_animal(sample_lion)

    # Verify correct animal removed
    assert sample_lion not in zoo.animals
    assert sample_tiger in zoo.animals
    assert len(zoo.animals) == 1


def test_remove_animal_not_in_zoo(zoo, sample_lion):
    """Test that removing an animal not in zoo raises ValueError."""
    # Do not add animal

    # Attempting to remove should raise ValueError
    with pytest.raises(ValueError):
        zoo.remove_animal(sample_lion)


def test_remove_animal_invalid_type(zoo):
    """Test that removing a non-Animal object raises TypeError."""
    # Type error: must be Animal instance
    with pytest.raises(TypeError):
        zoo.remove_animal('not an animal')

    with pytest.raises(TypeError):
        zoo.remove_animal(None)


# ============================ Find Animal Tests ==================================================
# Test finding animals by name

def test_find_animal_by_name_valid(zoo, sample_lion):
    """Test finding an animal by name."""
    # Add animal first
    zoo.add_animal(sample_lion)

    # Find animal by name
    found = zoo.find_animal_by_name('Simba')

    # Verify correct animal found
    assert found == sample_lion
    assert found.name == 'Simba'
    assert found.species == 'Lion'


def test_find_animal_by_name_case_insensitive(zoo, sample_tiger):
    """Test that finding animal by name is case-insensitive."""
    # Add animal
    zoo.add_animal(sample_tiger)

    # Find with different cases
    found1 = zoo.find_animal_by_name('luna')
    found2 = zoo.find_animal_by_name('LUNA')
    found3 = zoo.find_animal_by_name('LuNa')

    # All should return the same animal
    assert found1 == sample_tiger
    assert found2 == sample_tiger
    assert found3 == sample_tiger


def test_find_animal_from_multiple(zoo, sample_lion, sample_tiger, sample_parrot):
    """Test finding a specific animal when multiple animals exist."""
    # Add multiple animals
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)
    zoo.add_animal(sample_parrot)

    # Find specific animals
    found_lion = zoo.find_animal_by_name('Simba')
    found_tiger = zoo.find_animal_by_name('Luna')
    found_parrot = zoo.find_animal_by_name('Polly')

    # Verify correct animals found
    assert found_lion == sample_lion
    assert found_tiger == sample_tiger
    assert found_parrot == sample_parrot


def test_find_animal_not_found(zoo, sample_lion):
    """Test that finding a non-existent animal raises ValueError."""
    # Add one animal
    zoo.add_animal(sample_lion)

    # Try to find non-existent animal
    with pytest.raises(ValueError):
        zoo.find_animal_by_name('NonExistent')


def test_find_animal_empty_zoo(zoo):
    """Test that finding animal in empty zoo raises ValueError."""
    # Do not add any animals

    # Try to find animal
    with pytest.raises(ValueError):
        zoo.find_animal_by_name('Simba')


def test_find_animal_invalid_name_type(zoo):
    """Test that finding with invalid name type raises TypeError."""
    # Type error: name must be a string
    with pytest.raises(TypeError):
        zoo.find_animal_by_name(123)

    with pytest.raises(TypeError):
        zoo.find_animal_by_name(None)


def test_find_animal_empty_name(zoo):
    """Test that finding with empty name raises ValueError."""
    # Value error: name cannot be empty
    with pytest.raises(ValueError):
        zoo.find_animal_by_name('')

    with pytest.raises(ValueError):
        zoo.find_animal_by_name('   ')


# ===============================================
#        Enclosure Management Tests
# ===============================================
# Test adding and removing enclosures in the zoo

# ============================ Add Enclosure Tests ================================================
# Test adding enclosures to the zoo

def test_add_enclosure_valid(zoo, sample_enclosure):
    """Test adding a valid enclosure to the zoo."""
    msg = zoo.add_enclosure(sample_enclosure)

    # Check confirmation message
    assert 'Savannah enclosure has been added to the zoo.' in msg

    # Verify enclosure is in zoo
    assert sample_enclosure in zoo.enclosures
    assert len(zoo.enclosures) == 1


def test_add_multiple_enclosures(zoo):
    """Test adding multiple different enclosures to the zoo."""
    enc1 = Enclosure('Large', 'Savannah', Mammal, 80)
    enc2 = Enclosure('Medium', 'Tropical', Bird, 90)
    enc3 = Enclosure('Small', 'Rainforest', Bird, 95)

    zoo.add_enclosure(enc1)
    zoo.add_enclosure(enc2)
    zoo.add_enclosure(enc3)

    # Verify all enclosures are in zoo
    assert len(zoo.enclosures) == 3
    assert enc1 in zoo.enclosures
    assert enc2 in zoo.enclosures
    assert enc3 in zoo.enclosures


def test_add_enclosure_invalid_type(zoo):
    """Test that adding a non-Enclosure object raises TypeError."""
    # Type error: must be Enclosure instance
    with pytest.raises(TypeError):
        zoo.add_enclosure('not an enclosure')

    with pytest.raises(TypeError):
        zoo.add_enclosure(123)

    with pytest.raises(TypeError):
        zoo.add_enclosure(None)


def test_add_duplicate_enclosure(zoo, sample_enclosure):
    """Test that adding the same enclosure twice raises ValueError."""
    # Add enclosure once
    zoo.add_enclosure(sample_enclosure)

    # Attempting to add again should raise ValueError
    with pytest.raises(ValueError):
        zoo.add_enclosure(sample_enclosure)


# ============================ Remove Enclosure Tests =============================================
# Test removing enclosures from the zoo

def test_remove_enclosure_valid(zoo, sample_enclosure):
    """Test removing an enclosure from the zoo."""
    # Add enclosure first
    zoo.add_enclosure(sample_enclosure)

    # Remove enclosure
    msg = zoo.remove_enclosure(sample_enclosure)

    # Check confirmation message
    assert 'Savannah enclosure has been removed from the zoo.' in msg

    # Verify enclosure is not in zoo
    assert sample_enclosure not in zoo.enclosures
    assert len(zoo.enclosures) == 0


def test_remove_enclosure_from_multiple(zoo):
    """Test removing one enclosure when multiple enclosures exist."""
    enc1 = Enclosure('Large', 'Savannah', Mammal, 80)
    enc2 = Enclosure('Medium', 'Tropical', Bird, 90)

    # Add multiple enclosures
    zoo.add_enclosure(enc1)
    zoo.add_enclosure(enc2)

    # Remove one enclosure
    zoo.remove_enclosure(enc1)

    # Verify correct enclosure removed
    assert enc1 not in zoo.enclosures
    assert enc2 in zoo.enclosures
    assert len(zoo.enclosures) == 1


def test_remove_enclosure_not_in_zoo(zoo, sample_enclosure):
    """Test that removing an enclosure not in zoo raises ValueError."""
    # Do not add enclosure

    # Attempting to remove should raise ValueError
    with pytest.raises(ValueError):
        zoo.remove_enclosure(sample_enclosure)


def test_remove_enclosure_with_animals(zoo, sample_enclosure, sample_lion):
    """Test that removing an enclosure with animals raises ValueError."""
    # Add enclosure
    zoo.add_enclosure(sample_enclosure)

    # Add animal to enclosure
    sample_enclosure.add_animal(sample_lion)

    # Attempting to remove enclosure with animals should raise ValueError
    with pytest.raises(ValueError):
        zoo.remove_enclosure(sample_enclosure)


def test_remove_enclosure_after_removing_animals(zoo, sample_enclosure, sample_lion):
    """Test that enclosure can be removed after all animals are removed."""
    # Add enclosure and animal
    zoo.add_enclosure(sample_enclosure)
    sample_enclosure.add_animal(sample_lion)

    # Remove animal from enclosure
    sample_enclosure.remove_animal(sample_lion)

    # Now removing enclosure should succeed
    msg = zoo.remove_enclosure(sample_enclosure)
    assert 'Savannah enclosure has been removed from the zoo.' in msg
    assert sample_enclosure not in zoo.enclosures


def test_remove_enclosure_invalid_type(zoo):
    """Test that removing a non-Enclosure object raises TypeError."""
    # Type error: must be Enclosure instance
    with pytest.raises(TypeError):
        zoo.remove_enclosure('not an enclosure')

    with pytest.raises(TypeError):
        zoo.remove_enclosure(None)


# ===============================================
#        Staff Management Tests
# ===============================================
# Test adding and removing staff members in the zoo

# ============================ Add Staff Tests ====================================================
# Test adding staff members to the zoo

def test_add_staff_zookeeper(zoo, sample_zookeeper):
    """Test adding a zookeeper to the zoo."""
    msg = zoo.add_staff(sample_zookeeper)

    # Check confirmation message
    assert 'John (Zookeeper) has been added to the zoo staff.' in msg

    # Verify staff member is in zoo
    assert sample_zookeeper in zoo.staff
    assert len(zoo.staff) == 1


def test_add_staff_veterinarian(zoo, sample_vet):
    """Test adding a veterinarian to the zoo."""
    msg = zoo.add_staff(sample_vet)

    # Check confirmation message
    assert 'Dr. Smith (Veterinarian) has been added to the zoo staff.' in msg

    # Verify staff member is in zoo
    assert sample_vet in zoo.staff
    assert len(zoo.staff) == 1


def test_add_multiple_staff(zoo, sample_zookeeper, sample_vet):
    """Test adding multiple staff members to the zoo."""
    zoo.add_staff(sample_zookeeper)
    zoo.add_staff(sample_vet)

    # Verify both staff members are in zoo
    assert len(zoo.staff) == 2
    assert sample_zookeeper in zoo.staff
    assert sample_vet in zoo.staff


def test_add_staff_invalid_type(zoo):
    """Test that adding a non-Staff object raises TypeError."""
    # Type error: must be Staff instance
    with pytest.raises(TypeError):
        zoo.add_staff('not a staff member')

    with pytest.raises(TypeError):
        zoo.add_staff(123)

    with pytest.raises(TypeError):
        zoo.add_staff(None)


def test_add_duplicate_staff(zoo, sample_zookeeper):
    """Test that adding the same staff member twice raises ValueError."""
    # Add staff member once
    zoo.add_staff(sample_zookeeper)

    # Attempting to add again should raise ValueError
    with pytest.raises(ValueError):
        zoo.add_staff(sample_zookeeper)


def test_add_staff_duplicate_by_id(zoo):
    """Test that adding staff with same ID raises ValueError."""
    keeper1 = Zookeeper('John', 101)
    keeper2 = Zookeeper('Jane', 101)  # Same ID, different name

    # Add first staff member
    zoo.add_staff(keeper1)

    # Attempting to add staff with same ID should raise ValueError
    with pytest.raises(ValueError):
        zoo.add_staff(keeper2)


# ============================ Remove Staff Tests =================================================
# Test removing staff members from the zoo

def test_remove_staff_valid(zoo, sample_zookeeper):
    """Test removing a staff member from the zoo."""
    # Add staff member first
    zoo.add_staff(sample_zookeeper)

    # Remove staff member
    msg = zoo.remove_staff(sample_zookeeper)

    # Check confirmation message
    assert 'John (Zookeeper) has been removed from the zoo staff.' in msg

    # Verify staff member is not in zoo
    assert sample_zookeeper not in zoo.staff
    assert len(zoo.staff) == 0


def test_remove_staff_from_multiple(zoo, sample_zookeeper, sample_vet):
    """Test removing one staff member when multiple staff exist."""
    # Add multiple staff members
    zoo.add_staff(sample_zookeeper)
    zoo.add_staff(sample_vet)

    # Remove one staff member
    zoo.remove_staff(sample_zookeeper)

    # Verify correct staff member removed
    assert sample_zookeeper not in zoo.staff
    assert sample_vet in zoo.staff
    assert len(zoo.staff) == 1


def test_remove_staff_not_in_zoo(zoo, sample_zookeeper):
    """Test that removing a staff member not in zoo raises ValueError."""
    # Do not add staff member

    # Attempting to remove should raise ValueError
    with pytest.raises(ValueError):
        zoo.remove_staff(sample_zookeeper)


def test_remove_staff_invalid_type(zoo):
    """Test that removing a non-Staff object raises TypeError."""
    # Type error: must be Staff instance
    with pytest.raises(TypeError):
        zoo.remove_staff('not a staff member')

    with pytest.raises(TypeError):
        zoo.remove_staff(None)

# ===============================================
#        Animal Enclosure Assignment Tests
# ===============================================
# Test assigning animals to enclosures

# ============================ Assign Animal to Enclosure Tests ===================================
# Test the assignment of animals to appropriate enclosures

def test_assign_animal_to_enclosure_valid(zoo, sample_lion, sample_enclosure):
    """Test assigning an animal to an enclosure."""
    # Add animal and enclosure to zoo first
    zoo.add_animal(sample_lion)
    zoo.add_enclosure(sample_enclosure)

    # Assign animal to enclosure
    msg = zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)

    # Check confirmation message
    assert 'Simba assigned to Savannah enclosure' in msg
    assert 'has been added to the enclosure' in msg

    # Verify animal is in enclosure
    assert sample_lion in sample_enclosure.animals


def test_assign_multiple_animals_to_enclosure(zoo, sample_lion, sample_tiger, sample_enclosure):
    """Test assigning multiple animals to the same enclosure."""
    # Add animals and enclosure to zoo
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)
    zoo.add_enclosure(sample_enclosure)

    # Assign both animals
    zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)
    zoo.assign_animal_to_enclosure(sample_tiger, sample_enclosure)

    # Verify both animals are in enclosure
    assert len(sample_enclosure.animals) == 2
    assert sample_lion in sample_enclosure.animals
    assert sample_tiger in sample_enclosure.animals


def test_assign_animal_not_in_zoo(zoo, sample_lion, sample_enclosure):
    """Test that assigning an animal not in zoo raises ValueError."""
    # Add only enclosure, not animal
    zoo.add_enclosure(sample_enclosure)

    # Attempting to assign should raise ValueError
    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)


def test_assign_animal_enclosure_not_in_zoo(zoo, sample_lion, sample_enclosure):
    """Test that assigning to an enclosure not in zoo raises ValueError."""
    # Add only animal, not enclosure
    zoo.add_animal(sample_lion)

    # Attempting to assign should raise ValueError
    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)


def test_assign_animal_wrong_type(zoo, sample_parrot, sample_enclosure):
    """Test that assigning wrong animal type to enclosure raises TypeError."""
    # Add bird and mammal enclosure
    zoo.add_animal(sample_parrot)
    zoo.add_enclosure(sample_enclosure)  # Mammal enclosure

    # Attempting to assign bird to mammal enclosure should raise TypeError
    with pytest.raises(TypeError):
        zoo.assign_animal_to_enclosure(sample_parrot, sample_enclosure)


def test_assign_animal_wrong_environment(zoo, sample_enclosure):
    """Test that assigning animal with wrong environment raises ValueError."""
    # Create animal with different environment
    jungle_lion = Mammal('Leo', 'Lion', 5, 'Carnivore', 'Jungle', 'Roar', 'Golden', 'Warm-blooded')

    # Add animal and savannah enclosure
    zoo.add_animal(jungle_lion)
    zoo.add_enclosure(sample_enclosure)  # Savannah enclosure

    # Attempting to assign jungle animal to savannah enclosure should raise ValueError
    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(jungle_lion, sample_enclosure)


def test_assign_animal_with_critical_health(zoo, sample_lion, sample_enclosure):
    """Test that assigning animal with critical health issues raises ValueError."""

    # Add animal and enclosure
    zoo.add_animal(sample_lion)
    zoo.add_enclosure(sample_enclosure)

    # Add critical health record to animal
    critical_record = HealthRecord('Severe injury', '2025-11-10', 'critical', 'Immediate care')
    sample_lion.add_health_record(critical_record)

    # Attempting to assign should raise ValueError
    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)


def test_assign_animal_invalid_animal_type(zoo, sample_enclosure):
    """Test that assigning with invalid animal type raises TypeError."""
    # Add enclosure
    zoo.add_enclosure(sample_enclosure)

    # Type error: animal must be Animal instance
    with pytest.raises(TypeError):
        zoo.assign_animal_to_enclosure('not an animal', sample_enclosure)


def test_assign_animal_invalid_enclosure_type(zoo, sample_lion):
    """Test that assigning with invalid enclosure type raises TypeError."""
    # Add animal
    zoo.add_animal(sample_lion)

    # Type error: enclosure must be Enclosure instance
    with pytest.raises(TypeError):
        zoo.assign_animal_to_enclosure(sample_lion, 'not an enclosure')


# ===============================================
#        Reporting and Display Tests
# ===============================================
# Test report generation and filtering methods

# ============================ Generate Report Tests ==============================================
# Test the comprehensive zoo report generation

def test_generate_report_empty_zoo(zoo):
    """Test generating report for empty zoo."""
    report = zoo.generate_report()

    # Check report contains zoo name
    assert 'Taronga Zoo - Zoo Report' in report

    # Check sections indicate empty zoo
    assert 'No animals in the zoo.' in report
    assert 'No enclosures in the zoo.' in report
    assert 'No staff members in the zoo.' in report


def test_generate_report_with_animals(zoo, sample_lion, sample_tiger):
    """Test generating report with animals."""
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    report = zoo.generate_report()

    # Check animals section
    assert 'ANIMALS (2)' in report
    assert 'Simba (Lion)' in report
    assert 'Luna (Tiger)' in report


def test_generate_report_with_enclosures(zoo, sample_enclosure):
    """Test generating report with enclosures."""
    zoo.add_enclosure(sample_enclosure)

    report = zoo.generate_report()

    # Check enclosures section
    assert 'ENCLOSURES (1)' in report
    assert 'Savannah' in report
    assert 'Mammal' in report


def test_generate_report_with_staff(zoo, sample_zookeeper, sample_vet):
    """Test generating report with staff."""
    zoo.add_staff(sample_zookeeper)
    zoo.add_staff(sample_vet)

    report = zoo.generate_report()

    # Check staff section
    assert 'STAFF (2)' in report
    assert 'John' in report
    assert 'Zookeeper' in report
    assert 'Dr. Smith' in report
    assert 'Veterinarian' in report


def test_generate_report_comprehensive(zoo, sample_lion, sample_tiger, sample_enclosure, sample_zookeeper):
    """Test generating comprehensive report with all entities."""
    # Add all entities
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)
    zoo.add_enclosure(sample_enclosure)
    zoo.add_staff(sample_zookeeper)

    # Assign animal and staff
    zoo.assign_animal_to_enclosure(sample_lion, sample_enclosure)
    sample_zookeeper.assign_animal(sample_lion)

    report = zoo.generate_report()

    # Check all sections present
    assert 'ANIMALS (2)' in report
    assert 'ENCLOSURES (1)' in report
    assert 'STAFF (1)' in report
    assert 'Simba' in report
    assert 'Luna' in report
    assert 'Savannah' in report
    assert 'John' in report


def test_generate_report_with_critical_health(zoo, sample_lion):
    """Test that report shows critical health warning."""

    # Add animal
    zoo.add_animal(sample_lion)

    # Add critical health record
    critical_record = HealthRecord('Emergency', '2025-11-10', 'critical', 'Urgent care')
    sample_lion.add_health_record(critical_record)

    report = zoo.generate_report()

    # Check critical health warning appears
    assert 'CRITICAL HEALTH ISSUES' in report


# ============================ List Critical Health Tests =========================================
# Test filtering animals with critical health issues

def test_list_critical_health_empty(zoo):
    """Test listing critical health animals when none exist."""
    critical = zoo.list_animals_with_critical_health()

    # Should return empty list
    assert isinstance(critical, list)
    assert len(critical) == 0


def test_list_critical_health_no_critical(zoo, sample_lion, sample_tiger):
    """Test listing when animals have no critical health issues."""
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    critical = zoo.list_animals_with_critical_health()

    # Should return empty list
    assert len(critical) == 0


def test_list_critical_health_one_critical(zoo, sample_lion, sample_tiger):
    """Test listing when one animal has critical health issues."""
    from health_record import HealthRecord

    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    # Add critical health record to one animal
    critical_record = HealthRecord('Serious injury', '2025-11-10', 'high', 'Treatment needed')
    sample_lion.add_health_record(critical_record)

    critical = zoo.list_animals_with_critical_health()

    # Should return only lion
    assert len(critical) == 1
    assert sample_lion in critical
    assert sample_tiger not in critical


def test_list_critical_health_multiple_critical(zoo, sample_lion, sample_tiger):
    """Test listing when multiple animals have critical health issues."""
    from health_record import HealthRecord

    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    # Add critical health records to both
    record1 = HealthRecord('Injury', '2025-11-10', 'critical', 'Urgent')
    record2 = HealthRecord('Illness', '2025-11-10', 'high', 'Care needed')
    sample_lion.add_health_record(record1)
    sample_tiger.add_health_record(record2)

    critical = zoo.list_animals_with_critical_health()

    # Should return both animals
    assert len(critical) == 2
    assert sample_lion in critical
    assert sample_tiger in critical


# ============================ List Animals By Species Tests ======================================
# Test filtering animals by species

def test_list_by_species_valid(zoo, sample_lion, sample_tiger):
    """Test listing animals by species."""
    zoo.add_animal(sample_lion)
    zoo.add_animal(sample_tiger)

    # List lions
    lions = zoo.list_animals_by_species('Lion')

    # Should return only lion
    assert len(lions) == 1
    assert sample_lion in lions


def test_list_by_species_case_insensitive(zoo, sample_lion):
    """Test that species filtering is case-insensitive."""
    zoo.add_animal(sample_lion)

    # Try different cases
    lions1 = zoo.list_animals_by_species('lion')
    lions2 = zoo.list_animals_by_species('LION')
    lions3 = zoo.list_animals_by_species('LiOn')

    # All should return the same result
    assert len(lions1) == 1
    assert len(lions2) == 1
    assert len(lions3) == 1


def test_list_by_species_multiple(zoo):
    """Test listing when multiple animals of same species exist."""
    lion1 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Golden', 'Warm-blooded')
    lion2 = Mammal('Nala', 'Lion', 4, 'Carnivore', 'Savannah', 'Roar', 'Tan', 'Warm-blooded')
    tiger = Mammal('Luna', 'Tiger', 4, 'Carnivore', 'Savannah', 'Growl', 'Striped', 'Warm-blooded')

    zoo.add_animal(lion1)
    zoo.add_animal(lion2)
    zoo.add_animal(tiger)

    # List lions
    lions = zoo.list_animals_by_species('Lion')

    # Should return both lions
    assert len(lions) == 2
    assert lion1 in lions
    assert lion2 in lions
    assert tiger not in lions


def test_list_by_species_not_found(zoo, sample_lion):
    """Test listing species that doesn't exist."""
    zoo.add_animal(sample_lion)

    # List non-existent species
    elephants = zoo.list_animals_by_species('Elephant')

    # Should return empty list
    assert len(elephants) == 0


def test_list_by_species_empty_zoo(zoo):
    """Test listing species in empty zoo."""
    # List any species
    lions = zoo.list_animals_by_species('Lion')

    # Should return empty list
    assert len(lions) == 0


def test_list_by_species_invalid_type(zoo):
    """Test that invalid species type raises TypeError."""
    # Type error: species must be a string
    with pytest.raises(TypeError):
        zoo.list_animals_by_species(123)

    with pytest.raises(TypeError):
        zoo.list_animals_by_species(None)


def test_list_by_species_empty_string(zoo):
    """Test that empty species string raises ValueError."""
    # Value error: species cannot be empty
    with pytest.raises(ValueError):
        zoo.list_animals_by_species('')

    with pytest.raises(ValueError):
        zoo.list_animals_by_species('   ')


# ============================ String Method Test =================================================
# Test __str__ method

def test_str_method_calls_generate_report(zoo):
    """Test that __str__ returns the same as generate_report."""
    assert str(zoo) == zoo.generate_report()


def test_str_method_with_entities(zoo, sample_lion, sample_enclosure):
    """Test __str__ with zoo entities."""
    zoo.add_animal(sample_lion)
    zoo.add_enclosure(sample_enclosure)

    zoo_str = str(zoo)

    # Should contain same content as report
    assert 'Taronga Zoo - Zoo Report' in zoo_str
    assert 'Simba' in zoo_str
    assert 'Savannah' in zoo_str


