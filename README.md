# Main Goals
- Fit a GUI for employment management system using Object orientated software development lifecycle
- Utilise Key Concepts of Object orientated Programming Abstraction, encapsulation, inheritance, and polymorphism
- Upon creating a MVP solution, hold multiple code review, refactoring code using and implementing design patterns.

# Key Dates Logs: 
- 5th October : Imported Dataset, started reading Python 3 Object-Oriented Programming" by Dusty Phillips Chapter 1/2/3. Created ficticious bussiness requirements for GUI employee dataset. Conducted Basic EDA, finding dtypes, columns, samples index. 




# Key Links and Resources used :
- Learning OO software development : Python 3 Object-Oriented Programming" by Dusty Phillips
- Dataset: https://www.kaggle.com/datasets/ravindrasinghrana/employeedataset
- Design Patterns and Refactoring : https://refactoring.guru/

# Stage of Object Oriented Software Development Cycle 

## Object Orientated Analysis 

### Business Object 
This is a set of random business requirements I have generated using ChatGPT 

**Business Requirements for the Employee Management System**:
- Employee Information Management:
    - Objective: Develop a module that maintains comprehensive employee records.
    - Details: The system should enable HR to view and update employee profiles, including personal information, employment status, job title, and supervisor details. It should also support tracking employee status changes (e.g., Active, On Leave, Terminated) and historical employment data.

- Training and Development Management:
    - Objective: Implement a training management feature to streamline the administration of employee training programs.
    - Details: The system should allow HR to schedule training sessions, assign employees to different programs, and track their attendance and completion status. Additionally, it should include the capability to store training outcomes and generate reports on training participation by business units or departments.
    
- Recruitment and Applicant Tracking:
    - Objective: Create a recruitment module to manage the hiring process and applicant information.
    - Details: The system should support applicant tracking, status management (e.g., Submitted, Under Review, Selected, Rejected), and application history. It should provide an interface to view applicant details, schedule interviews, and track recruitment metrics.

- Employee Engagement and Survey Analysis:
    - Objective: Develop a survey management module to collect, store, and analyze employee engagement data.
    - Details: The module should facilitate the collection of survey responses and provide HR with tools to generate summary reports based on engagement scores, satisfaction scores, and work-life balance scores.

- Performance Evaluation and Employee Rating:
    - Objective: Build a performance management module that captures employee performance ratings and evaluations.
    - Details: The system should allow supervisors to record employee performance scores and generate performance evaluation reports. Historical performance data should be accessible for trend analysis and decision-making regarding promotions or training needs.

- Department and Business Unit Management:
    - Objective: Implement department-level tracking and reporting capabilities.
    - Details: The system should support the creation and management of departments, including assigning employees to departments, tracking departmental headcounts, and linking departments to broader business units.

- Employee Movement and Position Tracking:
    - Objective: Establish a module to track employee job movements, promotions, and role changes.
    - Details: The system should record job title changes, departmental transfers, and pay zone adjustments. This will help in maintaining an up-to-date organizational structure and support workforce planning.

## EDA 

The following contains summary of dtype, input format and sample input

**Employee Data**

Columns:
- EmpID | dtype: int64 | 1194
- FirstName | dtype: object | Maximilian
- LastName | dtype: object | Silva
- StartDate | dtype: object | 08-Jan-21
- ExitDate | dtype: object | 23-Sep-20
- Title | dtype: object | Production Technician I
- Supervisor | dtype: object | Alfred Sanders
- ADEmail | dtype: object | dorian.fox@bilearner.com
- BusinessUnit | dtype: object | ['CCDR' 'EW' 'PL' 'TNS' 'BPC' 'WBL' 'NEL' 'SVG' 'MSC' 'PYZ']
- EmployeeStatus | dtype: object | ['Active' 'Future Start' 'Voluntarily Terminated' 'Leave of Absence'
 'Terminated for Cause']
- EmployeeType | dtype: object | ['Contract' 'Full-Time' 'Part-Time']
- PayZone | dtype: object | ['Zone C' 'Zone A' 'Zone B']
- EmployeeClassificationType | dtype: object | ['Temporary' 'Part-Time' 'Full-Time']
- TerminationType | dtype: object | ['Unk' 'Involuntary' 'Resignation' 'Retirement' 'Voluntary']
- TerminationDescription | dtype: object | Its card benefit dream bring.
- DepartmentType | dtype: object | ['Production       ' 'Sales' 'IT/IS' 'Executive Office'
 'Software Engineering' 'Admin Offices']
- Division | dtype: object | Project Management - Eng
- DOB | dtype: object | 11-08-1966
- State | dtype: object | MA
- JobFunctionDescription | dtype: object | Lineman
- GenderCode | dtype: object | ['Female' 'Male']
- LocationCode | dtype: int64 | 25699
- RaceDesc | dtype: object | ['White' 'Hispanic' 'Other' 'Black' 'Asian']
- MaritalDesc | dtype: object | ['Widowed' 'Single' 'Married' 'Divorced']
- Performance Score | dtype: object | ['Fully Meets' 'Exceeds' 'Needs Improvement' 'PIP']
- Current Employee Rating | dtype: int64 | 1


**Employee Engagement Survey Data**

Columns: 
- Employee ID | dtype: int64 | 1167
- Survey Date | dtype: object | 26-04-2023
- Engagement Score | dtype: int64 | 1
- Satisfaction Score | dtype: int64 | 3
- Work-Life Balance Score | dtype: int64 | 1

**Recruitment Data**

Columns:
- Applicant ID | dtype: int64 | 3571
- Application Date | dtype: object | 10-Jul-23
- First Name | dtype: object | Michelle
- Last Name | dtype: object | Whitaker
- Gender | dtype: object | ['Male' 'Female' 'Other']
- Date of Birth | dtype: object | 19-07-2001
- Phone Number | dtype: object | 235-368-3239x12382
- Email | dtype: object | deborahkrause@example.com
- Address | dtype: object | 29762 Julian Lodge Suite 738
- City | dtype: object | Lake Kristen
- State | dtype: object | TN
- Zip Code | dtype: int64 | 62173
- Country | dtype: object | Mauritania
- Education Level | dtype: object | ['High School' "Bachelor's Degree" 'PhD' "Master's Degree"]
- Years of Experience | dtype: int64 | 17
- Desired Salary | dtype: float64 | 93325.91
- Job Title | dtype: object | Sports therapist
- Status | dtype: object | ['Interviewing' 'Rejected' 'In Review' 'Offered' 'Applied']

**Training and Development Data**

Columns:
- Employee ID | dtype: int64 | 3787
- Training Date | dtype: object | 12-Oct-22
- Training Program Name | dtype: object | ['Customer Service' 'Leadership Development' 'Technical Skills', 'Communication Skills' 'Project Management']
- Training Type | dtype: object | ['Internal' 'External']
- Training Outcome | dtype: object | ['Failed' 'Incomplete' 'Completed' 'Passed']
- Location | dtype: object | Claychester
- Trainer | dtype: object | Jose King
- Training Duration(Days) | dtype: int64 | 2
- Training Cost | dtype: float64 | 154.71

# Object Orientated Design 


