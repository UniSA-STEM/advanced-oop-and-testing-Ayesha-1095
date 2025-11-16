"""
File: main.py
Description: Demonstration script for the Zoo Management System.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""

# ============================ IMPORTS =============================================================
from zoo import Zoo
from animal import Mammal, Reptile, Bird
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord

# ============================ HELPER FUNCTION =====================================================
def print_section(title):
    """Helper function for printing section title."""
    print()
    print('=' * 70)
    print(title.center(70))
    print('=' * 70)

# ============================ STEP 1: ANIMAL CREATION =============================================
def demonstrate_animal_creation():
    """Creates and returns sample animals (Mammal, Bird, Reptile)."""
    print_section('STEP 1: Creating Animals (Inheritance)')

    # Create Mammals
    print('\n--- Creating Mammals ---')
    simba = Mammal('Simba', 'Lion', 5, 'Carnivore', 'Savannah',
                   'Roar', 'Golden mane', 'Warm-blooded')
    luna = Mammal('Luna', 'Tiger', 4, 'Carnivore', 'Savannah',
                  'Growl', 'Striped', 'Warm-blooded')
    print(f'* Created Mammal: {simba.name} the {simba.species}')
    print(f'* Created Mammal: {luna.name} the {luna.species}')

    # Create Birds
    print('\n--- Creating Birds ---')
    polly = Bird('Polly', 'Parrot', 2, 'Seeds', 'Tropical',
                 'Squawk', 'Colorful feathers', 'Warm-blooded', True)
    kiwi = Bird('Kiwi', 'Kiwi', 3, 'Insects', 'Forest',
                'Chirp', 'Brown feathers', 'Warm-blooded', False)
    print(f'* Created Bird: {polly.name} the {polly.species} (Can fly: {polly.can_fly})')
    print(f'* Created Bird: {kiwi.name} the {kiwi.species} (Can fly: {kiwi.can_fly})')

    # Create Reptiles
    print('\n--- Creating Reptiles ---')
    steve = Reptile('Steve', 'Crocodile', 10, 'Carnivore', 'Aquatic',
                    'Hiss', 'Scaly skin', 'Cold-blooded', False)
    monty = Reptile('Monty', 'Python', 6, 'Carnivore', 'Jungle',
                    'Hiss', 'Smooth scales', 'Cold-blooded', False)
    print(f'* Created Reptile: {steve.name} the {steve.species} (Venomous: {steve.is_venomous})')
    print(f'* Created Reptile: {monty.name} the {monty.species} (Venomous: {monty.is_venomous})')

    # Put all animals in a list and return it
    all_animals = [simba, luna, polly, kiwi, steve, monty]
    return all_animals

# ============================ STEP 2: POLYMORPHISM =================================================
def demonstrate_polymorphism(animals_list):
    """Demonstrates polymorphic behavior of animals."""
    print_section('STEP 2: Demonstrating Polymorphism')

    print('\n--- All animals can perform common behaviors ---')

    # Show eating behavior
    print('\nEating behavior:')
    for animal in animals_list:
        print(f'  {animal.eat()}')

    # Show sleeping behavior
    print('\nSleeping behavior:')
    for animal in animals_list:
        print(f'  {animal.sleep()}')

    # Show sound behavior
    print('\nSound behavior:')
    for animal in animals_list:
        print(f'  {animal.make_sound()}')

# ============================ STEP 3: CREATE ENCLOSURES ============================================
def create_enclosures():
    """Creates and returns sample enclosures."""
    print_section('STEP 3: Creating Enclosures')

    # Create different enclosures
    savannah_enclosure = Enclosure('Large', 'Savannah', Mammal, 85)
    tropical_enclosure = Enclosure('Medium', 'Tropical', Bird, 90)
    forest_enclosure = Enclosure('Small', 'Forest', Bird, 88)
    aquatic_enclosure = Enclosure('Large', 'Aquatic', Reptile, 92)
    jungle_enclosure = Enclosure('Medium', 'Jungle', Reptile, 87)

    print('* Created Savannah enclosure for Mammals')
    print('* Created Tropical enclosure for Birds')
    print('* Created Forest enclosure for Birds')
    print('* Created Aquatic enclosure for Reptiles')
    print('* Created Jungle enclosure for Reptiles')

    # Put all enclosures in a list and return
    all_enclosures = [savannah_enclosure, tropical_enclosure, forest_enclosure,
                      aquatic_enclosure, jungle_enclosure]
    return all_enclosures

# ============================ STEP 4: CREATE STAFF ================================================
def create_staff():
    """Creates and returns sample staff members."""
    print_section('STEP 4: Creating Staff')

    # Create Zookeepers
    print('\n--- Creating Zookeepers ---')
    john = Zookeeper('John Smith', 101)
    sarah = Zookeeper('Sarah Johnson', 102)
    print(f'* Created: {john.name} ({john.role})')
    print(f'* Created: {sarah.name} ({sarah.role})')

    # Create Veterinarians
    print('\n--- Creating Veterinarians ---')
    dr_smith = Veterinarian('Dr. Emily Smith', 201)
    dr_jones = Veterinarian('Dr. Michael Jones', 202)
    print(f'* Created: {dr_smith.name} ({dr_smith.role})')
    print(f'* Created: {dr_jones.name} ({dr_jones.role})')

    # Return list of all staff
    all_staff = [john, sarah, dr_smith, dr_jones]
    return all_staff

# ============================ STEP 5: ADD ENTITIES TO ZOO ========================================
def demonstrate_zoo_operations(zoo, animals, enclosures, staff_list):
    """Demonstrates adding entities to zoo and assignments."""
    print_section('STEP 5: Adding Entities to Zoo')

    # Add all animals to zoo
    print('\n--- Adding animals to zoo ---')
    for animal in animals:
        result = zoo.add_animal(animal)
        print(result)
    print(f'\n* Total animals in zoo: {len(zoo.animals)}')

    # Add all enclosures to zoo
    print('\n--- Adding enclosures to zoo ---')
    for enclosure in enclosures:
        result = zoo.add_enclosure(enclosure)
        print(result)
    print(f'\n* Total enclosures in zoo: {len(zoo.enclosures)}')

    # Add all staff to zoo
    print('\n--- Adding staff to zoo ---')
    for staff_member in staff_list:
        result = zoo.add_staff(staff_member)
        print(result)
    print(f'\n* Total staff in zoo: {len(zoo.staff)}')

# ============================ STEP 6: ASSIGN ANIMALS TO ENCLOSURES ===============================
def demonstrate_animal_enclosure_assignment(zoo, animals, enclosures):
    """Assigns animals to appropriate enclosures with validation."""
    print_section('STEP 6: Assigning Animals to Enclosures')

    print('\n--- Assigning animals to matching enclosures ---')

    # Assign each animal to correct enclosure
    # animals[0] is Simba, enclosures[0] is Savannah
    result = zoo.assign_animal_to_enclosure(animals[0], enclosures[0])
    print(result)

    # animals[1] is Luna, enclosures[0] is Savannah
    result = zoo.assign_animal_to_enclosure(animals[1], enclosures[0])
    print(result)

    # animals[2] is Polly, enclosures[1] is Tropical
    result = zoo.assign_animal_to_enclosure(animals[2], enclosures[1])
    print(result)

    # animals[3] is Kiwi, enclosures[2] is Forest
    result = zoo.assign_animal_to_enclosure(animals[3], enclosures[2])
    print(result)

    # animals[4] is Steve, enclosures[3] is Aquatic
    result = zoo.assign_animal_to_enclosure(animals[4], enclosures[3])
    print(result)

    # animals[5] is Monty, enclosures[4] is Jungle
    result = zoo.assign_animal_to_enclosure(animals[5], enclosures[4])
    print(result)

    # Demonstrate validation - try wrong assignment
    print('\n--- Attempting invalid assignment (Bird to Mammal enclosure) ---')
    try:
        zoo.assign_animal_to_enclosure(animals[2], enclosures[0])  # Polly to Savannah
    except TypeError as e:
        print(f'x Error: {e}')

# ============================ STEP 7: STAFF OPERATIONS =======================================================
def demonstrate_staff_operations(zookeeper, veterinarian, animals, enclosures):
    """Shows staff performing their duties."""
    print_section('STEP 7: Staff Operations')

    # Assign responsibilities to zookeeper
    print('\n--- Assigning animals to Zookeeper ---')
    print(zookeeper.assign_animal(animals[0]))  # Simba
    print(zookeeper.assign_animal(animals[1]))  # Luna
    print(zookeeper.assign_animal(animals[2]))  # Polly

    print('\n--- Assigning enclosures to Zookeeper ---')
    print(zookeeper.assign_enclosure(enclosures[0]))  # Savannah
    print(zookeeper.assign_enclosure(enclosures[1]))  # Tropical

    # Assign animals to veterinarian
    print('\n--- Assigning animals to Veterinarian ---')
    print(veterinarian.assign_animal(animals[0]))  # Simba
    print(veterinarian.assign_animal(animals[1]))  # Luna
    print(veterinarian.assign_animal(animals[4]))  # Steve

    # Zookeeper performs duties
    print('\n--- Zookeeper feeding animals ---')
    print(zookeeper.feed_animal(animals[0]))
    print(zookeeper.feed_animal(animals[1]))
    print(zookeeper.feed_animal(animals[2]))

    print('\n--- Zookeeper cleaning enclosures ---')
    print(zookeeper.clean_enclosure(enclosures[0]))
    print(zookeeper.clean_enclosure(enclosures[1]))

    # Veterinarian performs duties
    print('\n--- Veterinarian conducting health checks ---')
    print(veterinarian.conduct_health_check(animals[0]))
    print(veterinarian.conduct_health_check(animals[1]))
    print(veterinarian.conduct_health_check(animals[4]))

# ============================ STEP 8: HEALTH RECORD MANAGEMENT =======================================================
def demonstrate_health_records(veterinarian, animals):
    """Creates and manages health records."""
    print_section('STEP 8: Health Record Management')

    # Create health records
    print('\n--- Creating health records ---')
    record1 = HealthRecord('Routine checkup', '2025-11-10', 'low', 'All clear, healthy')
    record2 = HealthRecord('Dental cleaning', '2025-11-11', 'medium', 'Follow-up in 6 months')
    record3 = HealthRecord('Injured paw', '2025-11-12', 'high', 'Rest for 2 weeks')

    print(f'* Created record: {record1.summary()}')
    print(f'* Created record: {record2.summary()}')
    print(f'* Created record: {record3.summary()}')

    # Veterinarian adds records to animals
    print('\n--- Adding health records to animals ---')
    print(veterinarian.update_health_record(animals[0], record1))  # Simba
    print(veterinarian.update_health_record(animals[1], record2))  # Luna
    print(veterinarian.update_health_record(animals[4], record3))  # Steve

    # Display health records for each animal
    print('\n--- Displaying health records ---')

    print(f"\nSimba's health records:")
    for record in animals[0].display_health_records():
        print(f'  {record.summary()}')

    print(f"\nLuna's health records:")
    for record in animals[1].display_health_records():
        print(f'  {record.summary()}')

    print(f"\nSteve's health records:")
    for record in animals[4].display_health_records():
        print(f'  {record.summary()}')

# ============================ STEP 9: CRITICAL HEALTH RESTRICTIONS =======================================================
def demonstrate_critical_health_restrictions(zoo, animal):
    """Shows how critical health prevents moving animals."""
    print_section('STEP 9: Critical Health Restrictions')

    # Add critical health record
    print('\n--- Adding critical health issue to Simba ---')
    critical_record = HealthRecord('Severe infection', '2025-11-13',
                                   'critical', 'Immediate surgery required')
    animal.add_health_record(critical_record)
    print(f'* Added critical record: {critical_record.summary()}')

    # Check if animal can be moved
    print('\n--- Checking if Simba can be moved ---')
    if animal.can_be_moved():
        print('* Simba can be moved safely')
    else:
        print('x Simba CANNOT be moved due to critical health issues')

    # Try to move animal with critical health
    print('\n--- Attempting to move Simba ---')
    try:
        new_enclosure = Enclosure('Large', 'Savannah', Mammal, 100)
        zoo.add_enclosure(new_enclosure)
        zoo.assign_animal_to_enclosure(animal, new_enclosure)
    except ValueError as e:
        print(f'x Error: {e}')

# ============================ STEP 10: ENCLOSURE MAINTENANCE =======================================================
def demonstrate_enclosure_maintenance(zookeeper, enclosure):
    """Shows enclosure cleaning and cleanliness degradation."""
    print_section('STEP 10: Enclosure Maintenance')

    # Show current cleanliness
    print('\n--- Checking enclosure cleanliness ---')
    print(f'Savannah enclosure cleanliness: {enclosure.cleanliness_level}%')

    # Degrade cleanliness (simulate daily use)
    print('\n--- Degrading cleanliness (simulating daily use) ---')
    result = enclosure.degrade_cleanliness(15)
    print(result)

    # Clean enclosure
    print('\n--- Cleaning enclosure ---')
    result = zookeeper.clean_enclosure(enclosure)
    print(result)
    print(f'Cleanliness after cleaning: {enclosure.cleanliness_level}%')

# ============================ STEP 11: DAILY STAFF DUTIES =======================================================
def demonstrate_staff_duties_summary(zookeeper, veterinarian):
    """Shows daily duties summary for staff."""
    print_section('STEP 11: Daily Staff Duties Summary')

    # Zookeeper duties
    print('\n--- John (Zookeeper) Daily Duties ---')
    print(zookeeper.perform_duties())

    # Veterinarian duties
    print('\n--- Dr. Smith (Veterinarian) Daily Duties ---')
    print(veterinarian.perform_duties())

# ============================ STEP 12: ZOO REPORTING =======================================================
def demonstrate_zoo_reporting(zoo):
    """Demonstrates search and reporting features."""
    print_section('STEP 12: Zoo Reporting Features')

    # Find animal by name
    print('\n--- Finding specific animals ---')
    found_animal = zoo.find_animal_by_name('Luna')
    print(f'* Found: {found_animal.name} the {found_animal.species}')

    # List animals by species
    print('\n--- Listing animals by species ---')
    lions = zoo.list_animals_by_species('Lion')
    print(f'Lions in zoo: {len(lions)}')
    for animal in lions:
        print(f'  - {animal.name}')

    # List animals with critical health
    print('\n--- Checking for critical health issues ---')
    critical_animals = zoo.list_animals_with_critical_health()
    print(f'Animals with critical health: {len(critical_animals)}')
    for animal in critical_animals:
        print(f'  - {animal.name} the {animal.species}')

# ============================ STEP 13: ZOO REPORT =======================================================
def demonstrate_comprehensive_report(zoo):
    """Generates and displays full zoo report."""
    print_section('STEP 13: Comprehensive Zoo Report')

    # Generate and print full report
    report = zoo.generate_report()
    print(report)

# ============================ STEP 14: DATA VALIDATION =======================================================
def demonstrate_validation():
    """Shows data validation preventing invalid inputs."""
    print_section('STEP 14: Data Validation Examples')

    # Try invalid animal
    print('\n--- Attempting invalid animal creation ---')
    try:
        invalid_animal = Mammal('', 'Lion', -5, 'Carnivore', 'Savannah',
                                'Roar', 'Golden', 'Warm-blooded')
    except (TypeError, ValueError) as e:
        print(f'✗ Error: {e}')

    # Try invalid enclosure
    print('\n--- Attempting invalid enclosure ---')
    try:
        invalid_enclosure = Enclosure('', 'Savannah', Mammal, 150)
    except (TypeError, ValueError) as e:
        print(f'✗ Error: {e}')

    # Try invalid health record
    print('\n--- Attempting invalid health record ---')
    try:
        invalid_record = HealthRecord('Issue', '2025-11-10',
                                      'super critical', 'Treatment')
    except ValueError as e:
        print(f'✗ Error: {e}')


def print_final_statistics(zoo):
    """Prints final zoo statistics."""
    print_section('DEMONSTRATION COMPLETE')

    # Print key features
    print('\nFeatures demonstrated:')
    print('  * Inheritance (Animal and Staff hierarchies)')
    print('  * Polymorphism (eat, sleep, make_sound, perform_duties)')
    print('  * Encapsulation (private attributes, properties)')
    print('  * Abstraction (Abstract base classes)')
    print('  * Data validation (Type and value checking)')
    print('  * Health record management')
    print('  * Staff operations')
    print('  * Reporting')

    # Print final statistics
    print(f'\nFinal Zoo Statistics:')
    print(f'  Animals: {len(zoo.animals)}')
    print(f'  Enclosures: {len(zoo.enclosures)}')
    print(f'  Staff: {len(zoo.staff)}')
    print(f'  Animals with critical health: {len(zoo.list_animals_with_critical_health())}')

    print('\n' + '=' * 70)
    print('Thank you for using the Zoo Management System!')
    print('=' * 70)

# ============================ MAIN FUNCTION =======================================================
def main():
    """The main function that runs all the demonstrations."""

    # Welcome message
    print_section('WELCOME TO THE ZOO MANAGEMENT SYSTEM')

    # Create zoo
    print_section('Creating the Zoo')
    taronga_zoo = Zoo('Taronga Zoo')
    print(f'* Created: {taronga_zoo.name}')
    print(f'  Initial animals: {len(taronga_zoo.animals)}')
    print(f'  Initial enclosures: {len(taronga_zoo.enclosures)}')
    print(f'  Initial staff: {len(taronga_zoo.staff)}')

    # Create animals and demonstrate polymorphism
    animals = demonstrate_animal_creation()
    demonstrate_polymorphism(animals)

    # Create enclosures
    enclosures = create_enclosures()

    # Create staff
    staff_list = create_staff()
    john = staff_list[0]  # First zookeeper
    dr_smith = staff_list[2]  # First veterinarian

    # Add everything to zoo
    demonstrate_zoo_operations(taronga_zoo, animals, enclosures, staff_list)

    # Assign animals to enclosures
    demonstrate_animal_enclosure_assignment(taronga_zoo, animals, enclosures)

    # Staff operations
    demonstrate_staff_operations(john, dr_smith, animals, enclosures)

    # Health records
    demonstrate_health_records(dr_smith, animals)

    # Critical health restrictions
    demonstrate_critical_health_restrictions(taronga_zoo, animals[0])

    # Enclosure maintenance
    demonstrate_enclosure_maintenance(john, enclosures[0])

    # Staff duties summary
    demonstrate_staff_duties_summary(john, dr_smith)

    # Zoo reporting
    demonstrate_zoo_reporting(taronga_zoo)

    # Comprehensive report
    demonstrate_comprehensive_report(taronga_zoo)

    # Validation examples
    demonstrate_validation()

    # Final statistics
    print_final_statistics(taronga_zoo)

# ============================ RUN MAIN =============================================================
# Run main when file is executed
if __name__ == '__main__':
    main()