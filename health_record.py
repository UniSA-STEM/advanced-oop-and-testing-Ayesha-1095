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
    """

def __init__(self, description, date_reported, severity_level, treatment_plan):
    self._description = description
    self._date_reported = date_reported
    self._severity_level = severity_level
    self._treatment_plan = treatment_plan

def __str__(self):
    """
    Returns a string representation of the health record.
    """
    return (f'Issue: {self._description}\n'
            f'Severity: {self._severity_level}\n'
            f'Date: {self._date_reported}\n'
            f'Treatment: {self._treatment_plan}\n')
