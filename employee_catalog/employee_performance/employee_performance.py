"""
Subclass to Employee class that contains performance information

"""
from ..employee import Employee
class Performance(Employee):
    def __init__(self, employee_name, employee_id, employee_email, performance_score, employee_rating):
        super().__init__(employee_name, employee_id, employee_email)
        self.performance_score = performance_score
        self.employee_rating = employee_rating
    
    def _get_employee_performance(self):
        """
        Private method to retrieve the performance metrics of an employee.

        Returns:
            None
        """
        pass

    def _get_employee_rating(self):
        """
        Private method to retrieve the employee rating of an employee.
        """
        pass

