import pytest
from animal import Animal, Mammal, Reptile, Bird

# ==== Fixtures ====
@pytest.fixture
def lion():
    """Fixture to create a default Mammal instance for testing."""
    return Mammal('Simba','Lion', 5, 'Carnivore', 'Roar', 'Long and thick', 'Warm-blooded')

# ==== Inheritance and Abstract Tests ====
def test_mammal_inheritance(lion):
    """Verify that Mammal is an instance of Animal and Animal cannot be instantiated directly."""
    # Mammal is instance of Animal
    assert isinstance(lion, Animal)
    # Cannot instantiate abstract class directly
    with pytest.raises(TypeError):
        Animal('Simba', 'Lion', 5, 'Carnivore')

# ==== Method Tests ====
def test_mammal_methods(lion):
    """Test that eat, sleep, and make_sound return correct behavior strings."""
    assert lion.eat() == 'Simba the Lion is eating Carnivore.'
    assert lion.sleep() == 'Simba the Lion is sleeping.'
    assert lion.make_sound() == 'Simba Roar!'

# ==== Property Tests ====
def test_mammal_properties(lion):
    """Test getters and valid setters for Mammal properties."""
    # Testing getters
    assert lion.name == 'Simba'
    assert lion.species == 'Lion'
    assert lion.age == 5
    assert lion.dietary_needs == 'Carnivore'
    assert lion.blood_type == 'Warm-blooded'
    assert lion.sound == 'Roar'

    # Testing valid setters
    lion.name = 'Leo'
    assert lion.name == 'Leo'
    lion.age = 6
    assert lion.age == 6
    lion.dietary_needs = 'Meat'
    assert lion.dietary_needs == 'Meat'
    lion.sound = 'Meow'
    assert lion.sound == 'Meow'
    lion.hair_type = 'Short'
    assert lion.hair_type == 'Short'

# ==== Edge Case Tests ====
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
        lion.sound = 2
    with pytest.raises(TypeError):
        lion.hair_type = 123

    # Value errors / invalid values
    with pytest.raises(ValueError):
        lion.age = -2
    with pytest.raises(ValueError):
        lion.name = ''              # Empty string not allowed
    with pytest.raises(ValueError):
        lion.name = '    '          # Whitespace only
    with pytest.raises(ValueError):
        lion.species = ''
    with pytest.raises(ValueError):
        lion.species = '   '
    with pytest.raises(ValueError):
        lion.dietary_needs = ''
    with pytest.raises(ValueError):
        lion.dietary_needs = '   '
    with pytest.raises(ValueError):
        lion.sound = ''
    with pytest.raises(ValueError):
        lion.sound = '   '
    with pytest.raises(ValueError):
        lion.hair_type = ''
    with pytest.raises(ValueError):
        lion.hair_type = '   '

# ==== Health Record Tests ====
def test_mammal_health_records(lion):
    """Test adding and displaying health records for a Mammal."""
    # Empty initially
    assert lion.display_health_records() == 'Simba has no health records.'
    # Add records
    lion.add_health_record('Vaccinated')
    lion.add_health_record('Checkup complete')
    records = lion.display_health_records()
    assert 'Vaccinated' in records
    assert 'Checkup complete' in records

def test_mammal_health_record_type(lion):
    """Ensure display_health_records returns a list after adding a record."""
    lion.add_health_record('X-ray done')
    result = lion.display_health_records()
    assert isinstance(result, list)
    assert len(result) == 1

# ==== String Method Test ====
def test_mammal_str(lion):
    """Test that __str__ returns a properly formatted string with all Mammal details."""
    st = str(lion)
    assert 'Name: Simba' in st
    assert 'Species: Lion' in st
    assert 'Age: 5' in st
    assert 'Dietary needs: Carnivore' in st
    assert 'Sound: Roar' in st
    assert 'Hair type: Long and thick' in st
    assert 'Blood type: Warm-blooded' in st

# ==== Equality Tests ====
def test_mammal_equality():
    """Test __eq__ method for comparing two Mammals and differences in attributes."""
    lion1 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Roar', 'Long and thick', 'Warm-blooded')
    lion2 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Roar', 'Long and thick', 'Warm-blooded')
    lion3 = Mammal('Leo', 'Lion', 4, 'Carnivore', 'Roar', 'Short', 'Warm-blooded')
    assert lion1 == lion2
    assert lion1 != lion3

def test_mammal_equality_with_different_type(lion):
    """Test that __eq__ returns False when comparing with non-Mammal object."""
    assert lion != 'not a mammal'