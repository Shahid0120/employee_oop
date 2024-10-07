"""

This is based on my Prototype 2 UML

"""

class Employee():
    def __init__(self, employee_name : str, employee_id : int, employee_email : str) -> None:
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_email = employee_email
    
    def locate(self):
        pass
    
    def _get_employee_performance(self):
        """
        Private method to retrieve the performance metrics of an employee.

        Returns:
            None
        """
        pass

    def _get_employee_demographics(self):
        pass

    def _get_employee_company_details(self):
        pass
