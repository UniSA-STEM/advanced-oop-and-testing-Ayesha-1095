"""
File: test_enclosure.py
Description: Test suite for the Enclosure class.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from enclosure import Enclosure
from animal import Animal, Mammal, Reptile, Bird

# ============================ Fixtures ===============================================================
# Fixtures provide reusable objects for tests, including sample enclosures and animals
@pytest.fixture
def mammal_enclosure():
    """Fixture to create a sample enclosure for Mammals."""
    return Enclosure('Large', 'Savannah', Mammal, 80)

@pytest.fixture
def sample_mammal():
    """Fixture to create a sample Mammal instance."""
    return Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long and blond', 'Warm-blooded')

@pytest.fixture
def sample_bird():
    """Fixture to create a sample Bird instance (for wrong type tests)."""
    return Bird('Tweety', 'Canary', 2, 'Herbivore', 'Forest', 'Chirp', 'Soft and yellow', 'Cold-blooded', True)

# ============================ Constructor & Getters ====================================================
# Test that the enclosure initializes properly and getters return correct values
def test_init(mammal_enclosure):
    """Test if enclosure initializes correctly with given parameters."""
    assert mammal_enclosure.size == 'Large'
    assert mammal_enclosure.environmental_type == 'Savannah'
    assert mammal_enclosure.animal_type == Mammal
    assert mammal_enclosure.cleanliness_level == 80
    assert mammal_enclosure.animals == []

def test_init_default_cleanliness():
    """Test that default cleanliness level is 100%."""
    enclosure = Enclosure('Medium', 'Jungle', Mammal)
    assert enclosure.cleanliness_level == 100

# ============================ Setters (Valid Cases) ====================================================
# Test that setting valid attributes works as expected
def test_set_valid_values(mammal_enclosure):
    """Test updating enclosure attributes with valid values."""
    mammal_enclosure.size = 'Small'
    assert mammal_enclosure.size == 'Small'
    mammal_enclosure.environmental_type = 'Jungle'
    assert mammal_enclosure.environmental_type == 'Jungle'
    mammal_enclosure.animal_type = Mammal
    assert mammal_enclosure.animal_type == Mammal
    mammal_enclosure.cleanliness_level = 96.0
    assert mammal_enclosure.cleanliness_level == 96.0

# ============================ Setters (Edge Cases) ==================================================
# Test that invalid inputs raise appropriate exceptions
def test_set_invalid_values(mammal_enclosure):
    """Test that invalid types or out-of-range values raise errors."""
    # Type errors
    with pytest.raises(TypeError):
        mammal_enclosure.size = 123
    with pytest.raises(TypeError):
        mammal_enclosure.environmental_type = 125
    with pytest.raises(TypeError):
        mammal_enclosure.animal_type = 'Not a Class'
    with pytest.raises(TypeError):
        mammal_enclosure.cleanliness_level = 'Fully Clean'

    # Value errors
    with pytest.raises(ValueError):
        mammal_enclosure.size = ''
    with pytest.raises(ValueError):
        mammal_enclosure.size = '  '
    with pytest.raises(ValueError):
        mammal_enclosure.environmental_type = ''
    with pytest.raises(ValueError):
        mammal_enclosure.environmental_type = '  '
    with pytest.raises(ValueError):
        mammal_enclosure.cleanliness_level = -5
    with pytest.raises(ValueError):
        mammal_enclosure.cleanliness_level = 105

# ============================ Add Animal ===========================================================
# Test adding animals to the enclosure, including edge cases for type, environment, and duplicates
def test_add_animal_valid(mammal_enclosure, sample_mammal):
    """Test adding a valid animal to the enclosure."""
    enclosure = mammal_enclosure.add_animal(sample_mammal)
    assert sample_mammal in mammal_enclosure.animals
    assert 'Simba the Lion has been added to the enclosure.' in enclosure
    assert isinstance(enclosure, str)

def test_add_animal_invalid_type(mammal_enclosure, sample_bird):
    """Test that adding a wrong animal type raises TypeError."""
    with pytest.raises(TypeError):
        # Add wrong subclass
        mammal_enclosure.add_animal(sample_bird)

def test_add_animal_wrong_environment(mammal_enclosure):
    """Test that adding an animal with mismatched environment raises ValueError."""
    wrong_env_mammal = Mammal('Leo', 'Tiger', 3, 'Carnivore', 'Jungle', 'Roar', 'Striped', 'Warm-blooded')
    with pytest.raises(ValueError):
        # Add wrong environment
        mammal_enclosure.add_animal(wrong_env_mammal)

def test_add_duplicate_animal(mammal_enclosure, sample_mammal):
    """Test that adding the same animal twice raises ValueError."""
    mammal_enclosure.add_animal(sample_mammal)
    with pytest.raises(ValueError):
        # Add duplicate
        mammal_enclosure.add_animal(sample_mammal)

def test_add_animal_not_animal_object(mammal_enclosure):
    """Test that adding a non-Animal object raises TypeError."""
    with pytest.raises(TypeError):
        mammal_enclosure.add_animal('not an animal')
    with pytest.raises(TypeError):
        mammal_enclosure.add_animal(123)
    with pytest.raises(TypeError):
        mammal_enclosure.add_animal(None)


# ============================ Remove Animal ========================================================
# Test removing animals from the enclosure and error handling
def test_remove_animal_valid(mammal_enclosure, sample_mammal):
    """Test removing an animal from the enclosure."""
    mammal_enclosure.add_animal(sample_mammal)
    enclosure = mammal_enclosure.remove_animal(sample_mammal)
    assert sample_mammal not in mammal_enclosure.animals
    assert 'Simba the Lion has been removed from the enclosure.' in enclosure
    assert isinstance(enclosure, str)

def test_remove_animal_not_present(mammal_enclosure, sample_mammal):
    """Test that removing an animal not in the enclosure raises ValueError."""
    with pytest.raises(ValueError):
        mammal_enclosure.remove_animal(sample_mammal)

def test_remove_animal_invalid_type(mammal_enclosure):
    """Test that removing a non-Animal object raises TypeError."""
    with pytest.raises(TypeError):
        mammal_enclosure.remove_animal(None)

# ============================ Clean Enclosure ======================================================
# Test the clean_enclosure method including already-clean edge case
def test_clean_enclosure(mammal_enclosure):
    """Test that cleaning the enclosure resets cleanliness level to 100."""
    mammal_enclosure.cleanliness_level = 55
    enclosure = mammal_enclosure.clean_enclosure()
    assert mammal_enclosure.cleanliness_level == 100
    assert 'Enclosure cleaned. Cleanliness restored from 55% to 100%'in enclosure

def test_clean_enclosure_already_clean(mammal_enclosure):
    """Test cleaning an enclosure that is already at 100% cleanliness."""
    mammal_enclosure.cleanliness_level = 100
    result = mammal_enclosure.clean_enclosure()
    assert mammal_enclosure.cleanliness_level == 100
    assert 'The enclosure is already 100% clean.' in result

# ============================ Degrade Cleanliness ========================================================
# Test the degrade_cleanliness method including normal cases and edge cases

def test_degrade_cleanliness(mammal_enclosure):
    """Test that degrading cleanliness reduces the level correctly."""
    mammal_enclosure.cleanliness_level = 100
    result = mammal_enclosure.degrade_cleanliness(15)
    assert mammal_enclosure.cleanliness_level == 85
    assert 'Cleanliness degraded from 100% to 85%' in result

def test_degrade_cleanliness_below_zero(mammal_enclosure):
    """Test that cleanliness cannot go below 0%."""
    mammal_enclosure.cleanliness_level = 10
    result = mammal_enclosure.degrade_cleanliness(25)
    assert mammal_enclosure.cleanliness_level == 0
    assert 'Cleanliness degraded from 10% to 0%' in result

def test_degrade_cleanliness_already_at_zero(mammal_enclosure):
    """Test degrading when cleanliness is already at 0%."""
    mammal_enclosure.cleanliness_level = 0
    result = mammal_enclosure.degrade_cleanliness(10)
    assert mammal_enclosure.cleanliness_level == 0
    assert 'already at 0% cleanliness' in result

def test_degrade_cleanliness_invalid_type(mammal_enclosure):
    """Test that invalid type raises TypeError."""
    with pytest.raises(TypeError):
        mammal_enclosure.degrade_cleanliness('lots')

def test_degrade_cleanliness_invalid_value(mammal_enclosure):
    """Test that invalid value raises ValueError."""
    with pytest.raises(ValueError):
        mammal_enclosure.degrade_cleanliness(-10)
    with pytest.raises(ValueError):
        mammal_enclosure.degrade_cleanliness(150)

def test_degrade_cleanliness_default_parameter(mammal_enclosure):
    """Test degradation with default amount (10%)."""
    mammal_enclosure.cleanliness_level = 50
    result = mammal_enclosure.degrade_cleanliness()
    assert mammal_enclosure.cleanliness_level == 40
    assert 'Cleanliness degraded from 50% to 40%' in result

def test_degrade_cleanliness_exact_zero(mammal_enclosure):
    """Test degradation that reaches exactly 0%."""
    mammal_enclosure.cleanliness_level = 20
    result = mammal_enclosure.degrade_cleanliness(20)
    assert mammal_enclosure.cleanliness_level == 0
    assert 'Cleanliness degraded from 20% to 0%' in result

# ============================ Report Status ========================================================
# Test that report_status returns accurate details of the enclosure
def test_report_status_empty(mammal_enclosure):
    """Test status report when enclosure has no animals."""
    report = mammal_enclosure.report_status()
    assert 'No animals currently in this enclosure.' in report

def test_report_status_with_animals(mammal_enclosure, sample_mammal):
    """Test status report when enclosure has animals."""
    mammal_enclosure.add_animal(sample_mammal)
    report = mammal_enclosure.report_status()
    st = str(report)
    assert 'Enclosure type: Mammal' in st
    assert 'Environment: Savannah' in st
    assert 'Size: Large' in st
    assert 'Cleanliness level: 80' in st
    assert 'Number of animals: 1' in st
    assert 'List of animals: Simba' in st
    assert isinstance(report, str)

def test_multiple_animals_in_enclosure(mammal_enclosure):
    """Test adding multiple animals and checking report status."""
    m1 = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah', 'Roar', 'Long and blond', 'Warm-blooded')
    m2 = Mammal('Nala', 'Lion', 4, 'Carnivore', 'Savannah', 'Roar', 'Short and tan', 'Warm-blooded')
    mammal_enclosure.add_animal(m1)
    mammal_enclosure.add_animal(m2)
    report = mammal_enclosure.report_status()
    assert 'Number of animals: 2' in report
    assert 'List of animals: Simba, Nala' in report

# ============================ String Representation ================================================
# Test that __str__ returns the same as report_status for printing purposes
def test_str_method(mammal_enclosure, sample_mammal):
    """Test that __str__ returns the same output as report_status."""
    mammal_enclosure.add_animal(sample_mammal)
    assert str(mammal_enclosure) == mammal_enclosure.report_status()

def test_str_empty_enclosure(mammal_enclosure):
    """Ensure __str__ output is correct when no animals are present."""
    st = str(mammal_enclosure)
    assert 'No animals currently in this enclosure.' in st
    assert 'Number of animals: 0' in st