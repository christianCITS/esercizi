class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str,number_served:int=0):
        self.restaurant_name:str=restaurant_name
        self.cuisine_type:str=cuisine_type
        self.number_served=number_served
    
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name},{self.cuisine_type}")

    
    def open_restaurant(self):
        print(f"Il ristorante è APERTO!")
    
    def set_number_served(self,numb_serv:int)-> int:
        self.number_served=numb_serv
        return self.number_served
        
    def increment_number_served(self,incr_serv:int)-> int:
        self.number_served+=incr_serv 
        return self.number_served