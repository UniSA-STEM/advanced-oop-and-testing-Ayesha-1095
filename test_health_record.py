"""
File: test_health_record.py
Description: Test suite for the HealthRecord class.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from health_record import HealthRecord

# ===============================================
#        HealthRecord Tests
# ===============================================
# Test the HealthRecord class including initialization, properties, validation,
# methods, string representation, and equality checks.

# ============================ Fixtures ===============================================================
@pytest.fixture
def sample_record():
    """Fixture to create a default HealthRecord instance for testing."""
    return HealthRecord('Broken leg', '2025-11-10', 'high', 'Apply cast for 6 weeks')

# ============================ Initialization & Properties ============================================
# Test that the health record initializes properly and properties work correctly
def test_initialization_and_getters(sample_record):
    """Test if HealthRecord initializes correctly with given parameters."""
    assert sample_record.issue == 'Broken leg'
    assert sample_record.date_reported == '2025-11-10'
    assert sample_record.severity_level == 'high'
    assert sample_record.treatment_plan == 'Apply cast for 6 weeks'

def test_setters(sample_record):
    """Test that all setters work correctly with valid values."""
    # Test issue setter
    sample_record.issue = 'Fever'
    assert sample_record.issue == 'Fever'

    # Test date setter
    sample_record.date_reported = '2025-11-08'
    assert sample_record.date_reported == '2025-11-08'

    # Test severity level setter
    sample_record.severity_level = 'Medium'
    assert sample_record.severity_level == 'Medium'

    # Test treatment plan setter
    sample_record.treatment_plan = 'Give pain killer (3x in a day)'
    assert sample_record.treatment_plan == 'Give pain killer (3x in a day)'

# ============================ Validation Tests =======================================================
# Test that invalid inputs raise appropriate exceptions
def test_issue_validation(sample_record):
    """Test that invalid issue values raise TypeError or ValueError."""
    # Type error: issue must be a string
    with pytest.raises(TypeError):
        sample_record.issue = 123

    # Value error: issue cannot be empty or whitespace
    with pytest.raises(ValueError):
        sample_record.issue = '   '

def test_date_validation(sample_record):
    """Test that invalid date values raise TypeError or ValueError."""
    # Type error: date must be a string
    with pytest.raises(TypeError):
        sample_record.date_reported = 20251109

    # Value error: date cannot be empty
    with pytest.raises(ValueError):
        sample_record.date_reported = ''

def test_severity_validation(sample_record):
    """Test that invalid severity level values raise TypeError or ValueError."""
    # Type error: severity level must be a string
    with pytest.raises(TypeError):
        sample_record.severity_level = 5

    # Value error: severity level cannot be empty or whitespace
    with pytest.raises(ValueError):
        sample_record.severity_level = '   '

    # Value error: severity level must be one of valid levels
    with pytest.raises(ValueError):
        sample_record.severity_level = 'extreme'  # Not in valid levels

def test_treatment_validation(sample_record):
    """Test that invalid treatment plan values raise TypeError or ValueError."""
    # Type error: treatment plan must be a string
    with pytest.raises(TypeError):
        sample_record.treatment_plan = 123

    # Value error: treatment plan cannot be empty or whitespace
    with pytest.raises(ValueError):
        sample_record.treatment_plan = ' '

# ============================ Method Tests ===========================================================
# Test the behavior of HealthRecord methods
def test_update_treatment(sample_record):
    """Test that update_treatment() correctly updates the treatment plan."""
    # Test valid update
    msg = sample_record.update_treatment('Rest and medication')
    assert msg == 'Treatment plan updated: Rest and medication'
    assert sample_record.treatment_plan == 'Rest and medication'

    # Test invalid type
    with pytest.raises(TypeError):
        sample_record.update_treatment(123)

    # Test empty value
    with pytest.raises(ValueError):
        sample_record.update_treatment('  ')

def test_update_severity(sample_record):
    """Test that update_severity() correctly updates the severity level."""
    # Test valid update
    msg = sample_record.update_severity('critical')
    assert msg == 'Severity level updated: critical'
    assert sample_record.severity_level == 'critical'

    # Test invalid type
    with pytest.raises(TypeError):
        sample_record.update_severity(123)

    # Test empty value
    with pytest.raises(ValueError):
        sample_record.update_severity('  ')

    # Test invalid severity level
    with pytest.raises(ValueError):
        sample_record.update_severity('lowish')  # Not valid

def test_summary(sample_record):
    """Test that summary() returns a concise one-line summary."""
    summary = sample_record.summary()
    assert summary == 'Broken leg (high) reported on 2025-11-10'

def test_is_critical(sample_record):
    """Test that is_critical() correctly identifies high and critical severity levels."""
    # High severity should be critical
    assert sample_record.is_critical() is True

    # Medium severity should not be critical
    sample_record.severity_level = 'medium'
    assert sample_record.is_critical() is False

    # Low severity should not be critical
    sample_record.severity_level = 'low'
    assert sample_record.is_critical() is False

# ============================ String Method Test =====================================================
# Test that __str__ returns a properly formatted string
def test_str_method(sample_record):
    """Test that __str__ returns a properly formatted multi-line string."""
    st = str(sample_record)
    expected = ('Health Issue: Broken leg\n'
                'Severity: high\n'
                'Date: 2025-11-10\n'
                'Treatment: Apply cast for 6 weeks\n')
    assert st == expected

# ============================ Equality Test ==========================================================
# Test that __eq__ correctly compares HealthRecord objects
def test_eq_method(sample_record):
    """Test __eq__ method for comparing two HealthRecord objects."""
    # Same issue, date, and severity (treatment differs) - should be equal
    same_record = HealthRecord(
        issue='Broken leg',
        date_reported='2025-11-10',
        severity_level='high',
        treatment_plan='Some other treatment'
    )

    # Different issue, should not be equal
    diff_record = HealthRecord(
        issue='Fever',
        date_reported='2025-11-09',
        severity_level='high',
        treatment_plan='Rest'
    )
    # Test equality
    assert sample_record == same_record
    assert sample_record != diff_record

    # Test comparison with non-HealthRecord object
    assert sample_record != 'Not a record'