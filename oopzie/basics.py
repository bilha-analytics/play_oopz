import datetime
from copy import deepcopy

class Employee:
    etype = 'Staff'
    num_of_emps = 0    
    raise_rate = 1.5 

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay 
        # self.email = self.gen_email() 
        Employee.num_of_emps += 1
        self.id = Employee.num_of_emps 

    @property 
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self, names):
        fname, lname = names.split(' ')
        self.fname = fname
        self.lname = lname
    

    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None
    
    @property 
    def email(self):
        return f"{self.fname}.{self.lname}@company.com" 

    def apply_raise(self):
        self.pay = int( int(self.pay) * self.raise_rate )

    @classmethod  ##@ update class variables such that instances can also do the same (not necc good practice)
    def set_raise_amount(self, amount):
        self.raise_rate = amount 

    @classmethod ##@ alternative constructor use ase 
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-' ) 
        return cls(fname, lname, pay) 

    @staticmethod
    def is_workday(day):
        return False if day.weekday() >=5 else True 


    ######Dunders 
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname ) 

    def __repr__(self):
        #return f"{type(self)}:: {self.id}, {self.etype}, {self.pay}"
        return f"{self.__class__.__name__}('{self.fname}', '{self.lname}', '{self.pay}')"

    def __str__(self):
        return f"""
--- Employee ({self.id}  of {Employee.num_of_emps})---
Name:   {self.fullname}
Email:  {self.email}
Pay:    {self.pay}
Type:   {self.etype}
Len:    {len(self)}"""


class Manager(Employee): 
    etype = 'Manager'
    docket = 'Budgetary' 

    def __init__(self, fname, lname, pay, empz=None): ## don't pass mutalebles as defaults; use None instead
        super().__init__(fname, lname, pay) 
        self.empz = [] if empz is None else empz 

    
    def add_emp(self, emp):
        if emp not in self.empz:
            self.empz.append( emp ) 
    


    def empz_salary_budget(self):
        # res = deepcopy(self) 
        amt = 0 
        for e in self.empz: 
            # res.pay = res + e 
            amt += e.pay

        # return res.pay 
        return amt 

    def str_empz(self):
        res = f">>>>> BEGIN Reportees for {self.fullname}"
        for e in self.empz:
            res = f"""
    {res}
    {e.__str__()}"""
        return f"{res}\n<<<<< END Reportees"


    def __repr__(self): 
        return f"{super().__repr__()}\n\t{self.empz}"
        

    def __str__(self):
        return f"""
{super().__str__()} 
Docket: {self.docket}
Salary Budget: {self.empz_salary_budget()}
Employees: {self.str_empz() }
    """

class Developer(Employee):
    raise_rate = 10 
    etype = 'Developer'

    def __init__(self, fname, lname, pay, lang):
        #Employee.__init__(self, fname, lname, pay) ## BUT may get messy to manager when dealing with multiple inheritance
        super().__init__(fname, lname, pay)
        self.lang = lang 

    def __str__(self):
        return f"""
{super().__str__()} 
Lang:   {self.lang}
        """



if __name__ == '__main__':  
    emp = Employee('Jane', 'Smith', '102300')    
    print( f"{emp.fname} {emp.lname}, {emp.email}")
    print(  emp )
    emp.apply_raise()
    print(emp) 
    emp.set_raise_amount(2)

    emp2 = Developer('John', 'Doe', '30000', 'Ruby' )    
    emp2.apply_raise()

    emp3 = Manager.from_string( 'James-Otieno-100000')
    emp3.add_emp( emp ) 
    emp3.add_emp( emp2 ) 
    
    print(f"\n{'='*35}\n")
    emp.fullname = 'Maari Wakari'
    print(emp)
    print(emp2)  
    print(emp3)  
    

    print(f"\n{'='*35}\n")
    print(repr(emp3)   )

    print(f"\n{'='*35}\n")
    # d = datetime.date(2020, 7, 22 ) 
    # print( f"Is work day {d.strftime('%A, %d-%b-%Y')} is {Employee.is_workday(d) }")
    # d = datetime.date(2020, 7, 18 ) 
    # print( f"Is work day {d.strftime('%A, %d-%b-%Y')} is {Employee.is_workday(d) }")
    # d = datetime.datetime.now()
    # print( f"{d.strftime('%Z')} - {d.strftime('%x')} - {d.strftime('%c')}")

    # print( help(Manager))
    print( f'{type(emp3)} is instance of Employee = {isinstance(emp3, Employee)}' )
    print( f'{type(emp3)} is instance of Manager = {isinstance(emp3, Manager)}' )
    print( f'{type(emp3)} is instance of Developer = {isinstance(emp3, Developer)}' )
    print()
    print( f'{Manager.__class__} is subclass of Employee = {issubclass(Manager, Employee)}' )
    print( f'{type(Manager)} is subclass of Manager = {issubclass(Manager, Manager)}' )
    print( f'{type(emp3)} is subclass of Developer = {issubclass(Manager, Developer)}' )

    print(f"\n{'='*35}\n")
    print( emp + emp )
    print( emp + emp2 )
    # print( emp + emp3 )
    # print( emp2 + emp3 )
    del emp.fullname
    print( emp )
