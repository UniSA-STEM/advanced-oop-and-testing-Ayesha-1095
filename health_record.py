"""
File: health_record.py
Description:This module defines the HealthRecord class for tracking an animal's health details.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Integrity Policy.
"""
class HealthRecord:
    """
    The health record class stores information about a specific health issue
    or treatment for an animal.
     Attributes:
        __issue (str): Description of the health issue.
        __date_reported (str): Date the issue was reported.
        __severity_level (str): Severity level of the issue (e.g., Low, Medium, High, Critical).
        __treatment_plan (str): Treatment plan or notes for the issue.
    """
    # Class level constant
    VALID_SEVERITY_LEVELS = ('low', 'medium', 'high', 'critical')

# ============================== Constructor ============================================================================
    def __init__(self, issue: str, date_reported: str, severity_level: str, treatment_plan: str) -> None:
        """
        Initialize a HealthRecord instance.

        Args:
            issue (str): Description of the health issue.
            date_reported (str): Date the issue was reported.
            severity_level (str): Severity level of the issue.
            treatment_plan (str): Treatment plan for the issue.
        """
        # Use property setters for validation
        self.issue = issue
        self.date_reported = date_reported
        self.severity_level = severity_level
        self.treatment_plan = treatment_plan

# ========================= Getters ========================================================
    def get_issue(self) -> str:
        """Return the health issue description."""
        return self.__issue

    def get_date_reported(self) -> str:
        """Return the date the issue was reported."""
        return self.__date_reported

    def get_severity_level(self) -> str:
        """Return the severity level."""
        return self.__severity_level

    def get_treatment_plan(self) -> str:
        """Return the current treatment plan."""
        return self.__treatment_plan

# ========================= Setters =======================================================
    def set_issue(self, issue: str) -> None:
        """
         Set a new issue description for the health record.

        Args:
            issue (str): New description to set.

        Raises:
            TypeError: If issue is not a string.
            ValueError: If issue is empty.
        """
        # Validate and set a new description
        if not isinstance(issue, str):
            raise TypeError('Issue must be a string.')
        if issue.strip() == '':
            raise ValueError('Issue should not be empty.')
        self.__issue = issue

    def set_date_reported(self, date_reported: str) -> None:
        """
        Set a new date for when the health issue was reported.

        Args:
            date_reported (str): New date to set.

        Raises:
            TypeError: If date_reported is not a string.
            ValueError: If date_reported is empty.
        """
        # Validate and set a new date
        if not isinstance(date_reported, str):
            raise TypeError('Date must be a string.')
        if date_reported.strip() == '':
            raise ValueError('Date should not be empty.')
        self.__date_reported = date_reported

    def set_severity_level(self, severity_level: str) -> None:
        """
        Set a new severity level for the health issue.

        Args:
            severity_level (str): New severity level to set.

        Raises:
            TypeError: If severity_level is not a string.
            ValueError: If severity_level is empty.
        """
        # Validate and set a new severity level
        if not isinstance(severity_level, str):
            raise TypeError('Severity level must be a string.')
        if severity_level.strip() == '':
            raise ValueError('Severity level should not be empty.')

        # Validate against allowed values
        if severity_level.lower() not in self.VALID_SEVERITY_LEVELS:
            raise ValueError(f'Severity level must be one of: {", ".join(self.VALID_SEVERITY_LEVELS)}')

        self.__severity_level = severity_level

    def set_treatment_plan(self, treatment_plan: str) -> None:
        """
         Set a new treatment plan for the health issue.

        Args:
            treatment_plan (str): New treatment plan to set.

        Raises:
            TypeError: If treatment_plan is not a string.
            ValueError: If treatment_plan is empty.
        """
        # Validate and set a new treatment plan
        if not isinstance(treatment_plan, str):
            raise TypeError('Treatment plan must be a string.')
        if treatment_plan.strip() == '':
            raise ValueError('Treatment plan should not be empty.')
        self.__treatment_plan = treatment_plan

# =========================== Properties =============================================================
    issue = property(get_issue, set_issue)
    date_reported = property(get_date_reported, set_date_reported)
    severity_level = property(get_severity_level, set_severity_level)
    treatment_plan = property(get_treatment_plan, set_treatment_plan)

# =========================== Methods ===============================================================
    def update_treatment(self, new_plan: str) -> str:
        """
        Updates the treatment plan for this record.

        Args:
            new_plan (str): The new treatment plan.

        Returns:
            str: Confirmation message after updating.
        """
        # Ensure the new treatment plan is a string
        if not isinstance(new_plan, str):
            raise TypeError('The treatment plan must be a string.')

        # Ensure the new treatment plan is not empty or just whitespace
        if new_plan.strip() == '':
            raise ValueError('The treatment plan should not be empty.')

        # Update the treatment plan using the setter
        self.treatment_plan = new_plan

        # Return a confirmation message
        return f'Treatment plan updated: {self.treatment_plan}'

    def update_severity(self, new_level: str) -> str:
        """
        Updates the severity level of this record.

        Args:
            new_level (str): New severity level.

        Returns:
            str: Confirmation message after updating.
        """
        # Ensure the new severity level is a string
        if not isinstance(new_level, str):
            raise TypeError('The severity level must be a string.')

        # Ensure the new severity level is not empty or whitespace
        if new_level.strip() == '':
            raise ValueError('The severity level should not be empty.')

        # Update the severity level using the setter
        self.severity_level = new_level

        # Return a confirmation message
        return f'Severity level updated: {self.severity_level}'

    def summary(self) -> str:
        """
        Returns a concise summary of the health record.

        Returns:
            str: One line summary of the health issue and severity.
        """
        # Return a concise summary of the health record
        return f'{self.issue} ({self.severity_level}) reported on {self.date_reported}'

    def is_critical(self) -> bool:
        """
         Checks if the severity level is critical.

        Returns:
            bool: True if severity is 'High' or 'Critical', False otherwise.
        """
        # Check if the severity level is critical (High or Critical)
        return self.severity_level.lower() in ('high', 'critical')


    def __str__(self) -> str:
        """
        Returns a detailed string representation of the health record.

        Returns:
            str: Multi line description of the health issue, severity, date, and treatment.
        """
        # Return a detailed multi-line string representation of the health record
        return (f'Health Issue: {self.issue}\n'
                f'Severity: {self.severity_level}\n'
                f'Date: {self.date_reported}\n'
                f'Treatment: {self.treatment_plan}\n')

    def __eq__(self, other) -> bool:
        """
        Compare two HealthRecord objects based on their key attributes.

        Args:
            other (HealthRecord): Another health record to compare.

        Returns:
            bool: True if records match, False otherwise.
        """
        if not isinstance(other, HealthRecord):
            return False
        return (self.issue == other.issue and
                self.date_reported == other.date_reported and
                self.severity_level == other.severity_level)