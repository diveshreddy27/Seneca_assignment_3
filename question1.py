from datetime import date
#imported date class from datetime module

class Cycle:
    """
    This class is all about the make(Company of the vehicle), model and years old of the vehicle 
    
    it consists of some methods:
            __init__ method : where it initialises all the values to the variables which are given by the user,
                              when he creates the object to the CYcle class
            age_of_vehicle method : we can get the age of the vehicle since the owner purchased it
                 
    """
    
    def __init__(self,make,model,year_of_purchased):
        """
        this method assigns the variables to the instance(self.variable_name) to access any where in the whole class
         
        Args:
            make (string type): it refers to company of the vehicle
            model (string type): it refers to which model of the it is
            year (integer type): it refers to in which year the owner bought the vehicle
            
        """
        self.make = make
        self.model = model
        self.year = year_of_purchased
    
    def age_of_vehicle(self):
        """
        this method access the value of the year of purchased and returns the age or how many years it happened after purchasing the vehicle
        
        Args:
            self : it is an instance of this class where we can access some variables
            
        returns:
            age_of_the_vehicle(integer type) : it returns the age of the pariticular vehicle
             
        """
        present_year = date.today()
        
        age_of_the_vehicle = present_year.year - self.year
        
        return age_of_the_vehicle
        
class MotorCycle(Cycle):
    def __init__(self, make, model, year_of_purchased):
        super().__init__(make, model, year_of_purchased)
        
obj = MotorCycle("TVS","Apache 200",2017)

print("company of the motor cycle is : ",obj.make)
print("model name of the respective company is :",obj.model)
print("Year of purchase of the motor cycle is :",obj.year)

print("age of the vehicle is : ",obj.age_of_vehicle())


    