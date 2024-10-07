"""
Subclass to Employee class that contains employee company information
"""
from ..employee import Employee

class EmployeeCompanyInformation(Employee):
    def __init__(self, employee_name, employee_id, employee_email, employee_type, employee_title, employee_classfications, employee_payzone):
        super().__init__(employee_name, employee_id, employee_email)
        self.employee_title = employee_title
        self.employee_type = employee_type
        self.employee_classfications = employee_classfications
        self.employee_payzone = employee_payzone
    
    def locate(self):
        pass