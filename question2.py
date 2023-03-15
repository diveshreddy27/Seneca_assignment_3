
class Employee:
    """
    Employee class only stores the values of the employees at respective objectiives
    """
    def __init__(self, name, id_num, department):
        """
        this method assigns the variables to the instance(self.variable_name) to access any where in the whole class
        
        Args:
            name (string type): name of the respective employee
            id_num (integer type): employee id of the respective employee
            department (string type): department name of the respective employee
        """
        self.name = name
        self.id_num = id_num
        self.department = department
        
class Department:
    """
    this Department class only stores the values of the employees at respective objectiives
    """
    
    def __init__(self, name):
        """
        this method assigns the variables to the instance(self.variable_name) to access any where in the whole class

        Args:
            name (string type): name refers to department name
        """
        self.name = name

class Details:
    """
    this class consists of total 4 methods:(consists of total 3 class methods) and 2 class variables
    
    class variables :
        department_list
        employee_list
        
    Methods:
            __init__ method: staring point of the whole program where it interacts with user for the input
            
            class methods:
                enter_employee_details 
                enter_department_details
                show_details
            
    """
    employee_list = []
    department_list = []

    def __init__(self):
        """
        it display the options and takes input from the user and act according to it
        """
        
        while(1):
            print("Please select any one option from the given options :")
            print("\t\t1- Enter employee details")
            print("\t\t2- Enter Department Details")
            print("\t\t3- Show the list of employees and department details")
            print("\t\t4- Exit")
            user_opt = input("Enter only given options number : ")
            
            if( not (user_opt.isdigit())):
                print("Please enter only numbers")
            else:
                user_opt = int(user_opt)
                if user_opt == 1:
                    Details.enter_employee_details()
                elif user_opt == 2:
                    Details.enter_department_details()
                elif user_opt == 3:
                    Details.show_details()
                elif user_opt == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid, Please enter a valid option.")
                    
    @classmethod
    def enter_employee_details(cls):
        """
        this method takes input from the user about the details of the employee
        
        variables :
            name,id_num,department
        """
        name = input("Enter employee name: ")
        id_num = input("Enter employee ID number: ")
        department = input("Enter employee department: ")
        employee = Employee(name, id_num, department)
        cls.employee_list.append(employee)

    @classmethod
    def enter_department_details(cls):
        """
        this method takes input from the user about the details of the Department
        
        variables :
            department
        """
        name = input("Enter department name: ")
        department = Department(name)
        cls.department_list.append(department)
    
    @classmethod
    def show_details(cls):
        """
        this method is used to display the details of the employees and departments entered
        """
        print("Employee List:")
        for employee in cls.employee_list:
            print(f"{employee.name}, {employee.id_num}, {employee.department}")
        print("Department List:")
        for department in cls.department_list:
            print(f"{department.name}")
            
obj = Details()