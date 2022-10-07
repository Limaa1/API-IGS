Instructions for running the "IGS-Software Manager":

Prerequisites: having python installed.

Step by step:

1 - Install the libraries inside the "requirements.txt" file.

2 - Inside the IGS-Software Manager folder, use the command "python manage.py runserver" to run the program.

3 - Open the following addresses in the browser:
	- http://localhost:8000/index/ > access list with all employees.
	- http://localhost:8000/employee/ > use the employees API.
	- http://localhost:8000/department/ > use the departments API.
	- http://localhost:8000/admin/ > access admin panel. Need to create a superuser through terminal.

4 - To edit and delete specific employees and departments, it is necessary to put the id in front of the address, for example: 
	- http://localhost:8000/employee/1/
	- http://localhost:8000/department/1/

Validations:
- Cannot create an email that has already been registered.
- Cannot create an email that does not meet the regular expressions.
- Cannot assign a department that does not exist to an employee.
- Cannot create a department that has already been registered.
