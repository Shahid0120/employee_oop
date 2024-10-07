"""
This module defines a subsubclass for Employee and a subclass for EmployeeCompanyInformation.

Classes:
    EmployeeOrganisationLevel: Represents the organizational level of an employee within the company.
"""

class EmployeeOrganisationLevel(EmployeeCompanyInformation):
    def __init__(self, employee_name, employee_id, employee_email, employee_type, employee_title, employee_classfications, employee_payzone, employee_level, employee_department, employee_division, employee_business_level):
        super().__init__(employee_name, employee_id, employee_email, employee_type, employee_title, employee_classfications, employee_payzone)
        self.employee_department = employee_department
        self.employee_division = employee_division
        self.employee_business_level = employee_business_level


    def _get_employee_organisation_level(self):
        """
        Private method to retrieve the organizational level of an employee.

        Returns:
            None
        """
        pass