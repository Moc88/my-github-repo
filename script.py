TEMPLATE_PATH = 'templates'
CONTRACTS_PATH = 'contracts'
EMPLOYEE_DB_PATH = 'employees.txt'
TEMPLATES = ['salary change', 'job change', 'contract prolongation']

employees = open('employees.txt')
text = employees.read()
print(text)