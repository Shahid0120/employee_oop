"""
This is the init file for the employee_catalog package.
It imports the following modules:
- Employee: Handles employee-related operations.
- Performance: Manages employee performance data.
- EmployeeCompanyInformation: Contains information about the employee's company.
- Demographics: Manages demographic information of employees.
"""""

from .employee import Employee
from .employee_performance.employee_performance import Performance
from .employee_company_information.employee_company_information import EmployeeCompanyInformation
from .employee_demographics.employee_demographics import Demographics

