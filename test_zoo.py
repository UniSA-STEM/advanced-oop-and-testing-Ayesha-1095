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