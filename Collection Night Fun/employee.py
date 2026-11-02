employee_list = [("John", "IT", 50000), ("Jane", "HR", 45000), ("Mike", "IT", 60000), ("Sara", "Finance", 70000)]

for employee_name, employee_department, employee_salary in employee_list:
      print(f"""Name: , {employee_name}
      Department: , {employee_department}
      Salary: ", {employee_salary}""")
    

def departmental_employee(employee_list):
    employee_name, employee_department, employee_salary = employee_list
    return  employee_department == "IT"
print(list(filter(departmental_employee, employee_list)))


def salary(employee_list):
    employee_name, employee_department, employee_salary = employee_list
    return  employee_salary > 55000
print(list(filter(salary, employee_list)))




