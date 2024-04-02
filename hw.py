# Problem One
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner

if __name__ == "__main__":
    vehicle1 = Vehicle("1", "Car", "Alexa")
    vehicle2 = Vehicle("2", "Motorcycle", "Maria")
    vehicle3 = Vehicle("3", "Truck", "Yasmin")
    print("Initial Vehicle Information:")
    print("Vehicle 1 - Reg Num:", vehicle1.registration_number, "Type:", vehicle1.type, "Owner:", vehicle1.owner)
    print("Vehicle 2 - Reg Num:", vehicle2.registration_number, "Type:", vehicle2.type, "Owner:", vehicle2.owner)
    print("Vehicle 3 - Reg Num:", vehicle3.registration_number, "Type:", vehicle3.type, "Owner:", vehicle3.owner)
    
    vehicle1.update_owner("Olivia")
    vehicle2.update_owner("Robert")
    
    print("\nVehicle Information after updating owner:")
    print("Vehicle 1 - Reg Num:", vehicle1.registration_number, "Type:", vehicle1.type, "Owner:", vehicle1.owner)
    print("Vehicle 2 - Reg Num:", vehicle2.registration_number, "Type:", vehicle2.type, "Owner:", vehicle2.owner)
    print("Vehicle 3 - Reg Num:", vehicle3.registration_number, "Type:", vehicle3.type, "Owner:", vehicle3.owner)        
   

# Problem Two
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count