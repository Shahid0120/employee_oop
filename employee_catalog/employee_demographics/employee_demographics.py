"""

Subclass to Employee class that contains demographic information

"""
from .employee import Employee

class Demographics(Employee):
    def __init__(self, employee_age, race, gender, location, state, marital_status, employee_name, employee_id, employee_email):
        super().__init__(employee_name, employee_id, employee_email)
        self.age = employee_age
        self.race = race
        self.gender = gender
        self.location = location
        self.state = state
        self.marital_status = marital_status
        self
    
    def _get_employee_demograhics(self):
        """
        Private method to retrieve the demographic metrics of an employee.

        Returns:
            None
        """
        pass