class Customer:
    
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)
        
    def set_given_name(self, new_given_name):
        if (type(new_given_name) == str):
            self._given_name = new_given_name
        else:
            print("The value must be a string.")
            
    def get_given_name(self):
        return self._given_name
    
    _given_name = property(set_given_name, get_given_name)

    def set_family_name(self, new_family_name):
        if (type(new_family_name) == str):
            self._family_name = new_family_name
        else:
            print("The value must be a string.")
         
    def get_family_name(self):
        return self._family_name
    
    _family_name = property(get_family_name, set_family_name)
    
    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers
            
  
